🌐 Language: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

[![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml)
[![Local checks](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/local-checks.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/local-checks.yml)
[![Quality gate](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml)
[![Release](https://img.shields.io/github/v/release/wolfchil345/lyapunov-nn-control-lab)](https://github.com/wolfchil345/lyapunov-nn-control-lab/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Lyapunov NN Control Lab

A reproducible Python and PyTorch control experiment that trains a neural-network controller to imitate an LQR controller, then evaluates closed-loop behavior with sampled Lyapunov analysis, robustness tests, and region-of-attraction estimates.

The project uses a mass-spring-damper system as an understandable testbed for the intersection of mechanical engineering, control theory, and machine learning.

## Highlights

- LQR baseline and neural-network imitation controller.
- Stability-aware training with a sampled Lyapunov penalty.
- Multiple initial-condition and quantitative performance evaluation.
- Actuator saturation, measurement-noise, and parameter-variation tests.
- Phase portraits, Lyapunov contours, and region-of-attraction comparisons.
- Reproducible scripts, automated tests, CI workflows, and generated reports.
- Documentation in English, Japanese, Korean, and Thai.

## Control loop

```text
state x = [position, velocity]
            │
            ▼
 neural-network controller ──► control force u
            ▲                         │
            │                         ▼
            └──── mass-spring-damper plant
```

The controller is constrained so that the origin remains an equilibrium: `u(0) = 0`.

## System and stability model

The plant is

```text
m q'' + c q' + k q = u
```

with state-space dynamics

```text
x_dot = A x + B u
```

The LQR controller supplies the imitation target `u = -Kx`. For the quadratic Lyapunov candidate `V(x) = x^T P x`, the project samples

```text
V_dot(x) = 2 x^T P (A x + B u)
```

and penalizes sampled violations of

```text
V_dot(x) <= -alpha * ||x||^2
```

These sampled checks provide empirical evidence only; they are not a formal proof over the continuous state space.

## Method

1. Define the nominal mass-spring-damper plant and design an LQR baseline.
2. Sample states and label them with the LQR control law.
3. Train a neural controller with imitation loss plus a Lyapunov penalty.
4. Simulate LQR, neural, and saturated controllers from several initial states.
5. Measure final state norm, settling time, quadratic cost, control energy, and maximum control input.
6. Evaluate sampled Lyapunov behavior, robustness, and estimated regions of attraction.
7. Save figures, CSV metrics, the trained model, and an experiment report.

## Experiments and outputs

| Experiment | Purpose | Output |
|---|---|---|
| Architecture | Explain the closed-loop neural control structure | `results/model_architecture.png` |
| Controller comparison | Compare LQR and neural trajectories | `results/position_comparison.png` |
| Stability-aware training | Track total, imitation, and Lyapunov losses | `results/training_loss.png` |
| Initial conditions | Check convergence from several states | `results/multiple_initial_conditions.png` |
| Actuator saturation | Evaluate limited control force | `results/saturation_comparison.png` |
| Noise robustness | Evaluate noisy state measurements | `results/noise_robustness.png` |
| Parameter robustness | Vary mass, damping, and stiffness | `results/parameter_robustness.png` |
| State-space analysis | Show phase trajectories and Lyapunov contours | `results/phase_portrait.png`, `results/lyapunov_contours.png` |
| Region of attraction | Compare convergence over initial-state grids | `results/region_of_attraction_comparison.png` |
| Stability ablation | Compare Lyapunov-penalty weights | `results/stability_weight_ablation.csv` |
| Automatic report | Summarize generated evidence | `results/experiment_report.md` |

Full numerical metrics are available in [`results/performance_metrics.csv`](results/performance_metrics.csv).

## Results snapshot

The tracked results were generated with the repository's fixed random seed and current experiment settings.

| Case | Final state norm | Settling time | Quadratic cost |
|---|---:|---:|---:|
| LQR, `x0 = [1.5, 0.0]` | `3.35e-06` | `3.37 s` | `14.6481` |
| Neural network, `x0 = [1.5, 0.0]` | `2.75e-07` | `3.25 s` | `14.6803` |
| Saturated neural network, `x0 = [1.5, 0.0]` | `2.73e-07` | `3.28 s` | `14.8506` |

The tracked stability-weight ablation reports a sampled Lyapunov violation fraction of `0.0` for every tested weight. Interpret these numbers together with the documented experiment region and limitations.

## Results gallery

| Architecture | Controller response |
|---|---|
| ![Closed-loop model architecture](results/model_architecture.png) | ![LQR and neural-network position comparison](results/position_comparison.png) |
| **Stability-aware training** | **Region-of-attraction comparison** |
| ![Training losses](results/training_loss.png) | ![Region-of-attraction controller comparison](results/region_of_attraction_comparison.png) |

All generated plots are listed in the [figures guide](docs/en/figures.md).

## Installation

Python 3.10 or newer is required. CPU execution is sufficient.

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Windows PowerShell, activate the environment with `.venv\Scripts\Activate.ps1`.

## Run and verify

Run a short example:

```bash
python examples/quick_start.py
```

Run the complete experiment:

```bash
python main.py
```

Run the standard checks or the full readiness gate:

```bash
make checks
make quality-gate
```

Useful commands are collected in the [command guide](docs/en/commands.md). `python scripts/clean_results.py` previews the known generated files; removal requires the explicit `--yes` flag. Review the [experiment workflow](docs/en/experiment_workflow.md) first.

## Project structure

```text
lyapunov-nn-control-lab/
├── main.py                 # Full experiment pipeline
├── src/                    # Dynamics, controllers, analysis, and plotting
├── tests/                  # Automated test suite
├── scripts/                # Checks and repeatable maintenance commands
├── examples/               # Minimal runnable example
├── docs/{en,ja,ko,th}/     # Localized documentation
└── results/                # Tracked reference outputs and generated model
```

See the [project structure guide](docs/en/project_structure.md) for details.

## Scientific limitations

- The plant is a simulated linear mass-spring-damper system, not hardware.
- The neural controller is trained from an LQR teacher and may not generalize outside the sampled region.
- Lyapunov and region-of-attraction evaluations use finite grids and simulations.
- Robustness experiments cover selected noise levels, actuator limits, and parameter variations.
- Small numerical differences may occur across dependency versions or platforms.

See [limitations](docs/en/limitations.md), [results interpretation](docs/en/results_interpretation.md), and [reproducibility](docs/en/reproducibility.md) before drawing research conclusions.

## Documentation

The complete documentation index is available in four languages:

- [English documentation](docs/en/index.md)
- [日本語ドキュメント](docs/ja/index.md)
- [한국어 문서](docs/ko/index.md)
- [เอกสารภาษาไทย](docs/th/index.md)

Key references include the [methodology](docs/en/methodology.md), [experiment workflow](docs/en/experiment_workflow.md), [model card](docs/en/model_card.md), and [research questions](docs/en/research_questions.md).

## Community and project information

- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Roadmap](ROADMAP.md)
- [Release notes](RELEASE_NOTES.md)
- [Citation metadata](CITATION.cff)

## License and author

Released under the [MIT License](LICENSE).

Created by Sirichet Sriamontham, a mechanical-engineering student interested in control engineering, neural networks, and stability analysis.
