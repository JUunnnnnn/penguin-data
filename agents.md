# Python Development

Use `uv` for all Python development tasks in this workspace.

## Required Workflow

- Install Python packages with `uv add <package>` for project dependencies.
- Install development-only packages with `uv add --dev <package>`.
- Run Python scripts with `uv run python <script.py>`.
- Run Python modules with `uv run python -m <module>`.
- Run project commands and tools through `uv run` so they use the project environment.
- Do not use `pip install`, `python -m pip install`, or a separate manually managed virtual environment unless explicitly requested.
- Prefer maintaining dependencies in `pyproject.toml` and the `uv.lock` lockfile.
