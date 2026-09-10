from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path(__file__).with_name("penguins.csv")
OUTPUT_PATH = Path(__file__).with_name("penguin_mass_vs_flipperlength.png")


def main() -> None:
    penguins = pd.read_csv(DATA_PATH, na_values=["NA"])
    plot_data = penguins.dropna(
        subset=["flipper_length_mm", "body_mass_g", "species"]
    )

    species_styles = {
        "Adelie": {"color": "#007c91", "marker": "o"},
        "Chinstrap": {"color": "#d95f02", "marker": "s"},
        "Gentoo": {"color": "#5e3c99", "marker": "^"},
    }

    plt.style.use("seaborn-v0_8-whitegrid")
    figure, axis = plt.subplots(figsize=(10, 6.5), dpi=160)
    figure.patch.set_facecolor("#f7f4ee")
    axis.set_facecolor("#fffdf8")

    for species, style in species_styles.items():
        species_data = plot_data[plot_data["species"] == species]
        axis.scatter(
            species_data["flipper_length_mm"],
            species_data["body_mass_g"],
            label=species,
            color=style["color"],
            marker=style["marker"],
            s=62,
            alpha=0.82,
            edgecolors="#fffdf8",
            linewidths=0.7,
        )

    axis.set_title(
        "Penguin body mass rises with flipper length",
        fontsize=18,
        fontweight="bold",
        color="#24313a",
        pad=16,
    )
    axis.set_xlabel("Flipper length (mm)", fontsize=12, labelpad=10)
    axis.set_ylabel("Body mass (g)", fontsize=12, labelpad=10)
    axis.legend(
        title="Species",
        frameon=True,
        facecolor="#fffdf8",
        edgecolor="#d8d2c8",
        title_fontsize=11,
        fontsize=10,
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
        f"Showing {len(plot_data)} penguins with complete mass, flipper length, and species data",
        fontsize=9,
        color="#68747a",
    )
    figure.tight_layout(rect=(0, 0.04, 1, 1))
    figure.savefig(OUTPUT_PATH, bbox_inches="tight", facecolor=figure.get_facecolor())
    plt.close(figure)
    print(f"Saved {OUTPUT_PATH.name} with {len(plot_data)} plotted rows")


if __name__ == "__main__":
    main()
