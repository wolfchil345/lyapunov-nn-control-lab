# Figures Guide

This guide explains the generated figures in the `results/` directory.

## Main comparison plots

### `position_comparison.png`
Compares the position response of the LQR controller and the neural-network controller.

### `training_loss.png`
Shows the neural-network training loss over epochs.

### `multiple_initial_conditions.png`
Shows how the neural-network controller behaves from several different initial states.

## Stability and Lyapunov plots

### `phase_portrait.png`
Shows trajectories in the position-velocity state space.

### `lyapunov_contours.png`
Shows Lyapunov function contours together with closed-loop trajectories.

### `region_of_attraction.png`
Shows which initial states converge toward the target equilibrium.

### `region_of_attraction_comparison.png`
Compares the region of attraction for different controllers.

## Robustness plots

### `saturation_comparison.png`
Compares controller behavior when control input limits are applied.

### `noise_robustness.png`
Shows controller behavior under measurement noise.

### `parameter_robustness.png`
Shows how the controller behaves when physical system parameters are changed.

## Architecture and ablation plots

### `model_architecture.png`
Shows the project workflow from plant model to controller, simulation, stability checks, and reports.

### `stability_weight_ablation.png`
Shows how different stability penalty weights affect controller performance and stability metrics.

## Data files

### `performance_metrics.csv`
Stores numerical performance metrics for the controllers.

### `stability_weight_ablation.csv`
Stores numerical results from the stability-weight ablation experiment.

### `experiment_report.md`
Automatically summarizes the generated plots, metrics, and experiments.
