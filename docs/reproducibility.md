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
pip install -r requirements.txt
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
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png`
- `results/region_of_attraction_comparison.png`
- `results/stability_weight_ablation.png`
- `results/performance_metrics.csv`
- `results/stability_weight_ablation.csv`
- `results/experiment_report.md`

## 6. Open generated plots

In GitHub Codespaces or VS Code, open files from the `results/` folder.

Example:

```bash
code results/model_architecture.png
code results/experiment_report.md
```

## 7. Reproducibility notes

- Random seeds are set in the code to make results more stable across runs.
- Small numerical differences may still happen across operating systems, Python versions, or dependency versions.
- The project uses empirical simulation and grid-based Lyapunov checks, not a full formal proof for the neural-network controller.
- The generated plots are intended as practical stability and robustness diagnostics.

## 8. Recommended verification workflow

Before trusting a new experiment result, run:

```bash
python -m pytest
python main.py
python -m pytest
```

This checks that the code works before and after regenerating results.
