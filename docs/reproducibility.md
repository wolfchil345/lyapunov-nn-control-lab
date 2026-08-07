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

This publishes an isolated run under `results/runs/<run_id>/` only after its
artifacts have been generated, hashed, manifested, and verified.

Important run-local outputs include:

- `manifest.json`
- `SHA256SUMS`
- `report.md`
- `model_architecture.png`
- `performance_metrics.csv`
- paired raw and aggregate ablation/noise CSV files
- normalized-coordinate figures
- `nn_controller.pt`

## 6. Open generated plots

In GitHub Codespaces or VS Code, open files from one selected run directory.

Example:

```bash
code results/runs/<run_id>/model_architecture.png
code results/runs/<run_id>/report.md
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
- Official runs require a clean Git tree. `--allow-dirty` creates an explicitly
  exploratory run whose manifest records `git_dirty: true`.
- `configuration_sha256` hashes canonical sorted scientific configuration JSON;
  timestamps and platform metadata do not affect configuration identity.
- Verify a run with `python scripts/verify_run.py results/runs/<run_id>`.

## 8. Recommended verification workflow

Before trusting a new experiment result, run:

```bash
python -m pytest
python main.py
python scripts/verify_run.py results/runs/<run_id>
python -m pytest
```

This checks the code before generation and validates the exact published files.
