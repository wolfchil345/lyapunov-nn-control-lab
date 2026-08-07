🌐 Language: [English](../en/methodology.md) | [日本語](../ja/methodology.md) | [한국어](../ko/methodology.md) | [ไทย](../th/methodology.md)

# Methodology

This document explains the main control-engineering ideas used in the Lyapunov neural-network control lab.

## Coordinate convention

The repository uses a normalized, dimensionless second-order model. Normalized
time is `tau`, normalized position-like coordinate is `q`, normalized velocity
is `v = dq/dtau`, normalized control input is `u`, and `x = [q, v]`.
Therefore `||x||_2 = sqrt(q^2 + v^2)` and `||x||_2^2 = q^2 + v^2` are
Euclidean magnitudes in normalized state coordinates, not combinations of SI
position and velocity measurements.

## 1. Mass-spring-damper system

The project studies a second-order mass-spring-damper system.

```text
x = [q, v]
```

The system is written in state-space form:

```text
dx/dtau = A x + B u
```

Here, x is the state, u is the control input, A describes the plant dynamics, and B describes how the input affects the plant.

For the nominal parameters, `A` has eigenvalues `-0.2 + 1.4j` and
`-0.2 - 1.4j`. Both have negative real part, so the uncontrolled nominal
linear plant is already asymptotically stable. LQR changes the transient
response and control trade-off; this project studies imitation, performance,
robustness, and preservation of stable behavior rather than stabilization of
an open-loop unstable nominal plant.

## 2. LQR baseline controller

The Linear Quadratic Regulator is used as the classical optimal-control baseline.

```text
u = -Kx
```

`Q` and `R` are dimensionless objective weights. The resulting integral is a
quadratic LQR-style cost, not physical energy. LQR gives a strong reference
controller for the neural network to imitate.

## 3. Neural-network controller

The neural-network controller receives normalized `q` and `v` as input and outputs one normalized scalar control input.

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
decay margin:   V-dot(x) + alpha * ||x||_2^2 <= 0
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
decay residual = V-dot(x) + alpha * ||x||_2^2
stability penalty = mean(ReLU(decay residual))
```

## 6. Actuator saturation

The project also tests a limit on the normalized control input.

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

The same scalar Gaussian standard deviation is applied independently to `q`
and `v` in normalized coordinates.

The parameter robustness experiment changes normalized mass, damping, and
stiffness coefficients to simulate modelling error.

## 8. Phase portrait and Lyapunov contours

The phase portrait plots normalized position against normalized velocity and shows whether trajectories move toward the origin.

The Lyapunov contour plot overlays trajectories on level sets of the Lyapunov function.

These plots visually explain closed-loop stability behavior.

## 9. Finite-horizon convergence analysis

For every sampled initial state `x0`, the experiment simulates
`x(t; x0)` over `0 <= t <= T` and applies exactly this strict criterion:

```text
||x(T)||_2 < epsilon
```

The evaluator requires a successful simulation that reaches `T` with finite
time and state values. Failure or nonfinite output raises an error rather than
being silently classified as nonconverged.

`T` is normalized time and `epsilon` is a normalized-state Euclidean tolerance.
The result records the horizon `T`, tolerance `epsilon`, grid bounds and
resolution, number tested, number converged, and convergence fraction. It is
a sampled finite-horizon convergence map. A slowly converging state can fail
at `T` even when it converges as `t -> infinity`, so failure does not place
that state outside a mathematical attraction region.

For the equilibrium at the origin, a true region of attraction is
conceptually

```text
R = {x0 : x(t; x0) -> 0 as t -> infinity}.
```

Finite simulation does not verify this definition. Defensible estimation may
require invariant Lyapunov sublevel sets with verified decrease, applicable
sum-of-squares methods, reachability/invariance analysis, formal verification,
or analytic results for suitable linear systems. A plotted set
`{x : V(x) <= c}` is not automatically a certified attraction region.

The finite-horizon map and the separate sampled Lyapunov checks answer
different questions; neither is a formal continuous-state attraction-region
certificate.

## 10. Stability-weight ablation study

The ablation study trains controllers with different Lyapunov penalty weights.

It reports the basic derivative violation fraction and the stronger decay-margin
violation fraction separately, together with final normalized-state norm,
normalized settling time, quadratic LQR-style cost, and integrated squared
control effort. The latter is `integral u^2 dtau`, not physical energy.

## 11. Summary

The project combines classical control, neural-network imitation learning,
Lyapunov analysis, robustness testing, and sampled finite-horizon convergence
analysis.

The main research question is:

```text
Can a neural-network controller imitate an LQR reference while preserving useful transient, robustness, and sampled Lyapunov behavior?
```
