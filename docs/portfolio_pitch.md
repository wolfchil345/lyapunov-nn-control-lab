# Portfolio Pitch

Use this page when explaining the project in a CV, interview, professor meeting, research discussion, or graduate school application.

## One sentence summary

A reproducible Python research prototype that trains and evaluates a neural network controller for a mass-spring-damper system using LQR imitation, Lyapunov-aware analysis, robustness tests, and region-of-attraction style checks.

## 30 second pitch

This project studies whether a neural network controller can imitate an LQR controller while still being evaluated with control-oriented safety tools. The repository includes simulation, metrics, Lyapunov grid checks, robustness experiments, region-of-attraction style analysis, automated tests, and reproducible documentation.

## Technical keywords

- Neural network control
- LQR imitation
- Lyapunov analysis
- Closed-loop simulation
- Robustness evaluation
- Region of attraction
- Reproducible research code
- Python and PyTorch

## What makes the project strong

- It connects machine learning with control engineering.
- It includes automated tests and local checks.
- It documents methodology, limitations, reproducibility, and troubleshooting.
- It separates source code, scripts, tests, documentation, and results.
- It treats stability and robustness as evaluation topics, not afterthoughts.

## What to show first

1. README overview.
2. Five minute demo script.
3. Main experiment workflow.
4. Results plots and summary report.
5. Lyapunov and robustness documentation.

## Interview talking points

- Why LQR is used as a reference controller.
- How the neural network controller is trained.
- Why Lyapunov-style evaluation is useful.
- How robustness tests make the evaluation more realistic.
- Why reproducibility matters for research code.

## Honest limitation statement

This project is a research prototype. The Lyapunov grid check is an empirical evaluation tool and should not be described as a complete formal proof of global stability.
