🌐 Language: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# Troubleshooting

## Imports or tests fail

Confirm that the terminal is at the repository root, activate `.venv`, run `python -m pip install -e ".[dev]"`, then use `python -m pytest`.

## Plots or CSV files look old

Check `git status` and back up tracked artifacts. Preview cleanup with `python scripts/clean_results.py`; after reviewing the list, use `python scripts/clean_results.py --yes` followed by `python main.py`.

## Numerical values differ slightly

Confirm the Python and dependency versions and the fixed seed. Small platform differences are possible; large differences require investigation.

## Training is slow

Use the quick start for setup checks. The full experiment includes training, robustness sweeps, and region-of-attraction simulations.

## Git branch confusion

Run `git status -sb` and `git branch --show-current`. Do not commit environment files or unrelated generated outputs.

For installation-specific problems, see [dependency troubleshooting](dependency_troubleshooting.md).
