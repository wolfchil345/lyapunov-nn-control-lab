![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)

# Lyapunov NN Control Lab

A Python and PyTorch experiment that trains a neural-network controller to imitate an LQR controller and evaluates the closed-loop system using a quadratic Lyapunov function.

## Experiment summary

| Experiment | Purpose | Main output |
|---|---|---|
| LQR baseline | Creates a classical optimal-control reference controller | `results/position_comparison.png` |
| Neural-network controller | Trains a neural controller to imitate the LQR law | `results/training_loss.png` |
| Lyapunov grid check | Empirically checks whether V-dot is negative on sampled states | Printed terminal results |
| Stability-aware training | Adds a Lyapunov penalty during NN training | `results/training_loss.png` |
| Multiple initial conditions | Tests convergence from several starting states | `results/multiple_initial_conditions.png` |
| Quantitative metrics | Compares final norm, settling time, cost, energy, and max control | `results/performance_metrics.csv` |
| Actuator saturation | Tests controllers with limited control force | `results/saturation_comparison.png` |
| Noise robustness | Tests the controller under noisy state measurements | `results/noise_robustness.png` |
| Parameter robustness | Tests mass, damping, and stiffness variations | `results/parameter_robustness.png` |

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

## License

This project is released under the MIT License. See `LICENSE` for details.

## Quantitative performance evaluation

The experiment compares the LQR and neural-network controllers using:

- final state norm;
- settling time;
- quadratic control cost;
- control energy;
- maximum absolute control input.

The full results for all tested initial conditions are stored in [`results/performance_metrics.csv`](results/performance_metrics.csv).

## Stability-aware training

The neural controller is trained using a combined objective:

```text
total loss = imitation loss + lambda * Lyapunov penalty
```

The imitation term encourages the neural network to reproduce the LQR control law. The Lyapunov term penalizes sampled states that violate the desired decay condition:

```text
V-dot(x) <= -alpha * ||x||^2
```

This encourages stability-related behaviour during training. The sampled Lyapunov evaluation remains empirical and does not constitute formal verification over the full continuous state space.

## Actuator saturation comparison

The project also compares saturated and unsaturated controllers using a fixed actuator limit:

```text
u = clip(u, -u_max, u_max)
```

This models the fact that real actuators cannot apply unlimited control force.

The comparison includes:

- LQR;
- neural-network controller;
- saturated LQR;
- saturated neural-network controller.

The saturation comparison figure is stored in [`results/saturation_comparison.png`](results/saturation_comparison.png).

## Noise robustness experiment

The project evaluates the saturated neural-network controller under noisy state measurements:

```text
x_measured = x + noise
```

This simulates sensor noise, which is common in real control systems.

The experiment compares several Gaussian noise levels and checks whether the closed-loop state still converges toward the equilibrium.

The noise robustness figure is stored in [`results/noise_robustness.png`](results/noise_robustness.png).

## Parameter robustness experiment

The project tests whether the saturated neural-network controller remains stable when the plant parameters differ from the nominal model.

The tested variations include:

- increased and decreased mass;
- reduced damping;
- increased stiffness;
- combined parameter variation.

This evaluates robustness to modelling error, which is important because real mechanical systems rarely match their mathematical model exactly.

The parameter robustness figure is stored in [`results/parameter_robustness.png`](results/parameter_robustness.png).

## Phase portrait

The project includes a phase portrait of the neural-network controller.

The plot shows position on the horizontal axis and velocity on the vertical axis.

Multiple closed-loop trajectories are drawn from different initial conditions to show whether the controller drives the state toward the equilibrium at the origin.

The phase portrait figure is stored in [`results/phase_portrait.png`](results/phase_portrait.png).

## Lyapunov contour plot

The project visualizes Lyapunov level sets together with neural-network closed-loop trajectories.

The contour lines represent values of the quadratic Lyapunov function, while the trajectories show how the neural-network controller moves the system state toward the equilibrium.

The Lyapunov contour figure is stored in [`results/lyapunov_contours.png`](results/lyapunov_contours.png).
