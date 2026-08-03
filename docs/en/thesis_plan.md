🌐 Language: [English](../en/thesis_plan.md) | [日本語](../ja/thesis_plan.md) | [한국어](../ko/thesis_plan.md) | [ไทย](../th/thesis_plan.md)

# Thesis Plan

## Tentative title

Lyapunov-Aware Neural-Network Control for a Mechanical Dynamical System

## Objective

Evaluate whether a neural controller trained from an LQR teacher can preserve useful closed-loop performance, sampled stability behavior, and robustness under selected nonideal conditions.

## Method

1. Derive the state-space plant and LQR baseline.
2. Train the neural controller with imitation and stability-aware losses.
3. Compare trajectories, costs, effort, and settling time.
4. Evaluate sampled Lyapunov behavior and estimated regions of attraction.
5. Test saturation, noise, and parameter variation.
6. Document limitations and reproducibility.

## Suggested chapters

1. Introduction and related work
2. System model and LQR design
3. Neural-controller training
4. Stability and robustness evaluation
5. Results and discussion
6. Limitations, conclusions, and future work

The current system is a simulation testbed; hardware validation and formal verification remain future extensions.
