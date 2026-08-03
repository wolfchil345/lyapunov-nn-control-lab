# Result File Naming Guide

Use this guide to keep experiment outputs organized and easy to compare.

## Why naming matters

Experiment results become hard to compare when plots, metrics, and reports use unclear names. A consistent naming rule helps connect each output file to the settings that produced it.

## Recommended pattern

Use names that include the date, controller type, experiment type, and important setting.

```text
YYYYMMDD_controller_experiment_setting.ext
```

## Examples

```text
20260719_nn_trajectory_seed0.png
20260719_lqr_metrics_baseline.csv
20260719_nn_lyapunov_grid21.csv
20260719_nn_robustness_noise005.png
20260719_roa_comparison_grid31.png
20260719_experiment_report_seed0.md
```

## Suggested name parts

- Date: `YYYYMMDD`.
- Controller: `lqr`, `nn`, `kan`, or `comparison`.
- Experiment type: `trajectory`, `metrics`, `lyapunov`, `robustness`, `roa`, or `report`.
- Setting: seed, grid size, noise level, epoch count, or parameter variation.

## Good file names

- Clear.
- Lowercase.
- Uses underscores.
- Includes the most important setting.
- Does not contain spaces.

## Avoid

- `final.png`
- `new_result.csv`
- `test2.md`
- `really_final_plot.png`

## Comparison rule

When comparing two runs, make sure the file names show what changed between them.

## Documentation rule

If a result is important enough to keep, record it in the experiment log template.

## List current result files

Use the result inventory script before reports, demos, or release review:

```bash
python scripts/list_results.py
```

Or use the Makefile shortcut:

```bash
make list-results
```
