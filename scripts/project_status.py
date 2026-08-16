from __future__ import annotations

from pathlib import Path

from lyapunov_nn_control_lab.result_provenance import discover_runs


KEY_FILES = [
    "README.md",
    "README.ja.md",
    "README.ko.md",
    "README.th.md",
    "Makefile",
    "pyproject.toml",
    "docs/en/index.md",
    "docs/ja/index.md",
    "docs/ko/index.md",
    "docs/th/index.md",
    "docs/ci_workflows.md",
    "docs/project_status.md",
    "docs/maintenance.md",
    "docs/git_workflow.md",
    "docs/onboarding.md",
    "src/lyapunov_nn_control_lab/finite_horizon_convergence.py",
    "src/lyapunov_nn_control_lab/experimental_seeds.py",
    "src/lyapunov_nn_control_lab/noise.py",
    "src/lyapunov_nn_control_lab/stability_ablation.py",
    "src/lyapunov_nn_control_lab/state_coordinates.py",
    "src/lyapunov_nn_control_lab/result_provenance.py",
    "tests/test_experimental_seeds.py",
    "tests/test_finite_horizon_convergence.py",
    "tests/test_state_coordinates.py",
    "scripts/run_checks.py",
    "scripts/check_environment.py",
    "scripts/list_results.py",
    "scripts/new_experiment_log.py",
    "scripts/quality_gate.py",
    "scripts/check_workflow_badges.py",
    "scripts/verify_run.py",
    ".github/workflows/quality-gate.yml",
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
    legacy_count = sum(
        1
        for path in Path("results").glob("*")
        if path.is_file() and path.name != "README.md"
    )
    runs = discover_runs(Path("results"))
    verified_runs = sum(bool(run["verified"]) for run in runs)
    print(f"- Legacy/unverified historical result files: {legacy_count}")
    print(f"- Provenance-aware runs: {len(runs)} ({verified_runs} verified)")

    print("")
    if missing:
        print(f"Status: needs attention. Missing key files: {missing}")
        return 1

    print("Status: ready for checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
