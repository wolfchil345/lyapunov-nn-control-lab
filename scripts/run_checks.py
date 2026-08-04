"""Run local project checks."""

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
    """Run package, documentation, lint, test, and quick-start checks."""
    print("Running local checks...")
    run_command([sys.executable, "scripts/check_package.py"])
    run_command([sys.executable, "scripts/check_docs_links.py"])
    run_command([sys.executable, "scripts/check_i18n_docs.py"])
    run_command([sys.executable, "-m", "ruff", "check", "."])
    run_command([sys.executable, "-m", "pytest"])
    run_command([sys.executable, "examples/quick_start.py"])
    print()
    print("All checks passed.")


if __name__ == "__main__":
    main()
