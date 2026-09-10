from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path(__file__).parent / "class examples" / "penguins.csv"
OUTPUT_PATH = Path(__file__).parent / "penguins_bill_length_depth_by_island.png"


def main() -> None:
    penguins = pd.read_csv(DATA_PATH, na_values=["NA"])
    penguins = penguins.dropna(
        subset=["island", "bill_length_mm", "bill_depth_mm"]
    )

    island_order = ["Biscoe", "Dream", "Torgersen"]
    styles = {
        "Biscoe": {"color": "#1479A8", "marker": "o"},
        "Dream": {"color": "#D95F59", "marker": "s"},
        "Torgersen": {"color": "#2A9D69", "marker": "^"},
    }

    figure, axis = plt.subplots(figsize=(12, 6), dpi=160)
    figure.patch.set_facecolor("#F7F4EE")
    axis.set_facecolor("#F7F4EE")

    for island in island_order:
        island_data = penguins[penguins["island"] == island]
        style = styles[island]
        axis.scatter(
            island_data["bill_length_mm"],
            island_data["bill_depth_mm"],
            label=island,
            s=58,
            alpha=0.6,
            color=style["color"],
            marker=style["marker"],
            edgecolor="#FFFFFF",
            linewidth=0.7,
        )

    axis.set_xlabel(
        "Bill length (mm)", fontsize=16, labelpad=12, color="#455A64"
    )
    axis.set_ylabel(
        "Bill depth (mm)", fontsize=16, labelpad=12, color="#455A64"
    )
    axis.set_xlim(30, 60)
    axis.set_ylim(13, 22)
    axis.grid(axis="y", color="#D9D6CF", linewidth=0.8)
    axis.set_axisbelow(True)
    axis.spines[:].set_color("#9AA6A8")
    axis.tick_params(
        axis="both", colors="#455A64", labelsize=13, length=0, pad=8
    )
    axis.legend(
        title="Island",
        title_fontsize=14,
        fontsize=13,
        frameon=True,
        ncols=1,
        loc="upper left",
        bbox_to_anchor=(1.02, 1),
        borderpad=0.8,
        edgecolor="#9AA6A8",
        facecolor="#F7F4EE",
        handletextpad=0.5,
        columnspacing=1.5,
    )

    figure.tight_layout(rect=(0, 0, 0.82, 1))
    figure.savefig(OUTPUT_PATH, facecolor=figure.get_facecolor(), bbox_inches="tight")
    print(f"Saved plot to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()