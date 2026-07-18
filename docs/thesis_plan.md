# Thesis Plan

This document connects the Lyapunov Neural-Network Control Lab to a possible graduation research plan.

## Tentative title

Lyapunov-style stability evaluation of neural-network controllers for a mass-spring-damper system

## Background

Neural-network controllers can approximate nonlinear control policies, but their stability behavior is difficult to guarantee.

Classical control methods such as LQR provide reliable baselines for linear systems.

This project studies a neural-network controller trained from an LQR teacher and evaluated with Lyapunov-style checks.

## Research objective

The objective is to evaluate whether a neural-network controller can imitate LQR while maintaining useful closed-loop stability behavior in simulation.

## Proposed method

1. Define a mass-spring-damper system.
2. Design an LQR controller as a baseline.
3. Generate training data from the LQR controller.
4. Train a neural-network controller.
5. Add a stability-aware training penalty.
6. Simulate closed-loop responses.
7. Evaluate performance, robustness, and Lyapunov-style stability behavior.

## Evaluation items

- final state norm
- settling time
- quadratic cost
- control energy
- maximum absolute control input
- Lyapunov derivative behavior
- robustness under noise
- robustness under parameter variation
- actuator saturation behavior
- estimated region of attraction

## Expected contribution

The expected contribution is a reproducible Python research workflow for comparing classical and neural-network controllers using performance metrics, robustness tests, and Lyapunov-style stability checks.

## Possible KAN extension

After the standard neural-network controller is working, the same pipeline can be extended to compare a KAN-based controller.

The comparison can investigate whether KAN improves imitation accuracy, smoothness, robustness, or region-of-attraction behavior.

## Risks and limitations

- The current plant is simple.
- Grid-based checks do not prove global stability.
- Neural-network behavior outside the training region may be unreliable.
- Simulation results are not the same as hardware validation.

## Possible final thesis structure

1. Introduction
2. Background on LQR, neural-network control, and Lyapunov stability
3. System model and baseline controller
4. Neural-network controller design
5. Stability-aware training method
6. Simulation experiments
7. Robustness and region-of-attraction analysis
8. Discussion and limitations
9. Conclusion and future work
