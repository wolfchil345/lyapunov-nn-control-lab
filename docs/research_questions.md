# Research Questions

This document summarizes possible research questions for the Lyapunov Neural-Network Control Lab.

## Main research question

Can a neural-network controller imitate an LQR controller while maintaining useful Lyapunov-style stability behavior in closed-loop simulation?

## Controller performance

- How close is the neural-network controller performance to the LQR baseline?
- Does the neural-network controller reduce the final normalized-state norm reliably?
- How do normalized settling time, quadratic LQR-style cost, and integrated squared control effort compare between controllers?

## Stability behavior

- Does the Lyapunov derivative remain mostly negative in the checked region?
- Which sampled initial states meet a stated final-state tolerance after a
  stated finite horizon?
- How sensitive is that finite-horizon percentage to the horizon, tolerance,
  bounds, and grid resolution?

## Robustness behavior

- How does measurement noise affect the neural-network controller?
- How does actuator saturation affect convergence?
- How sensitive is the controller to changes in normalized mass, damping, and stiffness coefficients?

## Training design

- How does the stability penalty weight affect imitation accuracy?
- How does the stability penalty weight affect Lyapunov derivative violations?
- Is there a useful trade-off between imitation loss and stability-aware behavior?

## KAN extension questions

- Can a KAN controller imitate LQR as well as or better than a standard neural network?
- Does a KAN controller produce smoother or more interpretable control behavior?
- Does a KAN controller improve robustness or finite-horizon convergence
  results under identical sampling settings?

## Possible thesis direction

A possible graduation research direction is to compare standard neural-network controllers and KAN-based controllers using the same Lyapunov-style evaluation pipeline.

## Suggested evaluation summary

For each controller, report:

- performance metrics
- Lyapunov grid-check results
- robustness results
- finite-horizon convergence counts, percentages, and sampling metadata
- limitations and failure cases
