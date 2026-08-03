"""Print a quick summary of generated experiment results."""

from __future__ import annotations

import csv
from pathlib import Path

RESULTS_DIR = Path("results")


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    """Read a CSV file into a list of dictionaries."""
    if not path.exists():
        return []

    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def print_performance_metrics() -> None:
    """Print controller performance metrics if available."""
    rows = read_csv_rows(RESULTS_DIR / "performance_metrics.csv")
    if not rows:
        print("No performance_metrics.csv found.")
        return

    print("Performance metrics")
    for row in rows:
        controller = row.get("controller", "unknown")
        final_norm = row.get("final_state_norm", "n/a")
        settling_time = row.get("settling_time_s", "n/a")
        cost = row.get("quadratic_cost", "n/a")
        energy = row.get("control_energy", "n/a")
        print(f"- {controller}: final_norm={final_norm}, settling_time_s={settling_time}, cost={cost}, control_energy={energy}")


def print_ablation_metrics() -> None:
    """Print stability-weight ablation metrics if available."""
    rows = read_csv_rows(RESULTS_DIR / "stability_weight_ablation.csv")
    if not rows:
        print("No stability_weight_ablation.csv found.")
        return

    print()
    print("Stability-weight ablation")
    for row in rows:
        weight = row.get("stability_weight", "n/a")
        final_norm = row.get("final_state_norm", "n/a")
        violation = row.get(
            "lyapunov_violation_fraction",
            row.get("violation_fraction", row.get("violation_ratio", "n/a")),
        )
        print(f"- weight={weight}: final_norm={final_norm}, violation={violation}")


def main() -> None:
    """Print all available result summaries."""
    print_performance_metrics()
    print_ablation_metrics()


if __name__ == "__main__":
    main()
