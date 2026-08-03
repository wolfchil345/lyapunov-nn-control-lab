🌐 Language: [English](../en/faq.md) | [日本語](../ja/faq.md) | [한국어](../ko/faq.md) | [ไทย](../th/faq.md)

# Frequently Asked Questions

## What is the project about?

It trains a neural controller to imitate LQR on a mass-spring-damper system and evaluates performance, sampled Lyapunov behavior, and robustness.

## Why use LQR as the teacher?

LQR is transparent, reproducible, and stabilizing for the nominal linear plant, which makes it a useful baseline and source of labels.

## Does the project prove stability?

No. It provides simulation and finite-grid evidence with a quadratic Lyapunov candidate. Formal continuous-domain verification is outside the current scope.

## What makes it more than a machine-learning demo?

It evaluates closed-loop trajectories, control effort, cost, saturation, noise, model variation, Lyapunov behavior, and estimated regions of attraction with reproducible software checks.

## How do I verify it?

Run `python examples/quick_start.py`, `make checks`, and `make quality-gate`. Use `python main.py` for the complete experiment.

## Where should I start reading?

Read the [project summary](project_summary.md), [methodology](methodology.md), [experiment workflow](experiment_workflow.md), and [limitations](limitations.md).
