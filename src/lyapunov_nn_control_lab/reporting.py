import csv
from itertools import islice
from numbers import Integral
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .finite_horizon_convergence import FiniteHorizonConvergenceResult


def read_csv_rows(
    csv_path: Path,
    max_rows: int = 8,
) -> list[dict[str, str]]:
    """Read a small number of rows from a CSV file."""

    if isinstance(max_rows, bool) or not isinstance(max_rows, Integral):
        raise TypeError("max_rows must be a nonnegative integer.")
    if max_rows < 0:
        raise ValueError("max_rows must be a nonnegative integer.")
    if not csv_path.exists():
        return []

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(islice(reader, max_rows))


def escape_markdown_table_cell(value: object) -> str:
    """Escape content that would otherwise break a Markdown table cell."""

    if value is None:
        return ""

    text = str(value).replace("\r\n", "\n").replace("\r", "\n")
    return text.replace("|", r"\|").replace("\n", "<br>")


def format_markdown_table(
    rows: list[dict[str, str]],
    columns: list[str],
) -> list[str]:
    """Format selected CSV columns as a Markdown table."""

    if not rows:
        return ["No data available."]

    lines = [
        "| "
        + " | ".join(escape_markdown_table_cell(column) for column in columns)
        + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]

    for row in rows:
        values = [
            escape_markdown_table_cell(row.get(column, ""))
            for column in columns
        ]
        lines.append("| " + " | ".join(values) + " |")

    return lines


def generate_experiment_report(
    results_dir: Path,
    output_path: Path,
    *,
    finite_horizon_results: (
        dict[str, "FiniteHorizonConvergenceResult"] | None
    ) = None,
) -> None:
    """Generate a Markdown report summarizing all experiment outputs."""

    performance_rows = read_csv_rows(
        results_dir / "performance_metrics.csv",
        max_rows=8,
    )
    ablation_rows = read_csv_rows(
        results_dir / "stability_weight_ablation.csv",
        max_rows=8,
    )
    uses_legacy_ablation_schema = any(
        "lyapunov_violation_fraction" in row
        and "decay_margin_violation_fraction" not in row
        for row in ablation_rows
    )

    plot_files = [
        "model_architecture.png",
        "position_comparison.png",
        "training_loss.png",
        "multiple_initial_conditions.png",
        "saturation_comparison.png",
        "noise_robustness.png",
        "parameter_robustness.png",
        "phase_portrait.png",
        "lyapunov_contours.png",
        "finite_horizon_convergence.png",
        "finite_horizon_convergence_comparison.png",
        # Retained only so reports can link historical pre-migration files.
        "region_of_attraction.png",
        "region_of_attraction_comparison.png",
        "stability_weight_ablation.png",
    ]

    available_plots = [
        plot_file
        for plot_file in plot_files
        if (results_dir / plot_file).exists()
    ]

    lines = [
        "# Experiment Report",
        "",
        "This report summarizes the generated results for the Lyapunov neural-network control lab.",
        "",
        "## Main experiments",
        "",
        "| Experiment | Output |",
        "|---|---|",
        "| Model architecture | `model_architecture.png` |",
        "| LQR and neural-network comparison | `position_comparison.png` |",
        "| Stability-aware training loss | `training_loss.png` |",
        "| Multiple initial conditions | `multiple_initial_conditions.png` |",
        "| Actuator saturation comparison | `saturation_comparison.png` |",
        "| Measurement-noise robustness | `noise_robustness.png` |",
        "| Parameter robustness | `parameter_robustness.png` |",
        "| Phase portrait | `phase_portrait.png` |",
        "| Lyapunov contour plot | `lyapunov_contours.png` |",
        "| Finite-horizon convergence map | `finite_horizon_convergence.png` |",
        "| Finite-horizon convergence comparison | `finite_horizon_convergence_comparison.png` |",
        "| Stability-weight ablation study | `stability_weight_ablation.png` |",
        "",
        "## Available plots",
        "",
    ]

    if available_plots:
        for plot_file in available_plots:
            if plot_file.startswith("region_of_attraction"):
                lines.append(
                    f"- [`{plot_file}`]({plot_file}) (historical filename for "
                    "a finite-horizon convergence figure)"
                )
            else:
                lines.append(f"- [`{plot_file}`]({plot_file})")
    else:
        lines.append("No plot files were found.")

    lines.extend(
        [
            "",
            "## Finite-horizon convergence sampling",
            "",
            "A sampled state is classified as converged only when the strict "
            "final-state criterion `||x(T)|| < tolerance` holds. This "
            "finite-time result depends on the horizon, tolerance, and grid; "
            "it is not an asymptotic attraction-region certificate.",
            "",
        ]
    )

    if finite_horizon_results:
        lines.extend(
            [
                "| Controller | Horizon [s] | Tolerance | Position bounds | "
                "Velocity bounds | Grid | Converged / tested | Fraction |",
                "|---|---:|---:|---|---|---:|---:|---:|",
            ]
        )
        for controller_name, result in finite_horizon_results.items():
            lines.append(
                f"| {escape_markdown_table_cell(controller_name)} | "
                f"{result.horizon:g} | "
                f"{result.convergence_tolerance:g} | "
                f"{result.position_bounds} | "
                f"{result.velocity_bounds} | "
                f"{result.grid_resolution} x {result.grid_resolution} | "
                f"{result.converged_count} / {result.tested_count} | "
                f"{100.0 * result.convergence_fraction:.1f}% |"
            )
    else:
        lines.append("No finite-horizon convergence metadata were supplied.")

    lines.extend(
        [
            "",
            "## Performance metrics preview",
            "",
        ],
    )

    lines.extend(
        format_markdown_table(
            performance_rows,
            [
                "controller",
                "initial_position",
                "initial_velocity",
                "final_state_norm",
                "settling_time_s",
                "quadratic_cost",
                "control_energy",
                "max_abs_control",
            ],
        ),
    )

    lines.extend(
        [
            "",
            "## Stability-weight ablation preview",
            "",
        ],
    )

    lines.extend(
        format_markdown_table(
            ablation_rows,
            [
                "stability_weight",
                "decay_margin",
                "derivative_violation_fraction",
                "decay_margin_violation_fraction",
                "max_vdot",
                "max_decay_residual",
                "final_state_norm",
                "settling_time_s",
                "quadratic_cost",
                "control_energy",
            ],
        ),
    )

    if uses_legacy_ablation_schema:
        lines.extend(
            [
                "",
                "The available ablation CSV uses the legacy ambiguous violation "
                "column. Regenerate it in the planned result-provenance operation "
                "before interpreting derivative and decay-margin violations.",
            ]
        )

    lines.extend(
        [
            "",
            "## Interpretation guide",
            "",
            "- Lower final state norm means the controller drives the state closer to the equilibrium.",
            "- Lower settling time means the controller stabilizes faster.",
            "- Lower control energy means the controller uses less actuation effort.",
            "- The derivative violation fraction counts sampled states with V-dot above numerical tolerance.",
            "- The decay-margin violation fraction counts sampled states where V-dot + alpha ||x||^2 exceeds numerical tolerance.",
            "- Both Lyapunov metrics cover only the finite sampled grid and are not a formal continuous-state certificate.",
            "- Finite-horizon convergence percentages report only the sampled "
            "states that meet the stated final-state tolerance after the stated "
            "horizon.",
            "",
        ],
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )
