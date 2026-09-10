from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch


DATA_PATH = Path(__file__).with_name("penguins.csv")
OUTPUT_PATH = Path(__file__).with_name("penguin_bill_depth_by_sex_species.png")


def main() -> None:
    penguins = pd.read_csv(DATA_PATH, na_values=["NA"])
    plot_data = penguins.dropna(
        subset=["bill_depth_mm", "sex", "species"]
    )

    species_order = ["Adelie", "Chinstrap", "Gentoo"]
    sex_order = ["female", "male"]
    sex_colors = {"female": "#2f6db0", "male": "#c94c4c"}
    positions = []
    box_data = []
    box_colors = []
    labels = []

    for species_index, species in enumerate(species_order):
        for sex_index, sex in enumerate(sex_order):
            group = plot_data[
                (plot_data["species"] == species) & (plot_data["sex"] == sex)
            ]
            positions.append(species_index * 3 + sex_index + 1)
            box_data.append(group["bill_depth_mm"])
            box_colors.append(sex_colors[sex])
            labels.append(f"{species}\n{sex.title()}")

    plt.style.use("seaborn-v0_8-whitegrid")
    figure, axis = plt.subplots(figsize=(10, 6.5), dpi=160)
    figure.patch.set_facecolor("#f7f4ee")
    axis.set_facecolor("#fffdf8")

    boxplot = axis.boxplot(
        box_data,
        positions=positions,
        widths=0.72,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": "#fffdf8", "linewidth": 2},
        whiskerprops={"color": "#4f5a60", "linewidth": 1.2},
        capprops={"color": "#4f5a60", "linewidth": 1.2},
        boxprops={"edgecolor": "#4f5a60", "linewidth": 1.1},
    )
    for patch, color in zip(boxplot["boxes"], box_colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.9)

    axis.set_title(
        "Penguin bill depth by species and sex",
        fontsize=18,
        fontweight="bold",
        color="#24313a",
        pad=16,
    )
    axis.set_xticks(positions, labels)
    axis.set_xlabel("Species and sex", fontsize=12, labelpad=10)
    axis.set_ylabel("Bill depth (mm)", fontsize=12, labelpad=10)
    axis.set_xlim(0.25, positions[-1] + 0.75)
    axis.legend(
        handles=[
            Patch(facecolor=sex_colors["female"], label="Female"),
            Patch(facecolor=sex_colors["male"], label="Male"),
        ],
        title="Sex",
        frameon=True,
        facecolor="#fffdf8",
        edgecolor="#d8d2c8",
        fontsize=10,
        title_fontsize=11,
    )
    axis.grid(color="#d8d2c8", linewidth=0.8, alpha=0.65)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)
    axis.spines["left"].set_color("#b8b1a7")
    axis.spines["bottom"].set_color("#b8b1a7")
    axis.tick_params(colors="#4f5a60")
    figure.text(
        0.01,
        0.01,
        f"Showing {len(plot_data)} penguins with complete bill depth, sex, and species data",
        fontsize=9,
        color="#68747a",
    )
    figure.tight_layout(rect=(0, 0.04, 1, 1))
    figure.savefig(OUTPUT_PATH, bbox_inches="tight", facecolor=figure.get_facecolor())
    plt.close(figure)
    print(f"Saved {OUTPUT_PATH.name} with {len(plot_data)} plotted rows")


if __name__ == "__main__":
    main()
