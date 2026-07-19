from __future__ import annotations

from pathlib import Path


KEY_FILES = [
    "README.md",
    "Makefile",
    "pyproject.toml",
    "docs/index.md",
    "scripts/run_checks.py",
    "scripts/check_environment.py",
    "scripts/list_results.py",
    "scripts/new_experiment_log.py",
    ".github/workflows/local-checks.yml",
]


def count_files(directory: Path, pattern: str = "*") -> int:
    if not directory.exists():
        return 0
    return sum(1 for path in directory.rglob(pattern) if path.is_file())


def status_label(path: Path) -> str:
    return "OK" if path.exists() else "MISSING"


def main() -> int:
    print("Project status")
    print("=" * 14)
    print("")

    print("Key files:")
    missing = 0
    for file_name in KEY_FILES:
        path = Path(file_name)
        label = status_label(path)
        if label == "MISSING":
            missing += 1
        print(f"- {label}: {file_name}")

    print("")
    print("Inventory:")
    print(f"- Documentation files: {count_files(Path(\"docs\"), \"*.md\")}")
    print(f"- Script files: {count_files(Path(\"scripts\"), \"*.py\")}")
    print(f"- Test files: {count_files(Path(\"tests\"), \"test_*.py\")}")
    print(f"- Workflow files: {count_files(Path(\".github/workflows\"), \"*.yml\")}")
    print(f"- Result files: {count_files(Path(\"results\"))}")

    print("")
    if missing:
        print(f"Status: needs attention. Missing key files: {missing}")
        return 1

    print("Status: ready for checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
