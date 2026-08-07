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
    """Run the non-destructive provenance-aware experiment pipeline."""
    print("Running provenance-aware full experiment pipeline...")
    run_command([sys.executable, "main.py"])
    print()
    print("Full experiment pipeline completed without deleting prior runs.")


if __name__ == "__main__":
    main()
