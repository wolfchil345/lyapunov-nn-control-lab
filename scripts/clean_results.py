"""Safely clean known generated experiment files from the results directory."""

from __future__ import annotations

import argparse
from pathlib import Path

RESULTS_DIR = Path("results")
GENERATED_FILENAMES = frozenset(
    {
        "experiment_report.ja.md",
        "experiment_report.ko.md",
        "experiment_report.md",
        "experiment_report.th.md",
        "lyapunov_contours.png",
        "model_architecture.png",
        "multiple_initial_conditions.png",
        "nn_controller.pt",
        "noise_robustness.png",
        "parameter_robustness.png",
        "performance_metrics.csv",
        "phase_portrait.png",
        "position_comparison.png",
        "region_of_attraction.png",
        "region_of_attraction_comparison.png",
        "saturation_comparison.png",
        "stability_weight_ablation.csv",
        "stability_weight_ablation.png",
        "training_loss.png",
    },
)


def generated_paths(results_dir: Path = RESULTS_DIR) -> list[Path]:
    """Return existing files that the experiment pipeline can regenerate."""

    return sorted(
        path
        for name in GENERATED_FILENAMES
        if (path := results_dir / name).is_file()
    )


def clean_results(results_dir: Path = RESULTS_DIR, *, confirmed: bool = False) -> int:
    """List or remove only known generated files and return the target count."""

    paths = generated_paths(results_dir)
    if not paths:
        print("No known generated result files found.")
        return 0

    action = "Removing" if confirmed else "Would remove"
    print(f"{action} {len(paths)} known generated file(s):")
    for path in paths:
        print(f"- {path}")

    if not confirmed:
        print("Dry run only. Re-run with --yes to remove these files.")
        return len(paths)

    for path in paths:
        path.unlink()
    print(f"Removed {len(paths)} known generated file(s).")
    return len(paths)


def parse_args() -> argparse.Namespace:
    """Parse the explicit cleanup confirmation flag."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--yes",
        action="store_true",
        help="remove the listed generated files instead of performing a dry run",
    )
    return parser.parse_args()


def main() -> int:
    """Preview cleanup by default and remove files only with --yes."""

    args = parse_args()
    clean_results(confirmed=args.yes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
