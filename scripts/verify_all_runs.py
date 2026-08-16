"""Verify all committed provenance-aware runs under `results/runs/`.

This script iterates runs and invokes the project's `verify_run` helper to
ensure manifests and checksums are complete and valid.
"""

from __future__ import annotations

from pathlib import Path
import sys

from lyapunov_nn_control_lab.result_provenance import verify_run, RunValidationError


def main() -> int:
    runs_dir = Path("results") / "runs"
    if not runs_dir.exists():
        print("No runs directory found; nothing to verify.")
        return 0
    failures = []
    for run_dir in sorted(p for p in runs_dir.iterdir() if p.is_dir() and not p.name.startswith(".staging-")):
        try:
            result = verify_run(run_dir)
            print(f"Verified run {result.run_id}: {result.artifact_count} artifacts, commit={result.commit_sha}")
        except RunValidationError as exc:
            print(f"Run {run_dir.name} invalid: {exc}")
            failures.append(run_dir.name)
        except Exception as exc:  # pragma: no cover - be conservative
            print(f"Run {run_dir.name} error: {exc}")
            failures.append(run_dir.name)

    if failures:
        print(f"Runs with problems: {len(failures)}")
        return 2
    print("All committed runs verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
