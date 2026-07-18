"""Run the complete experiment pipeline."""

from __future__ import annotations

import subprocess
import sys


def run_command(command: list[str]) -> None:
    """Run one command and stop if it fails."""
    print()
    print("$ " + " ".join(command))
    result = subprocess.run(command, check=False)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> None:
    """Run cleanup, main experiment, and result summary."""
    print("Running full experiment pipeline...")
    run_command([sys.executable, "scripts/clean_results.py"])
    run_command([sys.executable, "main.py"])
    run_command([sys.executable, "scripts/summarize_results.py"])
    print()
    print("Full experiment pipeline completed.")


if __name__ == "__main__":
    main()
