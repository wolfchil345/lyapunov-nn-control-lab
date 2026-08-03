🌐 Language: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# Experiment Parameters

## Parameter groups

| Group | Examples | Main locations |
|---|---|---|
| Plant | mass, damping, stiffness | `src/system.py`, `src/parameter_variation.py` |
| Controller | `Q`, `R`, network size, saturation limit | `src/system.py`, `src/controllers.py`, `main.py` |
| Training | seed, epochs, learning rate, dataset size, loss weights | `src/controllers.py`, `main.py` |
| Simulation | initial state, duration, evaluation times | `src/simulation.py`, `main.py` |
| Stability | state range, grid density, decay margin | `src/lyapunov.py`, `main.py` |
| Robustness | noise, parameter cases, ablation weights | `src/noise.py`, `src/parameter_variation.py`, `src/stability_ablation.py` |

## Fair comparison

Change one parameter group at a time. Keep the seed, initial states, simulation horizon, and evaluation metrics fixed unless that change is the research question.

Record the exact settings in an [experiment log](experiment_log_template.md) before accepting new reference results.
