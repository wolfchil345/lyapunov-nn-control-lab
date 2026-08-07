# Project Structure

This page explains the main files and folders in the Lyapunov Neural-Network Control Lab.

## Top-level files

### `main.py`
Runs the main experiment pipeline, including controller training, simulation, metrics, plots, robustness tests, and report generation.

### `requirements.txt`
Provides a thin compatibility wrapper for installing the development extra. `pyproject.toml` is the authoritative dependency source.

### `README.md`
Introduces the project, quick-start commands, results, and documentation links.

### `CITATION.cff`
Provides citation metadata for the project.

### `LICENSE`
Defines the license for using and sharing the project.

## Source code

### `src/lyapunov_nn_control_lab/system.py`
Defines normalized second-order model coefficients, state-space matrices, LQR controller, and Lyapunov matrix.

### `src/lyapunov_nn_control_lab/state_coordinates.py`
Defines the normalized coordinate convention and shared NumPy/Torch state-norm helpers.

### `src/lyapunov_nn_control_lab/controllers.py`
Defines the neural-network controller, dataset generation, stability-aware training, and actuator saturation utilities.

### `src/lyapunov_nn_control_lab/simulation.py`
Simulates closed-loop system trajectories.

### `src/lyapunov_nn_control_lab/lyapunov.py`
Computes Lyapunov values, Lyapunov derivatives, and grid-based stability checks.

### `src/lyapunov_nn_control_lab/metrics.py`
Computes normalized-state and normalized-time performance metrics, LQR-style cost, and integrated squared control effort.

### `src/lyapunov_nn_control_lab/plotting.py`
Creates plots for simulations, robustness experiments, Lyapunov contours,
finite-horizon convergence maps, and model architecture.

### `src/lyapunov_nn_control_lab/reporting.py`
Generates the automatic experiment report.

### `src/lyapunov_nn_control_lab/noise.py`
Runs measurement-noise robustness simulations.

### `src/lyapunov_nn_control_lab/parameter_variation.py`
Runs robustness simulations under changed normalized model coefficients.

### `src/lyapunov_nn_control_lab/finite_horizon_convergence.py`
Evaluates a strict final-state tolerance on a bounded grid at an explicit
finite horizon and returns the sampling metadata.

### `src/lyapunov_nn_control_lab/region_of_attraction.py`
Provides only the deprecated legacy API wrapper for the former misleading
name.

### `src/lyapunov_nn_control_lab/stability_ablation.py`
Runs experiments with different stability penalty weights.

## Tests

### `tests/`
Contains automated tests for the system model, controllers, simulations, metrics, plots, documentation-related outputs, and robustness utilities.

## Examples

### `examples/quick_start.py`
Provides a small beginner-friendly example for running an LQR simulation.

## Results

### `results/`
Stores generated plots, CSV files, trained model outputs, and the automatic experiment report.

## Documentation

### `docs/`
Contains guides for methodology, reproducibility, figures, glossary terms, references, and project summary.
