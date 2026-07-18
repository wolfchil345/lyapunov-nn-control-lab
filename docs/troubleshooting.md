# Troubleshooting Guide

This guide lists common problems and quick fixes when running the Lyapunov Neural-Network Control Lab.

## `ModuleNotFoundError`

If Python cannot find a package, install the project requirements:

```bash
pip install -r requirements.txt
```

## Tests fail after changing code

Run the local checks script:

```bash
python scripts/run_checks.py
```

If one test fails, read the first error message carefully and check the file mentioned in the traceback.

## Results are old or confusing

Clean generated result files, then rerun the main experiment:

```bash
python scripts/clean_results.py
python main.py
```

## No CSV summary appears

The summary script needs generated CSV files. Run:

```bash
python main.py
python scripts/summarize_results.py
```

## Plots do not appear

Generated plots are saved in the `results/` directory. Open the PNG files from the file explorer or run:

```bash
ls results
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
