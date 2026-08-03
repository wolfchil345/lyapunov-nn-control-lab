# Five Minute Demo Script

Use this script when presenting the project to a professor, reviewer, interviewer, or lab member.

## 0. Goal

Show that this repository is a reproducible research prototype for neural network control with Lyapunov-aware evaluation.

## 1. Opening, 30 seconds

This project studies a neural network controller for a mass-spring-damper system. The controller is trained to imitate an LQR controller, then evaluated using simulation metrics, Lyapunov analysis, robustness tests, and region-of-attraction style checks.

## 2. Repository tour, 60 seconds

- `README.md`: project overview and main usage.
- `src/`: core implementation for system dynamics, controllers, simulation, Lyapunov checks, metrics, robustness, and plotting.
- `tests/`: automated tests for important project behavior.
- `scripts/`: repeatable commands for checking, cleaning, summarizing, and running experiments.
- `docs/`: methodology, troubleshooting, reproducibility, review guides, and release process.
- `results/`: generated figures, metrics, and reports.

## 3. Run checks, 60 seconds

```bash
python scripts/check_environment.py
make checks
```

Explain that `make checks` runs the documentation link check, Python tests, and quick-start example.

## 4. Explain research idea, 90 seconds

The baseline controller is LQR, which provides a stable reference controller for the linear system. The neural network controller learns from this reference behavior. After training, the project checks whether the learned controller behaves well in closed-loop simulation and whether Lyapunov-related quantities look safe on a grid.

## 5. Show outputs, 60 seconds

Show generated plots and summary files from `results/`. Focus on trajectory behavior, control signal behavior, performance metrics, Lyapunov checks, robustness results, and region-of-attraction comparisons.

## 6. Closing, 30 seconds

The important point is not only that the neural network can imitate LQR, but that the repository includes reproducible checks, documentation, and safety-focused evaluation tools.

## Demo safety

Before a real demo, run:

```bash
python scripts/check_environment.py
make checks
git status
```

Only demo from a clean working tree.
