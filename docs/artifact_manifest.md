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

## Main scripts

| Path | Purpose |
| --- | --- |
| `scripts/run_checks.py` | Runs documentation link checks, unit tests, and the quick start example. |
| `scripts/run_full_experiment.py` | Runs the full experiment workflow. |
| `scripts/summarize_results.py` | Summarizes generated experiment outputs. |
| `scripts/clean_results.py` | Removes generated result artifacts when a fresh run is needed. |
| `scripts/check_docs_links.py` | Checks internal documentation links. |

## Result artifacts

Generated result files are usually stored in `results/`.

| Artifact type | Meaning |
| --- | --- |
| Trajectory plots | Compare system state responses under different controllers. |
| Control plots | Compare control input behavior and saturation effects. |
| Lyapunov plots | Visualize Lyapunov function behavior and derivative regions. |
| Robustness plots | Show controller behavior under noise or parameter variation. |
| CSV summaries | Store numerical metrics for comparison and later reporting. |
| Experiment reports | Explain the main numerical and visual findings. |

## Reproducibility note

Before creating final thesis figures, run local checks and regenerate results from a clean state when possible.

```bash
python scripts/run_checks.py
python scripts/clean_results.py
python main.py
```

## How to use this document

Use this manifest when explaining the repository structure in a thesis, presentation, or research meeting.
