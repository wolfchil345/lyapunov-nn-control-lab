# Research Questions

This document summarizes possible research questions for the Lyapunov Neural-Network Control Lab.

## Main research question

Can a neural-network controller imitate an LQR controller while maintaining useful Lyapunov-style stability behavior in closed-loop simulation?

## Controller performance

- How close is the neural-network controller performance to the LQR baseline?
- Does the neural-network controller reduce the final state norm reliably?
- How do settling time, quadratic cost, and control energy compare between controllers?

## Stability behavior

- Does the Lyapunov derivative remain mostly negative in the checked region?
- Which initial states produce stable convergence?
- How large is the estimated region of attraction?

## Robustness behavior

- How does measurement noise affect the neural-network controller?
- How does actuator saturation affect convergence?
- How sensitive is the controller to changes in mass, damping, and stiffness?

## Training design

- How does the stability penalty weight affect imitation accuracy?
- How does the stability penalty weight affect Lyapunov derivative violations?
- Is there a useful trade-off between imitation loss and stability-aware behavior?

## KAN extension questions

- Can a KAN controller imitate LQR as well as or better than a standard neural network?
- Does a KAN controller produce smoother or more interpretable control behavior?
- Does a KAN controller improve robustness or region-of-attraction results?

## Possible thesis direction

A possible graduation research direction is to compare standard neural-network controllers and KAN-based controllers using the same Lyapunov-style evaluation pipeline.

## Suggested evaluation summary

For each controller, report:

- performance metrics
- Lyapunov grid-check results
- robustness results
- region-of-attraction results
- limitations and failure cases
