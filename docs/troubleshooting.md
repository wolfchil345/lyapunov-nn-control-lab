# Troubleshooting Guide

This guide lists common problems and quick fixes when running the Lyapunov Neural-Network Control Lab.

## `ModuleNotFoundError`

If Python cannot find the project or a runtime dependency, install the project:

```bash
python -m pip install -e .
```

## Tests fail after changing code

Run the local checks script:

```bash
python scripts/run_checks.py
```

If one test fails, read the first error message carefully and check the file mentioned in the traceback.

## Results are old or confusing

Create a new isolated run, then select it by run ID. Do not delete an older
completed run merely because a newer experiment is needed:

```bash
python main.py
python scripts/list_results.py
```

## No CSV summary appears

Use the report inside the selected run directory. Verify it with:

```bash
python scripts/verify_run.py results/runs/<run_id>
```

## Plots do not appear

Generated plots are saved in `results/runs/<run_id>/`. Open that directory from
the file explorer or run:

```bash
find results/runs/<run_id> -maxdepth 1 -type f
```

## Training takes a long time

The main experiment trains a neural-network controller and may also run robustness and grid-based experiments. This can take time depending on the machine.

For a quick check, run:

```bash
python examples/quick_start.py
```

## Numerical results changed slightly

Small numerical differences can happen because of solver tolerances, package versions, or hardware differences.

## Git branch confusion

Check your current branch and local changes:

```bash
git branch --show-current
git status
```

Before starting a new feature, return to `main` and pull the latest version:

```bash
git switch main
git pull origin main
```
