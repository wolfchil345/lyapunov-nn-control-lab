"""Clean generated files from the results directory."""

from __future__ import annotations

from pathlib import Path


RESULTS_DIR = Path("results")


def main() -> None:
    """Remove generated files from the results directory."""
    if not RESULTS_DIR.exists():
        print("results directory does not exist.")
        return

    removed_count = 0
    for path in RESULTS_DIR.iterdir():
        if path.is_file():
            path.unlink()
            removed_count += 1

    print(f"Removed {removed_count} file(s) from results/.")


if __name__ == "__main__":
    main()
