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

For a stable closed-loop system, the Lyapunov value should decrease along trajectories.

```text
dV/dt < 0
```

The project checks this condition on a grid of sampled states.

## 5. Stability-aware training

The neural network is trained using both imitation loss and a Lyapunov stability penalty.

```text
total loss = imitation loss + stability penalty
```

The stability penalty discourages controller outputs that make the Lyapunov derivative positive.

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

It tests whether stronger stability-aware training improves metrics such as Lyapunov violation fraction, final state norm, settling time, quadratic cost, and control energy.

## 11. Summary

The project combines classical control, neural-network imitation learning, Lyapunov analysis, robustness testing, and empirical region-of-attraction estimation.

The main research question is:

```text
Can a neural-network controller imitate a stabilizing classical controller while being evaluated with Lyapunov-based stability tools?
```
