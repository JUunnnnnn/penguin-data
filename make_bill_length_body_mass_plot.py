"""Create a species-coloured bill-length versus body-mass scatter plot."""
import csv
from html import escape

INPUT = "penguins.csv"
OUTPUT = "bill_length_vs_body_mass.svg"
WIDTH, HEIGHT = 900, 620
LEFT, RIGHT, TOP, BOTTOM = 105, 35, 75, 90
PLOT_W, PLOT_H = WIDTH - LEFT - RIGHT, HEIGHT - TOP - BOTTOM
COLORS = {"Adelie": "#2878b5", "Chinstrap": "#e07a22", "Gentoo": "#3ca370"}


def scale(value, low, high, start, length, invert=False):
    position = (value - low) / (high - low)
    return start + length * (1 - position if invert else position)


with open(INPUT, newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

points = []
for row in rows:
    bill_length, mass = row["bill_length_mm"], row["body_mass_g"]
    if bill_length in ("", "NA") or mass in ("", "NA"):
        continue
    points.append((float(bill_length), float(mass), row["species"]))

x_min, x_max = 30, 60
y_min, y_max = 2500, 6500
x_ticks = range(30, 61, 5)
y_ticks = range(2500, 6501, 500)
missing_count = len(rows) - len(points)

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
    '<style>text{font-family:Arial,sans-serif;fill:#222}.title{font-size:23px;font-weight:bold}.subtitle{font-size:13px;fill:#555}.axis{font-size:12px}.label{font-size:15px;font-weight:bold}.legend{font-size:13px}</style>',
    f'<rect width="{WIDTH}" height="{HEIGHT}" fill="white"/>',
    '<text x="105" y="32" class="title">Penguin bill length and body mass</text>',
    f'<text x="105" y="53" class="subtitle">Each point is one penguin; n = {len(points)} ({missing_count} rows with missing plotted measurements excluded)</text>',
]

for tick in x_ticks:
    x = scale(tick, x_min, x_max, LEFT, PLOT_W)
    svg += [f'<line x1="{x:.1f}" y1="{TOP}" x2="{x:.1f}" y2="{TOP + PLOT_H}" stroke="#e6e6e6"/>',
            f'<text x="{x:.1f}" y="{TOP + PLOT_H + 22}" text-anchor="middle" class="axis">{tick}</text>']
for tick in y_ticks:
    y = scale(tick, y_min, y_max, TOP, PLOT_H, invert=True)
    svg += [f'<line x1="{LEFT}" y1="{y:.1f}" x2="{LEFT + PLOT_W}" y2="{y:.1f}" stroke="#e6e6e6"/>',
            f'<text x="{LEFT - 12}" y="{y + 4:.1f}" text-anchor="end" class="axis">{tick:,}</text>']

svg.append(f'<rect x="{LEFT}" y="{TOP}" width="{PLOT_W}" height="{PLOT_H}" fill="none" stroke="#555"/>')
for bill_length, mass, species in points:
    x = scale(bill_length, x_min, x_max, LEFT, PLOT_W)
    y = scale(mass, y_min, y_max, TOP, PLOT_H, invert=True)
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{COLORS[species]}" fill-opacity=".72"><title>{escape(species)}: {bill_length:.1f} mm, {mass:,.0f} g</title></circle>')

svg += [
    f'<text x="{LEFT + PLOT_W / 2}" y="{HEIGHT - 25}" text-anchor="middle" class="label">Bill length (mm)</text>',
    f'<text x="25" y="{TOP + PLOT_H / 2}" text-anchor="middle" class="label" transform="rotate(-90 25 {TOP + PLOT_H / 2})">Body mass (g)</text>',
]
for index, species in enumerate(COLORS):
    x = 560 + index * 105
    svg += [f'<circle cx="{x}" cy="35" r="5" fill="{COLORS[species]}"/>',
            f'<text x="{x + 9}" y="39" class="legend">{species}</text>']
svg.append('</svg>')

with open(OUTPUT, "w", encoding="utf-8") as file:
    file.write("\n".join(svg))
print(f"Wrote {OUTPUT} with {len(points)} plotted observations.")
