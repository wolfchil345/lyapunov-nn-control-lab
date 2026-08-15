"""Remove only incomplete provenance-run staging directories."""

from __future__ import annotations

from pathlib import Path
import shutil


RESULTS_DIR = Path("results")


def clean_incomplete_staging(results_dir: Path = RESULTS_DIR) -> int:
    """Remove exact ``.staging-*`` directories without touching valid runs."""

    runs_dir = Path(results_dir) / "runs"
    if not runs_dir.exists():
        return 0
    removed_count = 0
    for path in runs_dir.iterdir():
        if (
            path.name.startswith(".staging-")
            and path.is_dir()
            and not path.is_symlink()
        ):
            shutil.rmtree(path)
            removed_count += 1
    return removed_count


def main() -> None:
    """Clean incomplete staging directories only."""

    if not RESULTS_DIR.exists():
        print("results directory does not exist; nothing to clean.")
        return
    removed_count = clean_incomplete_staging()
    print(
        f"Removed {removed_count} incomplete staging director"
        f"{'y' if removed_count == 1 else 'ies'}; completed runs and legacy "
        "artifacts were preserved."
    )


if __name__ == "__main__":
    main()
