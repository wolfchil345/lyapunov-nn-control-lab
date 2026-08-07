# Model Card

This model card summarizes the neural-network controller used in the Lyapunov Neural-Network Control Lab.

## Model purpose

The neural-network controller maps the system state to a scalar control input.

It is trained to imitate an LQR controller while using a stability-aware training penalty.

## System state

The model input is a two-dimensional state:

- normalized position `q`
- normalized velocity `v = dq/dtau`

## Model output

The model output is one scalar control input:

- normalized scalar control input `u` applied to the model

## Training target

The training target is generated from the LQR controller.

The neural network learns to approximate the LQR state-to-control mapping.

## Stability-aware training

The training process can include a Lyapunov-style penalty.

This encourages behavior that reduces the Lyapunov function around sampled states.

## Intended use

This controller is intended for simulation-based control experiments, education, and research exploration.

It is useful for studying neural-network control, Lyapunov-style checks, robustness tests, and controller comparison.

## Out-of-scope use

This model should not be used as a safety-certified real-world controller.

It has not been verified for hardware deployment, dangerous systems, or safety-critical environments.

## Evaluation methods

The controller is evaluated using:

- closed-loop simulation
- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared normalized control effort
- maximum absolute normalized control input
- Lyapunov derivative grid checks
- robustness experiments
- finite-horizon final-state tolerance mapping

## Known limitations

- The plant model is simple.
- The controller may not generalize outside the training region.
- Grid-based Lyapunov checks do not prove global stability.
- Simulation results may vary slightly across environments.
- Robustness tests cover selected cases only.

## Recommended reporting

When reporting results, include:

- training settings
- random seed
- system parameters
- controller type
- evaluation metrics
- Lyapunov check results
- robustness settings
- finite-horizon convergence settings: horizon, tolerance, bounds, grid,
  tested count, and converged count

## Future improvements

- Add more controller architectures.
- Compare with KAN-based controllers.
- Add stronger formal verification.
- Learn neural Lyapunov functions directly.
- Test more nonlinear systems.
