from __future__ import annotations

import subprocess
import sys


COMMANDS = [
    ["python", "scripts/project_status.py"],
    ["python", "scripts/check_workflow_badges.py"],
    ["python", "scripts/check_environment.py"],
    ["python", "scripts/list_results.py"],
    ["python", "scripts/run_checks.py"],
]


def run_command(command: list[str]) -> int:
    command_text = " ".join(command)
    print("")
    print(f"Running: {command_text}")
    print("-" * (9 + len(command_text)))
    completed = subprocess.run(command)
    return completed.returncode


def main() -> int:
    print("Quality gate")
    print("=" * 12)

    for command in COMMANDS:
        return_code = run_command(command)
        if return_code != 0:
            command_text = " ".join(command)
            print("")
            print(f"Quality gate failed at: {command_text}")
            return return_code

    print("")
    print("Quality gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
