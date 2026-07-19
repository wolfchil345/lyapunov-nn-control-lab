# Experiment Parameters Guide

This guide explains the main parameters that affect experiment behavior and results.

## Why parameters matter

Neural network control experiments can change when training settings, random seeds, grid ranges, system constants, or robustness settings are changed. Record important parameter changes before comparing results.

## Main parameter groups

## 1. System parameters

These define the mass-spring-damper model, such as mass, damping, stiffness, and state-space matrices.

Important files:

- `src/system.py`
- `src/parameter_variation.py`

## 2. Controller parameters

These affect the LQR reference controller, neural network controller, saturation behavior, and learned control output.

Important files:

- `src/system.py`
- `src/controllers.py`
- `main.py`

## 3. Training parameters

These affect neural network learning.

Examples:

- Random seed.
- Number of epochs.
- Learning rate.
- Dataset size.
- Loss weights.
- Network hidden size.

Important files:

- `src/controllers.py`
- `main.py`

## 4. Simulation parameters

These affect closed-loop evaluation.

Examples:

- Initial condition.
- Simulation time.
- Time step.
- Controller saturation limit.

Important files:

- `src/simulation.py`
- `main.py`

## 5. Lyapunov grid parameters

These affect sampled Lyapunov-style checks.

Examples:

- State range.
- Grid density.
- Controller used during grid evaluation.

Important files:

- `src/lyapunov.py`
- `main.py`

## 6. Robustness parameters

These affect noise and model variation experiments.

Examples:

- Noise level.
- Parameter variation range.
- Number of tested cases.

Important files:

- `src/noise.py`
- `src/parameter_variation.py`
- `src/stability_ablation.py`

## Safe comparison rule

When comparing two experiment results, change only one parameter group at a time when possible.

## Before saving final results

Run:

```bash
python scripts/check_environment.py
make checks
python main.py
python scripts/summarize_results.py
```

Then record what parameters were changed and why.
