import argparse
import csv
from pathlib import Path
from typing import Any

import numpy as np
import torch

from lyapunov_nn_control_lab.controllers import (
    ZeroAtOriginController,
    make_nn_controller,
    make_saturated_controller,
    train_controller,
)
from lyapunov_nn_control_lab.finite_horizon_convergence import (
    evaluate_finite_horizon_convergence,
)
from lyapunov_nn_control_lab.experimental_seeds import (
    ExperimentSeedPlan,
    seed_random_generators,
)
from lyapunov_nn_control_lab.lyapunov import (
    DEFAULT_DECAY_MARGIN,
    DEFAULT_NUMERICAL_TOLERANCE,
    grid_check,
)
from lyapunov_nn_control_lab.metrics import calculate_metrics
from lyapunov_nn_control_lab.noise import (
    NOISE_PAIRING_STRATEGY,
    aggregate_noise_results,
    run_measurement_noise_trials,
    save_noise_aggregate_csv,
    save_noise_trial_results_csv,
)
from lyapunov_nn_control_lab.parameter_variation import simulate_parameter_variation
from lyapunov_nn_control_lab.plotting import (
    save_finite_horizon_convergence_comparison_plot,
    save_finite_horizon_convergence_plot,
    save_lyapunov_contour_plot,
    save_model_architecture_diagram,
    save_multiple_initial_conditions_plot,
    save_noise_robustness_plot,
    save_noise_robustness_statistics_plot,
    save_parameter_robustness_plot,
    save_phase_portrait_plot,
    save_plots,
    save_saturation_comparison_plot,
    save_stability_weight_ablation_plot,
)
from lyapunov_nn_control_lab.stability_ablation import (
    ABLATION_PAIRING_STRATEGY,
    aggregate_ablation_results,
    run_stability_weight_ablation,
    save_ablation_aggregate_csv,
    save_ablation_results_csv,
)
from lyapunov_nn_control_lab.reporting import generate_experiment_report
from lyapunov_nn_control_lab.result_provenance import RunContext, publish_run
from lyapunov_nn_control_lab.simulation import simulate
from lyapunov_nn_control_lab.state_coordinates import (
    NORMALIZED_STATE_CONVENTION,
    state_norm,
)
from lyapunov_nn_control_lab.system import (
    A,
    B,
    CLOSED_LOOP_EIGENVALUES,
    DAMPING,
    K,
    MASS,
    P,
    Q,
    R,
    STIFFNESS,
    lqr_controller,
)

SEED = 7
CONTROL_LIMIT = 2.0
DECAY_MARGIN = DEFAULT_DECAY_MARGIN
TRAINING_EPOCHS = 1000
TRAINING_STABILITY_WEIGHT = 10.0
INITIAL_STATES = (
    (1.5, 0.0),
    (-1.5, 0.0),
    (1.0, 1.5),
    (-1.0, -1.5),
    (0.5, -2.0),
)
CONVERGENCE_BOUNDS = (-2.5, 2.5)
CONVERGENCE_TOLERANCE = 0.1
CONVERGENCE_HORIZON = 8.0
CONVERGENCE_GRID_RESOLUTION = 15
CONVERGENCE_COMPARISON_GRID_RESOLUTION = 11
ABLATION_WEIGHTS = (0.0, 1.0, 10.0, 50.0)
ABLATION_EPOCHS = 300
ABLATION_BASE_SEED = 700
ABLATION_REPEAT_COUNT = 3
ABLATION_SEEDS = tuple(
    range(ABLATION_BASE_SEED, ABLATION_BASE_SEED + ABLATION_REPEAT_COUNT)
)
NOISE_LEVELS = (0.0, 0.01, 0.05, 0.1)
NOISE_BASE_SEED = SEED
NOISE_REPEAT_COUNT = 3
NOISE_SEEDS = tuple(
    range(NOISE_BASE_SEED, NOISE_BASE_SEED + NOISE_REPEAT_COUNT)
)
PARAMETER_SCENARIOS = {
    "nominal": {"mass": 1.0, "damping": 0.4, "stiffness": 2.0},
    "mass +20%": {"mass": 1.2, "damping": 0.4, "stiffness": 2.0},
    "mass -20%": {"mass": 0.8, "damping": 0.4, "stiffness": 2.0},
    "damping -30%": {"mass": 1.0, "damping": 0.28, "stiffness": 2.0},
    "stiffness +20%": {"mass": 1.0, "damping": 0.4, "stiffness": 2.4},
    "combined variation": {"mass": 1.2, "damping": 0.28, "stiffness": 2.4},
}


def set_seed() -> None:
    """Set fixed project seeds without claiming universal determinism."""

    seed_random_generators(SEED)
    torch.set_num_threads(1)


def save_metrics_csv(
    rows: list[dict[str, float | str]],
    output_path: Path,
) -> None:
    """Save controller metrics as a CSV file."""

    fieldnames = [
        "initial_position",
        "initial_velocity",
        "controller",
        "control_limit",
        "final_state_norm",
        "settling_time",
        "settling_time_s",
        "quadratic_cost",
        "integrated_squared_control_effort",
        "control_energy",
        "max_abs_control",
    ]

    if not rows:
        raise ValueError("metric rows must not be empty.")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def scientific_configuration_snapshot() -> dict[str, Any]:
    """Return the effective default scientific configuration used below."""

    model = ZeroAtOriginController()
    architecture = []
    for layer in model.net:
        record: dict[str, Any] = {"type": type(layer).__name__}
        if hasattr(layer, "in_features"):
            record["in_features"] = int(layer.in_features)
            record["out_features"] = int(layer.out_features)
        architecture.append(record)
    return {
        "normalized_coordinate_convention": {
            "identifier": NORMALIZED_STATE_CONVENTION.name,
            "time_symbol": NORMALIZED_STATE_CONVENTION.time_symbol,
            "state": [
                NORMALIZED_STATE_CONVENTION.position_symbol,
                NORMALIZED_STATE_CONVENTION.velocity_symbol,
            ],
            "control_symbol": NORMALIZED_STATE_CONVENTION.control_symbol,
            "dimensionless": NORMALIZED_STATE_CONVENTION.dimensionless,
        },
        "plant": {
            "mass": MASS,
            "damping": DAMPING,
            "stiffness": STIFFNESS,
            "A": A.tolist(),
            "B": B.tolist(),
        },
        "lqr": {"Q": Q.tolist(), "R": R.tolist(), "K": K.tolist()},
        "controller": {
            "neural_architecture": architecture,
            "zero_at_origin": True,
            "normalized_control_limit": CONTROL_LIMIT,
        },
        "training": {
            "seed": SEED,
            "epochs": TRAINING_EPOCHS,
            "stability_weight": TRAINING_STABILITY_WEIGHT,
            "decay_margin": DECAY_MARGIN,
        },
        "lyapunov_evaluation": {
            "P": P.tolist(),
            "decay_margin": DECAY_MARGIN,
            "numerical_tolerance": DEFAULT_NUMERICAL_TOLERANCE,
            "position_bounds": [-2.0, 2.0],
            "velocity_bounds": [-3.0, 3.0],
            "grid_resolution": [81, 81],
        },
        "finite_horizon_convergence": {
            "position_bounds": list(CONVERGENCE_BOUNDS),
            "velocity_bounds": list(CONVERGENCE_BOUNDS),
            "horizon": CONVERGENCE_HORIZON,
            "convergence_tolerance": CONVERGENCE_TOLERANCE,
            "single_grid_resolution": CONVERGENCE_GRID_RESOLUTION,
            "comparison_grid_resolution": CONVERGENCE_COMPARISON_GRID_RESOLUTION,
        },
        "stability_weight_ablation": {
            "weights": list(ABLATION_WEIGHTS),
            "epochs": ABLATION_EPOCHS,
            "base_seed": ABLATION_BASE_SEED,
            "seeds": list(ABLATION_SEEDS),
            "repeat_count": len(ABLATION_SEEDS),
            "pairing_strategy": ABLATION_PAIRING_STRATEGY,
        },
        "measurement_noise": {
            "noise_levels": list(NOISE_LEVELS),
            "base_seed": NOISE_BASE_SEED,
            "seeds": list(NOISE_SEEDS),
            "repeat_count": len(NOISE_SEEDS),
            "pairing_strategy": NOISE_PAIRING_STRATEGY,
        },
        "initial_states": [list(state) for state in INITIAL_STATES],
        "parameter_scenarios": PARAMETER_SCENARIOS,
    }


def run_experiment(
    output_dir: Path,
    *,
    report_provenance: dict[str, Any] | None = None,
) -> None:
    """Generate one complete experiment only inside ``output_dir``."""

    set_seed()

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("LQR gain K:", K)
    print("Closed-loop eigenvalues:", CLOSED_LOOP_EIGENVALUES)
    print(f"Normalized control-input saturation limit: +/-{CONTROL_LIMIT}")

    model = ZeroAtOriginController()

    training_history = train_controller(
        model,
        epochs=TRAINING_EPOCHS,
        stability_weight=TRAINING_STABILITY_WEIGHT,
        stability_margin=DECAY_MARGIN,
    )

    nn_controller = make_nn_controller(model)

    saturated_lqr_controller = make_saturated_controller(
        lqr_controller,
        limit=CONTROL_LIMIT,
    )

    saturated_nn_controller = make_saturated_controller(
        nn_controller,
        limit=CONTROL_LIMIT,
    )

    controllers = {
        "LQR": (lqr_controller, "none"),
        "Neural network": (nn_controller, "none"),
        "Saturated LQR": (saturated_lqr_controller, CONTROL_LIMIT),
        "Saturated neural network": (saturated_nn_controller, CONTROL_LIMIT),
    }

    initial_states = [np.array(state) for state in INITIAL_STATES]

    solutions: dict[str, list] = {
        controller_name: [
            simulate(controller, initial_state)
            for initial_state in initial_states
        ]
        for controller_name, (controller, _limit) in controllers.items()
    }

    all_solutions = [
        solution
        for controller_solutions in solutions.values()
        for solution in controller_solutions
    ]

    if not all(solution.success for solution in all_solutions):
        raise RuntimeError("At least one simulation failed.")

    metric_rows: list[dict[str, float | str]] = []

    print()
    print("Quantitative performance metrics:")

    for controller_name, (controller, control_limit) in controllers.items():
        for initial_state, solution in zip(
            initial_states,
            solutions[controller_name],
            strict=True,
        ):
            metrics = calculate_metrics(solution, controller)

            row = {
                "initial_position": float(initial_state[0]),
                "initial_velocity": float(initial_state[1]),
                "controller": controller_name,
                "control_limit": control_limit,
                **metrics,
            }

            metric_rows.append(row)

            print(
                f"x0={initial_state}, "
                f"{controller_name}: "
                f"settling={metrics['settling_time']:.3f} normalized time, "
                f"cost={metrics['quadratic_cost']:.4f}, "
                "integrated squared control effort="
                f"{metrics['integrated_squared_control_effort']:.4f}, "
                f"max normalized |u|={metrics['max_abs_control']:.4f}, "
                f"final normalized-state norm={metrics['final_state_norm']:.3e}"
            )

    metrics_path = output_dir / "performance_metrics.csv"
    save_metrics_csv(metric_rows, metrics_path)

    print()
    print(
        "LQR sampled Lyapunov check:",
        grid_check(lqr_controller, decay_margin=DECAY_MARGIN),
    )
    print(
        "NN sampled Lyapunov check:",
        grid_check(nn_controller, decay_margin=DECAY_MARGIN),
    )

    torch.save(model.state_dict(), output_dir / "nn_controller.pt")

    save_plots(
        training_history,
        solutions["LQR"][0],
        solutions["Neural network"][0],
        output_dir,
    )
    save_model_architecture_diagram(output_dir)

    save_multiple_initial_conditions_plot(
        solutions["Neural network"],
        initial_states,
        output_dir,
    )
    save_phase_portrait_plot(
        solutions["Neural network"],
        initial_states,
        output_dir,
    )
    save_lyapunov_contour_plot(
        solutions["Neural network"],
        initial_states,
        P,
        output_dir,
    )
    convergence_result = evaluate_finite_horizon_convergence(
        saturated_nn_controller,
        position_bounds=CONVERGENCE_BOUNDS,
        velocity_bounds=CONVERGENCE_BOUNDS,
        grid_resolution=CONVERGENCE_GRID_RESOLUTION,
        convergence_tolerance=CONVERGENCE_TOLERANCE,
        horizon=CONVERGENCE_HORIZON,
        controller_label="Saturated NN",
    )

    print()
    print(
        "Finite-horizon convergence (Saturated NN): "
        f"{convergence_result.converged_count}/"
        f"{convergence_result.tested_count} sampled initial states "
        f"({100.0 * convergence_result.convergence_fraction:.1f}%) "
        "satisfied ||x(T)||_2 < normalized-state tolerance with "
        f"tau={convergence_result.horizon:g} and "
        "normalized-state tolerance="
        f"{convergence_result.convergence_tolerance:g} "
        f"on a {convergence_result.grid_resolution}x"
        f"{convergence_result.grid_resolution} grid with normalized-position bounds "
        f"{convergence_result.position_bounds} and normalized-velocity bounds "
        f"{convergence_result.velocity_bounds}."
    )

    save_finite_horizon_convergence_plot(
        convergence_result,
        output_dir,
    )

    convergence_comparison_controllers = {
        "LQR": lqr_controller,
        "Neural network": nn_controller,
        "Saturated NN": saturated_nn_controller,
    }

    convergence_comparison_results = {
        controller_name: evaluate_finite_horizon_convergence(
            controller,
            position_bounds=CONVERGENCE_BOUNDS,
            velocity_bounds=CONVERGENCE_BOUNDS,
            grid_resolution=CONVERGENCE_COMPARISON_GRID_RESOLUTION,
            convergence_tolerance=CONVERGENCE_TOLERANCE,
            horizon=CONVERGENCE_HORIZON,
            controller_label=controller_name,
        )
        for controller_name, controller in (
            convergence_comparison_controllers.items()
        )
    }

    print()
    print("Finite-horizon convergence comparison:")

    for controller_name, result in convergence_comparison_results.items():
        print(
            f"{controller_name}: {result.converged_count}/"
            f"{result.tested_count} sampled initial states "
            f"({100.0 * result.convergence_fraction:.1f}%) satisfied "
            f"||x(tau={result.horizon:g})||_2 < "
            f"{result.convergence_tolerance:g} on a "
            f"{result.grid_resolution}x{result.grid_resolution} grid with "
            f"normalized-position bounds {result.position_bounds} and "
            "normalized-velocity bounds "
            f"{result.velocity_bounds}."
        )

    save_finite_horizon_convergence_comparison_plot(
        convergence_comparison_results,
        output_dir,
    )

    ablation_weights = list(ABLATION_WEIGHTS)
    ablation_initial_state = np.array([1.5, 0.0])
    ablation_seed_plan = ExperimentSeedPlan.consecutive(
        ABLATION_BASE_SEED,
        ABLATION_REPEAT_COUNT,
    )

    ablation_rows = run_stability_weight_ablation(
        stability_weights=ablation_weights,
        initial_state=ablation_initial_state,
        epochs=ABLATION_EPOCHS,
        stability_margin=DECAY_MARGIN,
        seed_plan=ablation_seed_plan,
    )
    ablation_aggregates = aggregate_ablation_results(ablation_rows)

    ablation_csv_path = output_dir / "stability_weight_ablation_trials_paired.csv"
    save_ablation_results_csv(
        ablation_rows,
        ablation_csv_path,
    )
    save_ablation_aggregate_csv(
        ablation_aggregates,
        output_dir / "stability_weight_ablation_summary_paired.csv",
    )

    save_stability_weight_ablation_plot(
        ablation_rows,
        output_dir,
        aggregate_rows=ablation_aggregates,
        filename="stability_weight_ablation_paired.png",
    )

    print()
    print("Stability-weight ablation results:")

    for row in ablation_aggregates:
        print(
            f"weight={row['stability_weight']:g}: "
            f"n={row['n']}, "
            "mean sampled derivative violation="
            f"{row['derivative_violation_fraction_mean']:.3f}, "
            "mean sampled decay-margin violation="
            f"{row['decay_margin_violation_fraction_mean']:.3f}, "
            "mean final normalized-state norm="
            f"{row['final_state_norm_mean']:.3e}"
        )

    first_initial_condition_solutions = {
        controller_name: controller_solutions[0]
        for controller_name, controller_solutions in solutions.items()
    }

    save_saturation_comparison_plot(
        first_initial_condition_solutions,
        output_dir,
    )

    noise_levels = list(NOISE_LEVELS)
    noise_initial_state = np.array([1.5, 0.0])
    noise_seed_plan = ExperimentSeedPlan.consecutive(
        NOISE_BASE_SEED,
        NOISE_REPEAT_COUNT,
    )
    noise_rows, noise_solutions_by_trial = run_measurement_noise_trials(
        saturated_nn_controller,
        noise_initial_state,
        noise_levels,
        seed_plan=noise_seed_plan,
    )
    noise_aggregates = aggregate_noise_results(noise_rows)
    save_noise_trial_results_csv(
        noise_rows,
        output_dir / "noise_robustness_trials_paired.csv",
    )
    save_noise_aggregate_csv(
        noise_aggregates,
        output_dir / "noise_robustness_summary_paired.csv",
    )

    print()
    print("Noise robustness results:")

    for row in noise_aggregates:
        print(
            f"normalized-coordinate noise std={row['noise_std']:g}: "
            f"n={row['n']}, mean final normalized-state norm="
            f"{row['final_state_norm_mean']:.3e}"
        )

    representative_noise_solutions = {
        noise_std: noise_solutions_by_trial[(noise_std, noise_seed_plan.seeds[0])]
        for noise_std in noise_levels
    }
    save_noise_robustness_plot(
        representative_noise_solutions,
        output_dir,
        filename="noise_robustness_paired_trajectories.png",
    )
    save_noise_robustness_statistics_plot(
        noise_rows,
        noise_aggregates,
        output_dir,
    )

    parameter_initial_state = np.array([1.5, 0.0])

    parameter_scenarios = PARAMETER_SCENARIOS

    parameter_solutions = {
        scenario_name: simulate_parameter_variation(
            saturated_nn_controller,
            parameter_initial_state,
            **parameters,
        )
        for scenario_name, parameters in parameter_scenarios.items()
    }

    if not all(solution.success for solution in parameter_solutions.values()):
        raise RuntimeError("At least one parameter-variation simulation failed.")

    print()
    print("Parameter robustness results:")

    for scenario_name, solution in parameter_solutions.items():
        final_norm = state_norm(solution.y[:, -1])
        print(
            f"{scenario_name}: "
            f"final normalized-state norm={final_norm:.3e}"
        )

    save_parameter_robustness_plot(
        parameter_solutions,
        output_dir,
    )

    report_path = output_dir / "report.md"
    generate_experiment_report(
        output_dir,
        report_path,
        finite_horizon_results=convergence_comparison_results,
        experiment_seed_metadata={
            "Stability-weight ablation": ablation_seed_plan.metadata(
                pairing_strategy=ABLATION_PAIRING_STRATEGY,
            ),
            "Measurement-noise robustness": noise_seed_plan.metadata(
                pairing_strategy=NOISE_PAIRING_STRATEGY,
            ),
        },
        provenance=report_provenance,
    )

    print()
    print(f"Metrics saved to: {metrics_path.resolve()}")
    print(f"Experiment report saved to: {report_path.resolve()}")
    print(f"Model and figures saved in: {output_dir.resolve()}")


def _report_provenance(context: RunContext) -> dict[str, Any]:
    return {
        "run_id": context.run_id,
        "source_commit": context.git.commit_sha,
        "git_dirty": context.git.dirty,
        "generated_at_utc": context.generated_at_utc,
        "package_version": context.package_version,
        "manifest": "manifest.json",
        "configuration_sha256": context.configuration_sha256,
        "ablation_seeds": list(ABLATION_SEEDS),
        "noise_seeds": list(NOISE_SEEDS),
        "repeat_count": len(ABLATION_SEEDS),
        "pairing_strategies": [
            ABLATION_PAIRING_STRATEGY,
            NOISE_PAIRING_STRATEGY,
        ],
        "decay_margin": DECAY_MARGIN,
        "finite_horizon": context.scientific_configuration[
            "finite_horizon_convergence"
        ],
    }


def main(argv: list[str] | None = None) -> Path:
    """Publish one provenance-aware run without touching legacy artifacts."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id")
    parser.add_argument("--allow-dirty", action="store_true")
    parser.add_argument("--results-dir", type=Path, default=Path("results"))
    args = parser.parse_args(argv)
    command = "python main.py"
    if args.run_id:
        command += f" --run-id {args.run_id}"
    if args.allow_dirty:
        command += " --allow-dirty"

    def producer(context: RunContext) -> None:
        run_experiment(
            context.staging_dir,
            report_provenance=_report_provenance(context),
        )

    run_dir = publish_run(
        producer,
        scientific_configuration_snapshot(),
        results_dir=args.results_dir,
        repo_root=Path(__file__).resolve().parent,
        run_id=args.run_id,
        allow_dirty=args.allow_dirty,
        generation_command=command,
    )
    print(f"Published verified run: {run_dir.as_posix()}")
    return run_dir


if __name__ == "__main__":
    main()
