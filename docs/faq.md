# Frequently Asked Questions

This page answers common questions about the project.

## What is this project about?

This project trains and evaluates a neural network controller for a mass-spring-damper system. The controller learns from an LQR reference controller and is evaluated with simulation metrics, Lyapunov-style checks, robustness tests, and region-of-attraction style analysis.

## Why use LQR as the reference controller?

LQR is a standard control method for linear systems. It gives a stable and interpretable reference policy, which makes it useful for training and comparing a neural network controller.

## Does this project prove global stability?

No. The Lyapunov grid check is an empirical evaluation tool. It can provide useful evidence over sampled states, but it should not be described as a complete formal proof of global stability.

## What makes this project different from a normal machine learning demo?

The project does not only train a neural network. It also evaluates closed-loop behavior, control cost, robustness, Lyapunov-related quantities, reproducibility, and documentation quality.

## What should I show first in a presentation?

Start with the README, then show the five minute demo script, main experiment workflow, results plots, and Lyapunov or robustness documentation.

## How do I check that the project is working?

```bash
python scripts/check_environment.py
make checks
```

## Where are the main files?

- `src/`: source code.
- `tests/`: automated tests.
- `scripts/`: repeatable command scripts.
- `docs/`: explanations and guides.
- `results/`: generated outputs.

## What are the current limitations?

This is a research prototype. Results depend on the chosen system, controller settings, training setup, random seed, sampled grid, and experiment conditions.
