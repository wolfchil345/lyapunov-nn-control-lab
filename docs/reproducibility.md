# Reproducibility Guide

This guide explains how to reproduce the main results of the Lyapunov Neural-Network Control Lab.

## 1. Clone the repository

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
```

## 2. Create a Python environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```bash
python -m pip install -e ".[dev]"
```

## 4. Run tests

```bash
python -m pytest
```

All tests should pass before regenerating results.

## 5. Regenerate experiment results

```bash
python main.py
```

This regenerates the main plots, CSV files, trained controller file, and automatic experiment report.

Important outputs include:

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness_paired.png`
- `results/noise_robustness_trials_paired.csv`
- `results/noise_robustness_summary_paired.csv`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/finite_horizon_convergence.png`
- `results/finite_horizon_convergence_comparison.png`
- `results/stability_weight_ablation_paired.png`
- `results/performance_metrics.csv`
- `results/stability_weight_ablation_trials_paired.csv`
- `results/stability_weight_ablation_summary_paired.csv`
- `results/experiment_report.md`

## 6. Open generated plots

In GitHub Codespaces or VS Code, open files from the `results/` folder.

Example:

```bash
code results/model_architecture.png
code results/experiment_report.md
```

## 7. Reproducibility notes

- Python, NumPy, PyTorch CPU, and available PyTorch CUDA generators are seeded
  through one project utility. Fixed seeds support repeatable CPU comparisons
  in the same environment; they are not a universal guarantee of bitwise
  deterministic CUDA or cross-platform execution.
- Stability weights are compared with paired seeds across all weights. Raw
  per-seed trials are kept separate from aggregate means, sample standard
  deviations, and standard errors.
- Measurement-noise amplitudes use common random-number realizations: the same
  standardized sequence for a seed is scaled by each amplitude. Repeated
  matched seeds reduce noise-realization confounding but do not eliminate all
  experimental uncertainty.
- Small numerical differences may still happen across operating systems, Python versions, or dependency versions.
- The project uses empirical simulation and grid-based Lyapunov checks, not a full formal proof for the neural-network controller.
- The generated plots are intended as practical stability and robustness diagnostics.
- The finite-horizon convergence figures apply only the strict criterion
  `||x(T)||_2 < epsilon` on the stated normalized-coordinate grid. They are not mathematical
  attraction-region certificates.
- The tracked files whose names begin with `region_of_attraction` are
  historical pre-migration artifacts and are intentionally not regenerated in
  this terminology-only operation.

## 8. Recommended verification workflow

Before trusting a new experiment result, run:

```bash
python -m pytest
python main.py
python -m pytest
```

This checks that the code works before and after regenerating results.
