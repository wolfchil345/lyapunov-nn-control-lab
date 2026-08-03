🌐 Language: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# Project Summary

## Purpose

Lyapunov NN Control Lab is a reproducible research and portfolio project connecting mechanical systems, classical control, neural networks, and stability analysis.

## Approach

The project models a mass-spring-damper plant, designs an LQR baseline, and trains a neural controller to imitate the LQR state-feedback law. Training also includes a sampled Lyapunov penalty. Evaluation covers multiple initial states, quantitative metrics, actuator saturation, measurement noise, plant-parameter variation, sampled Lyapunov behavior, and estimated regions of attraction.

## Evidence

- Automated tests, quick-start example, CI, and quality gate.
- Tracked figures, CSV metrics, and generated experiment reports.
- Fixed random seeds and a documented reproduction workflow.
- Honest separation between empirical sampled evidence and formal proof.

## Current result

Within the tracked test settings, the neural controller closely follows the LQR baseline, converges from the selected initial states, and reports zero sampled Lyapunov violations. These results are limited to the documented model, regions, thresholds, and uncertainty scenarios.

## Portfolio value

The repository demonstrates system modeling, optimal control, PyTorch training, numerical simulation, scientific evaluation, software testing, GitHub workflows, release management, and multilingual technical communication.
