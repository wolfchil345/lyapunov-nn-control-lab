🌐 Language: [English](../en/experiment_workflow.md) | [日本語](../ja/experiment_workflow.md) | [한국어](../ko/experiment_workflow.md) | [ไทย](../th/experiment_workflow.md)

# Experiment Workflow

## Safe sequence

1. Install the project and run `python scripts/check_environment.py`.
2. Run `python examples/quick_start.py` and `make checks`.
3. Record the branch, commit, seed, and intended parameter changes.
4. Back up tracked files in `results/` before any cleanup.
5. Run `python main.py` or `python scripts/run_full_experiment.py`.
6. Run `python scripts/summarize_results.py` and inspect every generated plot and CSV.
7. Compare metrics only when settings are compatible.
8. Run `make quality-gate` before committing.

## Expected outputs

The full pipeline produces controller comparisons, robustness plots, Lyapunov diagnostics, region-of-attraction estimates, two CSV files, `nn_controller.pt`, and an experiment report.

## Review rule

Do not treat low error, negative sampled `V_dot`, or grid convergence as a formal proof. Record failures and unexpected results instead of removing them.
