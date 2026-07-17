from pathlib import Path

from src.reporting import (
    format_markdown_table,
    generate_experiment_report,
    read_csv_rows,
)


def test_read_csv_rows_reads_limited_rows(tmp_path):
    csv_path = tmp_path / "data.csv"
    csv_path.write_text(
        "name,value\n"
        "a,1\n"
        "b,2\n",
        encoding="utf-8",
    )

    rows = read_csv_rows(
        csv_path,
        max_rows=1,
    )

    assert len(rows) == 1
    assert rows[0]["name"] == "a"


def test_format_markdown_table_handles_rows():
    rows = [
        {
            "name": "controller",
            "value": "stable",
        },
    ]

    table = format_markdown_table(
        rows,
        ["name", "value"],
    )

    assert "| name | value |" in table
    assert "| controller | stable |" in table


def test_generate_experiment_report_creates_file(tmp_path):
    results_dir = tmp_path
    output_path = results_dir / "experiment_report.md"

    (results_dir / "performance_metrics.csv").write_text(
        "controller,initial_position,initial_velocity,final_state_norm,settling_time_s,quadratic_cost,control_energy,max_abs_control\n"
        "LQR,1.5,0.0,0.001,2.0,4.0,1.0,2.0\n",
        encoding="utf-8",
    )

    (results_dir / "stability_weight_ablation.csv").write_text(
        "stability_weight,lyapunov_violation_fraction,final_state_norm,settling_time_s,quadratic_cost,control_energy\n"
        "10.0,0.01,0.001,2.0,4.0,1.0\n",
        encoding="utf-8",
    )

    generate_experiment_report(
        results_dir,
        output_path,
    )

    text = output_path.read_text(encoding="utf-8")

    assert output_path.exists()
    assert "# Experiment Report" in text
    assert "Performance metrics preview" in text
    assert "Stability-weight ablation preview" in text
