# Penguin Mass vs. Flipper Length

This project creates a publication-ready scatter plot of penguin body mass versus flipper length, using a different marker for each species.

## Requirements

- Python
- [uv](https://docs.astral.sh/uv/)

## Run the plot

From this directory, run:

```powershell
uv run --with pandas --with matplotlib python plot_penguins.py
```

The script reads `penguins.csv` and writes `penguin_mass_vs_flipperlength.png`.

Rows missing species, flipper length, or body mass are excluded from the plot. Adelie, Chinstrap, and Gentoo penguins are shown with distinct colors and symbols.

## Project files

- `penguins.csv`: Penguin measurements.
- `plot_penguins.py`: Plotting script.
- `penguin_mass_vs_flipperlength.png`: Generated plot.
- `agents.md`: Workspace guidance for using `uv` with Python.