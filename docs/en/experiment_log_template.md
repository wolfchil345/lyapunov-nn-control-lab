🌐 Language: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# Experiment Log Template

## Identity

- Date:
- Branch and commit SHA:
- Research question:
- Purpose:

## Environment and settings

- Python and PyTorch versions:
- Runtime:
- Random seed:
- Epochs, learning rate, dataset size, network architecture:
- Plant, controller, simulation, Lyapunov, noise, and parameter settings:

## Commands and outputs

- Commands used:
- Metrics CSV:
- Report:
- Figures:

## Interpretation

- What improved or became worse?
- How did the controller compare with LQR?
- Were there sampled Lyapunov violations or robustness failures?
- Are the settings comparable with the previous run?

## Decision

- Keep as a reference result? Yes / No
- Include in a report or presentation? Yes / No
- Next experiment:

Create a timestamped copy with `python scripts/new_experiment_log.py "short description"`.
