🌐 Language: [English](../en/methodology.md) | [日本語](../ja/methodology.md) | [한국어](../ko/methodology.md) | [ไทย](../th/methodology.md)

# Methodology

This document explains the main control-engineering ideas used in the Lyapunov neural-network control lab.

## 1. Mass-spring-damper system

The project studies a second-order mass-spring-damper system.

```text
x = [position, velocity]
```

The system is written in state-space form:

```text
dx/dt = A x + B u
```

Here, x is the state, u is the control input, A describes the plant dynamics, and B describes how the input affects the plant.

## 2. LQR baseline controller

The Linear Quadratic Regulator is used as the classical optimal-control baseline.

```text
u = -Kx
```

LQR gives a strong reference controller for the neural network to imitate.

## 3. Neural-network controller

The neural-network controller receives position and velocity as input and outputs one scalar control input.

```text
NN(x) ≈ LQR(x)
```

This is imitation learning: the neural network learns the behavior of the LQR controller over sampled states.

## 4. Lyapunov stability check

A Lyapunov function is an energy-like function used to reason about stability.

```text
V(x) = x^T P x
```

Along the closed-loop dynamics, the derivative is:

```text
V-dot(x) = 2 x^T P (A x + B pi(x))
```

The evaluator reports two distinct sampled conditions:

```text
basic decrease: V-dot(x) <= 0
decay margin:   V-dot(x) + alpha * ||x||^2 <= 0
```

The second condition is stronger when `alpha > 0`. The exact equilibrium is
excluded because `V(0) = V-dot(0) = 0`; no surrounding neighborhood is hidden.
A small default numerical tolerance of `1e-9` handles floating-point noise separately from
`alpha`. Grid results cover only the finite sampled region and are not a formal
continuous-state stability certificate.

## 5. Stability-aware training

The neural network is trained using both imitation loss and a Lyapunov stability penalty.

```text
total loss = imitation loss + stability penalty
```

With `alpha = 0.05`, training minimizes the positive part of the same decay
residual used by evaluation:

```text
decay residual = V-dot(x) + alpha * ||x||^2
stability penalty = mean(ReLU(decay residual))
```

## 6. Actuator saturation

Real actuators cannot apply unlimited force, so the project also tests saturated control.

```text
u = clip(u, -u_max, u_max)
```

This shows how actuator limits affect closed-loop stability and performance.

## 7. Robustness experiments

The project tests whether the learned controller remains effective under imperfect conditions.

The noise robustness experiment adds measurement noise:

```text
x_measured = x + noise
```

The parameter robustness experiment changes mass, damping, and stiffness to simulate modelling error.

## 8. Phase portrait and Lyapunov contours

The phase portrait plots position against velocity and shows whether trajectories move toward the origin.

The Lyapunov contour plot overlays trajectories on level sets of the Lyapunov function.

These plots visually explain closed-loop stability behavior.

## 9. Region of attraction analysis

The region of attraction experiment simulates many initial states and classifies each one as converged or not converged.

This answers the question:

```text
From which initial states can the controller stabilize the system?
```

The project also compares regions of attraction for LQR, neural-network control, and saturated neural-network control.

## 10. Stability-weight ablation study

The ablation study trains controllers with different Lyapunov penalty weights.

It reports the basic derivative violation fraction and the stronger decay-margin
violation fraction separately, together with final state norm, settling time,
quadratic cost, and control energy.

## 11. Summary

The project combines classical control, neural-network imitation learning, Lyapunov analysis, robustness testing, and empirical region-of-attraction estimation.

The main research question is:

```text
Can a neural-network controller imitate a stabilizing classical controller while being evaluated with Lyapunov-based stability tools?
```
