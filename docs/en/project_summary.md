🌐 Language: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# Project Summary

## Overview

This project is a Python research lab for neural-network control with Lyapunov-inspired stability analysis.

The target system is a mass-spring-damper plant. The project compares a classical LQR controller with a neural-network controller trained by imitation learning.

## Main goal

The main goal is to study whether a neural-network controller can imitate an
LQR reference while preserving useful transient, robustness, and sampled
Lyapunov behavior. The nominal uncontrolled linear plant is already
asymptotically stable; the controller changes its closed-loop performance.

## Nominal plant (canonical)

The canonical normalized plant parameters used across the repository are:

- MASS = 1.0
- DAMPING = 0.4
- STIFFNESS = 2.0

For these parameters the state matrix `A` has eigenvalues approximately
`-0.2 + 1.4j` and `-0.2 - 1.4j`, which have negative real parts. These values
are part of the canonical baseline and must be preserved verbatim in all
language variants of this file.

## Main features

- LQR baseline controller
- neural-network controller
- stability-aware training penalty
- Lyapunov grid check
- actuator saturation experiment
- measurement-noise robustness experiment
- parameter robustness experiment
- phase portrait visualization
- Lyapunov contour visualization
- finite-horizon convergence mapping with explicit sampling metadata
- controller comparison using an explicit finite-horizon final-state tolerance
- stability-weight ablation study
- automatic experiment report generation

## Key outputs

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png` (historical filename for the finite-horizon map)
- `results/region_of_attraction_comparison.png` (historical filename for the finite-horizon comparison)
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## Why this project matters

Neural-network controllers are powerful, but stability is a major concern in control engineering.

This project combines learning-based control with classical stability analysis ideas. It does not claim to provide a full formal proof for the neural-network controller, but it gives practical empirical tools for studying stability behavior.

## Portfolio value

This repository demonstrates skills in control engineering, Python, PyTorch, numerical simulation, testing, visualization, GitHub Actions, documentation, and reproducible research workflow.
