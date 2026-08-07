# Artifact Manifest

This document explains the main files produced or used by the Lyapunov neural network control lab.

## Purpose

The project generates plots, reports, and summary files to evaluate neural network control performance, Lyapunov stability behavior, robustness, and reproducibility.

## Main source files

| Path | Purpose |
| --- | --- |
| `main.py` | Runs the main experiment pipeline. |
| `src/system.py` | Defines the mass-spring-damper system and LQR reference controller. |
| `src/controllers.py` | Defines neural network controllers, training data, and Lyapunov-aware training logic. |
| `src/simulation.py` | Simulates closed-loop system behavior. |
| `src/lyapunov.py` | Computes Lyapunov values and Lyapunov derivative grid checks. |
| `src/metrics.py` | Computes performance metrics such as state error, control effort, and cost. |
| `src/plotting.py` | Creates figures for trajectories, phase portraits, robustness, and stability analysis. |
| `src/lyapunov_nn_control_lab/finite_horizon_convergence.py` | Tests a strict final-state tolerance on a bounded grid at an explicit finite horizon and records the sampling metadata. |

## Main scripts

| Path | Purpose |
| --- | --- |
| `scripts/run_checks.py` | Runs documentation link checks, unit tests, and the quick start example. |
| `scripts/run_full_experiment.py` | Runs the non-destructive full experiment workflow. |
| `scripts/verify_run.py` | Verifies a completed manifest and its recorded SHA-256 checksums. |
| `scripts/summarize_results.py` | Summarizes generated experiment outputs. |
| `scripts/clean_results.py` | Removes generated result artifacts when a fresh run is needed. |
| `scripts/check_docs_links.py` | Checks internal documentation links. |

## Result artifacts

Historical files remain directly under `results/`. New outputs are isolated in
`results/runs/<run_id>/` and are never mixed across runs.

| Artifact type | Meaning |
| --- | --- |
| Trajectory plots | Compare system state responses under different controllers. |
| Control plots | Compare control input behavior and saturation effects. |
| Lyapunov plots | Visualize Lyapunov function behavior and derivative regions. |
| Finite-horizon convergence plots | Report sampled final-state tolerance results with explicit horizon, tolerance, bounds, grid, and counts; they are not attraction-region certificates. |
| Robustness plots | Show controller behavior under noise or parameter variation. |
| CSV summaries | Store numerical metrics for comparison and later reporting. |
| Experiment reports | Explain the main numerical and visual findings. |

## Reproducibility note

Before creating final thesis figures, run local checks and create an official
run from a clean Git state.

```bash
python scripts/run_checks.py
python main.py
python scripts/verify_run.py results/runs/<run_id>
```

`manifest.json` records schema version, Git provenance, runtime versions,
effective configuration, exact seeds, pairing methodology, inventory, sizes,
and hashes. See [`../results/README.md`](../results/README.md) for the
legacy-artifact policy.

## How to use this document

Use this manifest when explaining the repository structure in a thesis, presentation, or research meeting.
