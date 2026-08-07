# Glossary

This glossary explains important terms used in the Lyapunov Neural-Network Control Lab.

## Control engineering terms

### State
The normalized, dimensionless coordinates `x = [q, v]`, where `q` is a
position-like coordinate and `v = dq/dtau` is velocity in normalized time.

### State norm
The Euclidean normalized-state magnitude
`||x||_2 = sqrt(q^2 + v^2)`. It is not a physical displacement or velocity.

### Control input
The normalized scalar input `u` applied to the model. No physical force unit is defined.

### Plant
The system being controlled. In this project, the plant is a mass-spring-damper system.

### Closed-loop system
A system where the controller uses feedback from the current state to choose the control input.

### LQR
Linear Quadratic Regulator. A classical optimal controller that minimizes a quadratic cost involving state error and control effort.

### Actuator saturation
A limit on the magnitude of the normalized control input.

## Stability terms

### Equilibrium
A state where the system can remain without changing. In this project, the target equilibrium is the origin.

### Lyapunov function
An energy-like function used to study stability. If it decreases along trajectories, the system is likely moving toward equilibrium.

### Lyapunov derivative
The rate of change of the Lyapunov function along the system trajectory.

### Region of attraction
For an equilibrium at the origin, the set
`R = {x0 : x(t; x0) -> 0 as t -> infinity}`. A finite simulation or a plot of
a Lyapunov sublevel set does not by itself certify this set.

### Finite-horizon convergence map
A sampled map that classifies an initial state when the strict final-state
criterion `||x(T)||_2 < epsilon` holds for a normalized-time horizon `T` and
normalized-state Euclidean tolerance `epsilon`. It depends on those settings and is not a region of
attraction.

### Integrated squared control effort
The integral of normalized `u^2` over normalized time. The historical field
name `control_energy` refers to the same number, but it is not physical energy.

## Machine-learning terms

### Neural-network controller
A controller represented by a neural network. It maps the system state to a control input.

### Imitation learning
Training a model to copy the behavior of another controller. In this project, the neural network imitates LQR.

### Stability-aware training
Training that includes a penalty related to Lyapunov stability, not only imitation accuracy.

### Ablation study
An experiment that changes or removes one design factor to study its effect. This project changes the stability penalty weight.
