# Experiment Workflow

This guide explains the recommended workflow for running experiments in the Lyapunov Neural-Network Control Lab.

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Run a quick example

Use the quick-start script to confirm that the basic simulation works:

```bash
python examples/quick_start.py
```

## 3. Run local checks

Before running long experiments, check that tests and examples pass:

```bash
python scripts/run_checks.py
```

## 4. Clean old results

Clean old generated files if you want a fresh experiment run:

```bash
python scripts/clean_results.py
```

## 5. Run the main experiment

Run the full training, simulation, robustness, plotting, and reporting pipeline:

```bash
python main.py
```

## 6. Summarize numerical results

Print a quick terminal summary of CSV result files:

```bash
python scripts/summarize_results.py
```

## 7. Inspect generated outputs

Important outputs are saved in the `results/` directory.

Recommended files to check first:

- `performance_metrics.csv`
- `position_comparison.png`
- `phase_portrait.png`
- `lyapunov_contours.png`
- `region_of_attraction_comparison.png`
- `experiment_report.md`

## 8. Interpret the results

Use these guides:

- `docs/results_interpretation.md`
- `docs/figures.md`
- `docs/limitations.md`

## 9. Before committing changes

Run checks again before committing:

```bash
python scripts/run_checks.py
git status
```

## Recommended complete workflow

```bash
python scripts/run_checks.py
python scripts/clean_results.py
python main.py
python scripts/summarize_results.py
python scripts/run_checks.py
```
