# KAN Extension Guide

This guide explains how the current Lyapunov Neural-Network Control Lab could be extended toward Kolmogorov-Arnold Network controller experiments.

## Motivation

The current project uses a standard neural-network controller to imitate LQR and evaluate stability-related behavior.

A KAN-based controller could be tested as an alternative function approximator for mapping system state to control input.

## Current controller pipeline

The current workflow is:

1. Define the mass-spring-damper system.
2. Generate training data from the LQR controller.
3. Train a neural-network controller.
4. Simulate closed-loop behavior.
5. Compute performance metrics.
6. Check Lyapunov-style stability behavior.
7. Run robustness and region-of-attraction experiments.

## KAN controller idea

A KAN controller would replace the standard neural-network model with a KAN-style model.

The input would still be the system state:

- position
- velocity

The output would still be the control input:

- scalar force

## Files that may need changes

### `src/controllers.py`
Add a KAN controller class or wrapper function.

### `main.py`
Add KAN training, simulation, metrics, and plotting alongside LQR and the current neural-network controller.

### `src/plotting.py`
Add plots comparing LQR, standard neural network, and KAN.

### `tests/`
Add tests to check that the KAN controller returns valid scalar controls and can run in simulation.

## Suggested experiment design

Compare three controllers:

- LQR baseline
- standard neural-network controller
- KAN controller

Use the same initial states, metrics, and Lyapunov checks for all controllers.

## Suggested metrics

- final state norm
- settling time
- quadratic cost
- control energy
- maximum absolute control input
- Lyapunov derivative violation fraction
- region-of-attraction convergence rate

## Suggested plots

- position comparison
- control input comparison
- phase portrait comparison
- Lyapunov contour comparison
- region-of-attraction comparison
- robustness comparison under noise and parameter variation

## Research questions

- Does the KAN controller imitate LQR better than the standard neural network?
- Does the KAN controller produce smoother control inputs?
- Does the KAN controller improve Lyapunov derivative behavior?
- Does the KAN controller increase the estimated region of attraction?
- Does the KAN controller remain robust under noise, saturation, and parameter changes?

## Important caution

Replacing the model architecture does not automatically guarantee stability.

KAN results should still be checked with simulations, Lyapunov-style grid checks, robustness experiments, and region-of-attraction analysis.
