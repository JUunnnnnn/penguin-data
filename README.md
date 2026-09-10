# Making Conclusions from Penguin Data Graphs

Graphs turn the measurements in `penguins.csv` into patterns that are easier to compare than a table of individual rows. A useful graph does more than display values: it connects a question, a visual comparison, and a conclusion that is supported by the data.

## The question behind this graph

The project asks how bill depth varies across penguin species and sex. The box plot groups observations into six categories: Adelie, Chinstrap, and Gentoo, each split into female and male penguins. Female boxes are blue and male boxes are red.

## Why use a box plot?

A box plot summarizes each group with its median, middle 50 percent of values, overall whisker range, and possible outliers. Comparing the boxes helps us examine:

- **Typical values:** a higher median indicates a greater typical bill depth.
- **Variation:** a taller box means the middle half of the group is more spread out.
- **Overlap:** substantial overlap means species or sex groups may be less clearly separated by bill depth alone.
- **Unusual observations:** points beyond the whiskers can identify values worth checking.

## Conclusions suggested by the data

The graph suggests that species is strongly associated with bill depth. Gentoo penguins generally have shallower bills than Adelie and Chinstrap penguins, while Chinstrap penguins tend to have the deepest bills in this dataset. Within each species, the male and female distributions are also separated, with male bill depth generally higher than female bill depth.

These are descriptive conclusions about the recorded penguins. They do not prove that species or sex causes a particular bill depth, and bill depth alone should not be used to identify every penguin. Stronger conclusions would require a defined sampling method, statistical tests, and consideration of other measurements such as bill length, flipper length, body mass, island, and year.

## Reproduce the graph

Requirements: Python and [uv](https://docs.astral.sh/uv/).

```powershell
uv run --with pandas --with matplotlib python plot_penguins.py
```

The script excludes rows missing species, sex, or bill depth and writes `penguin_bill_depth_by_sex_species.png`.

## Project files

- `penguins.csv`: Penguin measurements.
- `plot_penguins.py`: Graph-generation script.
- `penguin_bill_depth_by_sex_species.png`: Generated box plot.
- `agents.md`: Workspace guidance for using `uv` with Python.
