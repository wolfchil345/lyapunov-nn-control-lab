import csv
from itertools import islice
from numbers import Integral
from pathlib import Path
from typing import TYPE_CHECKING, Any

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


def canonicalize_metric_aliases(rows: list[dict[str, str]]) -> None:
    """Add precise metric names when reading historical compatible CSVs."""

    for row in rows:
        row.setdefault("settling_time", row.get("settling_time_s", ""))
        row.setdefault(
            "integrated_squared_control_effort",
            row.get("control_energy", ""),
        )


def generate_experiment_report(
    results_dir: Path,
    output_path: Path,
    *,
    finite_horizon_results: (
        dict[str, "FiniteHorizonConvergenceResult"] | None
    ) = None,
    experiment_seed_metadata: dict[str, dict[str, Any]] | None = None,
    provenance: dict[str, Any] | None = None,
) -> None:
    """Generate a Markdown report summarizing all experiment outputs."""

    performance_rows = read_csv_rows(
        results_dir / "performance_metrics.csv",
        max_rows=8,
    )
    paired_ablation_path = (
        results_dir / "stability_weight_ablation_trials_paired.csv"
    )
    ablation_rows = read_csv_rows(
        paired_ablation_path
        if paired_ablation_path.exists()
        else results_dir / "stability_weight_ablation.csv",
        max_rows=8,
    )
    canonicalize_metric_aliases(performance_rows)
    canonicalize_metric_aliases(ablation_rows)
    uses_legacy_ablation_schema = any(
        "lyapunov_violation_fraction" in row
        and "decay_margin_violation_fraction" not in row
        for row in ablation_rows
    )
    noise_plot = (
        "noise_robustness_paired.png"
        if (results_dir / "noise_robustness_paired.png").exists()
        else "noise_robustness.png"
    )
    ablation_plot = (
        "stability_weight_ablation_paired.png"
        if (results_dir / "stability_weight_ablation_paired.png").exists()
        else "stability_weight_ablation.png"
    )

    plot_files = [
        "model_architecture.png",
        "position_comparison.png",
        "training_loss.png",
        "multiple_initial_conditions.png",
        "saturation_comparison.png",
        "noise_robustness.png",
        "noise_robustness_paired.png",
        "noise_robustness_paired_trajectories.png",
        "parameter_robustness.png",
        "phase_portrait.png",
        "lyapunov_contours.png",
        "finite_horizon_convergence.png",
        "finite_horizon_convergence_comparison.png",
        # Retained only so reports can link historical pre-migration files.
        "region_of_attraction.png",
        "region_of_attraction_comparison.png",
        "stability_weight_ablation.png",
        "stability_weight_ablation_paired.png",
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
    ]

    if provenance:
        lines.extend(
            [
                "## Run provenance",
                "",
                f"- Run ID: `{escape_markdown_table_cell(provenance.get('run_id', ''))}`",
                f"- Source commit: `{escape_markdown_table_cell(provenance.get('source_commit', ''))}`",
                f"- Git working tree dirty: `{str(provenance.get('git_dirty')).lower()}`",
                f"- Generated at (UTC): `{escape_markdown_table_cell(provenance.get('generated_at_utc', ''))}`",
                f"- Package version: `{escape_markdown_table_cell(provenance.get('package_version', ''))}`",
                f"- Configuration SHA-256: `{escape_markdown_table_cell(provenance.get('configuration_sha256', ''))}`",
                f"- Manifest: [`{escape_markdown_table_cell(provenance.get('manifest', 'manifest.json'))}`]({escape_markdown_table_cell(provenance.get('manifest', 'manifest.json'))})",
                f"- Stability-weight seeds: `{provenance.get('ablation_seeds', [])}`",
                f"- Measurement-noise seeds: `{provenance.get('noise_seeds', [])}`",
                f"- Repeat count: `{provenance.get('repeat_count', '')}`",
                f"- Pairing strategies: `{provenance.get('pairing_strategies', [])}`",
                f"- Lyapunov decay margin: `{provenance.get('decay_margin', '')}`",
                f"- Finite-horizon settings: `{provenance.get('finite_horizon', {})}`",
                "",
            ]
        )

    lines.extend(
        [
            "## Main experiments",
            "",
        "| Experiment | Output |",
        "|---|---|",
        "| Model architecture | `model_architecture.png` |",
        "| LQR and neural-network comparison | `position_comparison.png` |",
        "| Stability-aware training loss | `training_loss.png` |",
        "| Multiple initial conditions | `multiple_initial_conditions.png` |",
        "| Actuator saturation comparison | `saturation_comparison.png` |",
        f"| Measurement-noise robustness | `{noise_plot}` |",
        "| Parameter robustness | `parameter_robustness.png` |",
        "| Phase portrait | `phase_portrait.png` |",
        "| Lyapunov contour plot | `lyapunov_contours.png` |",
        "| Finite-horizon convergence map | `finite_horizon_convergence.png` |",
        "| Finite-horizon convergence comparison | `finite_horizon_convergence_comparison.png` |",
        f"| Stability-weight ablation study | `{ablation_plot}` |",
            "",
            "## Available plots",
            "",
        ]
    )

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
            "## Experimental seed design",
            "",
        ]
    )
    if experiment_seed_metadata:
        lines.extend(
            [
                "| Experiment | Base seed | Explicit seeds | Repeats | Pairing strategy |",
                "|---|---:|---|---:|---|",
            ]
        )
        for experiment_name, metadata in experiment_seed_metadata.items():
            lines.append(
                f"| {escape_markdown_table_cell(experiment_name)} | "
                f"{escape_markdown_table_cell(metadata.get('base_seed', ''))} | "
                f"{escape_markdown_table_cell(metadata.get('seed_list', ''))} | "
                f"{escape_markdown_table_cell(metadata.get('repeat_count', ''))} | "
                f"{escape_markdown_table_cell(metadata.get('pairing_strategy', ''))} |"
            )
        lines.extend(
            [
                "",
                "Fixed seeds support repeatable paired CPU comparisons under "
                "the same environment; they do not guarantee fully "
                "deterministic execution on every accelerator or platform.",
            ]
        )
    else:
        lines.append("No experimental seed metadata were supplied.")

    lines.extend(
        [
            "",
            "## Finite-horizon convergence sampling",
            "",
            "A sampled state is classified as converged only when the strict "
            "final-state criterion `||x(T)||_2 < tolerance` holds in "
            "normalized coordinates. This "
            "finite-time result depends on the horizon, tolerance, and grid; "
            "it is not an asymptotic attraction-region certificate.",
            "",
        ]
    )

    if finite_horizon_results:
        lines.extend(
            [
                "| Controller | Horizon (normalized time) | Normalized-state "
                "tolerance | Normalized-position bounds | Normalized-velocity "
                "bounds | Grid | Converged / tested | Fraction |",
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
                "settling_time",
                "quadratic_cost",
                "integrated_squared_control_effort",
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
                "settling_time",
                "quadratic_cost",
                "integrated_squared_control_effort",
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
            "- The final normalized-state norm is the Euclidean norm of normalized position and velocity.",
            "- Settling time is measured in normalized time and requires all later samples to remain inside the tolerance.",
            "- Integrated squared control effort is the integral of normalized control squared; it is not physical energy.",
            "- The derivative violation fraction counts sampled states with V-dot above numerical tolerance.",
            "- The decay-margin violation fraction counts sampled states where V-dot + alpha ||x||_2^2 exceeds numerical tolerance.",
            "- Both Lyapunov metrics cover only the finite sampled grid and are not a formal continuous-state certificate.",
            "- Finite-horizon convergence percentages report only the sampled "
            "states that meet the stated normalized Euclidean final-state "
            "tolerance after the stated normalized-time horizon.",
            "",
        ],
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )
