# Roadmap

This roadmap lists possible future improvements for the Lyapunov Neural-Network Control Lab.

## Near-term improvements

- Extend paired multi-seed experiments to additional learned-controller studies.
- Evaluate justified confidence-interval methods for larger repeat counts.
- Add a command-line interface for selecting experiments.
- Split heavy experiments into separate scripts for faster development.

## Control-engineering extensions

- Compare the neural-network controller with PID control.
- Add nonlinear plant dynamics.
- Add external disturbance rejection experiments.
- Add model-predictive control as another baseline.
- Test finite-horizon convergence on broader documented grids and study its
  sensitivity to horizon and tolerance.

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
- Add diagrams distinguishing sampled finite-horizon convergence, sampled
  Lyapunov decrease, and a mathematically certified region of attraction.
- Investigate defensible attraction-region methods such as invariant Lyapunov
  sublevel sets, reachability/invariance analysis, or formal verification.
- Add links to related papers and textbooks.

## Long-term research direction

The long-term goal is to build a compact experimental platform for studying learning-based control with stability-aware evaluation.
