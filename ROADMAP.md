# Roadmap

This roadmap lists possible future improvements for the Lyapunov Neural-Network Control Lab.

## Near-term improvements

- Add multiple random-seed experiments for neural-network training.
- Save averaged metrics across repeated training runs.
- Add confidence intervals for performance and stability metrics.
- Add a command-line interface for selecting experiments.
- Split heavy experiments into separate scripts for faster development.

## Control-engineering extensions

- Compare the neural-network controller with PID control.
- Add nonlinear plant dynamics.
- Add external disturbance rejection experiments.
- Add model-predictive control as another baseline.
- Test larger regions of attraction.

## Stability-analysis extensions

- Study alternative Lyapunov candidate functions.
- Add neural-network Lyapunov function learning.
- Compare empirical Lyapunov checks with formal verification tools.
- Add denser grid checks and adaptive sampling near unstable regions.

## Machine-learning extensions

- Compare different neural-network architectures.
- Test different activation functions.
- Add KAN-based controller experiments.
- Add regularization experiments.
- Study generalization outside the training state range.

## Documentation and portfolio improvements

- Add a short technical blog-style explanation.
- Add a poster-style project summary.
- Add diagrams explaining Lyapunov decrease and region of attraction.
- Add links to related papers and textbooks.

## Long-term research direction

The long-term goal is to build a compact experimental platform for studying learning-based control with stability-aware evaluation.
