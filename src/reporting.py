import csv
from pathlib import Path


def read_csv_rows(
    csv_path: Path,
    max_rows: int = 8,
) -> list[dict[str, str]]:
    """Read a small number of rows from a CSV file."""

    if not csv_path.exists():
        return []

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)[:max_rows]


def format_markdown_table(
    rows: list[dict[str, str]],
    columns: list[str],
) -> list[str]:
    """Format selected CSV columns as a Markdown table."""

    if not rows:
        return ["No data available."]

    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]

    for row in rows:
        values = [
            row.get(column, "")
            for column in columns
        ]
        lines.append("| " + " | ".join(values) + " |")

    return lines


def generate_experiment_report(
    results_dir: Path,
    output_path: Path,
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
        "| Region of attraction map | `region_of_attraction.png` |",
        "| Region of attraction controller comparison | `region_of_attraction_comparison.png` |",
        "| Stability-weight ablation study | `stability_weight_ablation.png` |",
        "",
        "## Available plots",
        "",
    ]

    if available_plots:
        for plot_file in available_plots:
            lines.append(f"- [`{plot_file}`]({plot_file})")
    else:
        lines.append("No plot files were found.")

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
                "lyapunov_violation_fraction",
                "final_state_norm",
                "settling_time_s",
                "quadratic_cost",
                "control_energy",
            ],
        ),
    )

    lines.extend(
        [
            "",
            "## Interpretation guide",
            "",
            "- Lower final state norm means the controller drives the state closer to the equilibrium.",
            "- Lower settling time means the controller stabilizes faster.",
            "- Lower control energy means the controller uses less actuation effort.",
            "- Lower Lyapunov violation fraction means fewer sampled states violate the Lyapunov decrease condition.",
            "- Region of attraction results estimate which initial states converge successfully.",
            "",
        ],
    )

    output_path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )
