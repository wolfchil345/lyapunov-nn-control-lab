# Project Structure

This page explains the main files and folders in the Lyapunov Neural-Network Control Lab.

## Top-level files

### `main.py`
Runs the main experiment pipeline, including controller training, simulation, metrics, plots, robustness tests, and report generation.

### `requirements.txt`
Lists the Python packages needed to run the project.

### `README.md`
Introduces the project, quick-start commands, results, and documentation links.

### `CITATION.cff`
Provides citation metadata for the project.

### `LICENSE`
Defines the license for using and sharing the project.

## Source code

### `src/system.py`
Defines the mass-spring-damper system, state-space matrices, LQR controller, and Lyapunov matrix.

### `src/controllers.py`
Defines the neural-network controller, dataset generation, stability-aware training, and actuator saturation utilities.

### `src/simulation.py`
Simulates closed-loop system trajectories.

### `src/lyapunov.py`
Computes Lyapunov values, Lyapunov derivatives, and grid-based stability checks.

### `src/metrics.py`
Computes performance metrics such as final state norm, settling time, cost, and control energy.

### `src/plotting.py`
Creates plots for simulations, robustness experiments, Lyapunov contours, region of attraction, and model architecture.

### `src/reporting.py`
Generates the automatic experiment report.

### `src/noise.py`
Runs measurement-noise robustness simulations.

### `src/parameter_variation.py`
Runs robustness simulations under changed physical parameters.

### `src/region_of_attraction.py`
Evaluates convergence over a grid of initial states.

### `src/stability_ablation.py`
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
