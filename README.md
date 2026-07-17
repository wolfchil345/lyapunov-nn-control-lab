# Lyapunov NN Control Lab

A Python and PyTorch experiment that trains a neural-network controller to imitate an LQR controller and evaluates the closed-loop system using a quadratic Lyapunov function.

## Project overview

This project combines:

- mechanical system modelling;
- linear quadratic regulator control;
- neural-network controller training;
- closed-loop simulation;
- sampled Lyapunov stability analysis.

The first controlled system is a mass-spring-damper model.

## System model

The physical system is:

```text
m q'' + c q' + k q = u
```

The state vector is:

```text
x = [position, velocity]
```

The state-space model is:

```text
x_dot = A x + B u
```

## Method

1. Define the mass-spring-damper system.
2. design an LQR baseline controller.
3. Generate state and control training data from the LQR controller.
4. Train a neural network to imitate the LQR control law.
5. Simulate the LQR and neural-network controllers.
6. Evaluate the Lyapunov derivative over a sampled state-space grid.

## Results

### Closed-loop position comparison

![LQR and neural-network position comparison](results/position_comparison.png)

The neural-network controller produces a response close to the LQR baseline and drives the position toward the equilibrium.

### Neural-network training loss

![Neural-network training loss](results/training_loss.png)

The decreasing mean-squared error indicates that the neural network progressively learns the LQR control law.

## Lyapunov grid check

| Controller | Maximum V-dot | Violation fraction |
|---|---:|---:|
| LQR | -0.0221 | 0.0 |
| Neural network | -0.0192 | 0.0 |

All tested nonzero grid points produced a negative Lyapunov derivative.

This is empirical evidence within the sampled region. It is not a formal stability proof over the entire continuous state space.

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the experiment

```bash
python main.py
```

The program trains the controller and creates:

```text
results/
├── nn_controller.pt
├── position_comparison.png
└── training_loss.png
```

The trained model file is ignored by Git, while the two result figures are included in the repository.

## Current limitations

- The neural network imitates an existing LQR controller.
- Stability is evaluated on a finite grid.
- Only one initial condition is shown in the main comparison.
- The plant currently has no actuator saturation, measurement noise, or parameter uncertainty.

## Future work

- Add a Lyapunov penalty to the training loss.
- Compare LQR, PID, and neural controllers.
- Test multiple initial conditions.
- Add actuator saturation and measurement noise.
- Study robustness to changes in mass, damping, and stiffness.
- Extend the project to an inverted pendulum.
- Investigate formal neural-network verification.

## Technologies

- Python
- PyTorch
- NumPy
- SciPy
- Matplotlib
- Python Control Systems Library

## Author

Sirichet Sriamontham  
Mechanical Engineering student interested in control engineering, neural networks, and stability analysis.
