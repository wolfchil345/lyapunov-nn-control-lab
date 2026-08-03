from __future__ import annotations

from pathlib import Path


KEY_FILES = [
    "README.md",
    "README.ja.md",
    "README.ko.md",
    "README.th.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING.ja.md",
    "CONTRIBUTING.ko.md",
    "CONTRIBUTING.th.md",
    "SECURITY.md",
    "SECURITY.ja.md",
    "SECURITY.ko.md",
    "SECURITY.th.md",
    "Makefile",
    "pyproject.toml",
    "docs/en/index.md",
    "docs/ja/index.md",
    "docs/ko/index.md",
    "docs/th/index.md",
    "docs/en/ci_workflows.md",
    "docs/en/project_status.md",
    "docs/en/maintenance.md",
    "docs/en/git_workflow.md",
    "docs/en/onboarding.md",
    "scripts/run_checks.py",
    "scripts/check_docs_links.py",
    "scripts/check_i18n_docs.py",
    "scripts/check_environment.py",
    "scripts/list_results.py",
    "scripts/new_experiment_log.py",
    "scripts/quality_gate.py",
    "scripts/check_workflow_badges.py",
    ".github/workflows/local-checks.yml",
    ".github/workflows/quality-gate.yml",
    "results/experiment_report.md",
    "results/experiment_report.ja.md",
    "results/experiment_report.ko.md",
    "results/experiment_report.th.md",
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

    docs_count = count_files(Path("docs"), "*.md")
    scripts_count = count_files(Path("scripts"), "*.py")
    tests_count = count_files(Path("tests"), "test_*.py")
    workflows_count = count_files(Path(".github/workflows"), "*.yml")
    results_count = count_files(Path("results"))

    print("")
    print("Inventory:")
    print(f"- Documentation files: {docs_count}")
    print(f"- Script files: {scripts_count}")
    print(f"- Test files: {tests_count}")
    print(f"- Workflow files: {workflows_count}")
    print(f"- Result files: {results_count}")

    print("")
    if missing:
        print(f"Status: needs attention. Missing key files: {missing}")
        return 1

    print("Status: ready for checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
