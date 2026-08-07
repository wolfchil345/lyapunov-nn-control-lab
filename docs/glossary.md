# Glossary

This glossary explains important terms used in the Lyapunov Neural-Network Control Lab.

## Control engineering terms

### State
The variables that describe the current condition of the system. In this project, the state is position and velocity.

### Control input
The input applied to the plant. For the mass-spring-damper system, this is a scalar force.

### Plant
The system being controlled. In this project, the plant is a mass-spring-damper system.

### Closed-loop system
A system where the controller uses feedback from the current state to choose the control input.

### LQR
Linear Quadratic Regulator. A classical optimal controller that minimizes a quadratic cost involving state error and control effort.

### Actuator saturation
A limit on how large the control input can be. Real actuators cannot apply infinite force.

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
criterion `||x(T)|| < epsilon` holds for an explicit finite horizon `T` and
tolerance `epsilon`. It depends on those settings and is not a region of
attraction.

## Machine-learning terms

### Neural-network controller
A controller represented by a neural network. It maps the system state to a control input.

### Imitation learning
Training a model to copy the behavior of another controller. In this project, the neural network imitates LQR.

### Stability-aware training
Training that includes a penalty related to Lyapunov stability, not only imitation accuracy.

### Ablation study
An experiment that changes or removes one design factor to study its effect. This project changes the stability penalty weight.
