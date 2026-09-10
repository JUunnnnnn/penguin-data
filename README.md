# Penguin Bill Depth by Sex and Species

This project creates a publication-ready box plot of penguin bill depth, split by species and sex. Female boxes are blue and male boxes are red.

## Requirements

- Python
- [uv](https://docs.astral.sh/uv/)

## Run the plot

From this directory, run:

```powershell
uv run --with pandas --with matplotlib python plot_penguins.py
```

The script reads `penguins.csv` and writes `penguin_bill_depth_by_sex_species.png`.

Rows missing species, sex, or bill depth are excluded from the plot. Adelie, Chinstrap, and Gentoo penguins are shown as separate female and male boxes.

## Project files

- `penguins.csv`: Penguin measurements.
- `plot_penguins.py`: Plotting script.
- `penguin_bill_depth_by_sex_species.png`: Generated plot.
- `agents.md`: Workspace guidance for using `uv` with Python.