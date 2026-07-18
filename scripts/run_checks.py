"""Run basic local project checks."""

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
    """Run the project health checks."""
    run_command([sys.executable, "-m", "pytest"])
    run_command([sys.executable, "examples/quick_start.py"])
    print()
    print("All checks passed.")


if __name__ == "__main__":
    main()
