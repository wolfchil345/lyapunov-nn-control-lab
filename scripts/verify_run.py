"""Verify one provenance-aware scientific result run."""

from __future__ import annotations

import argparse
from pathlib import Path

from lyapunov_nn_control_lab.result_provenance import verify_run


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    result = verify_run(args.run_dir)
    print(
        f"Verified run {result.run_id}: {result.artifact_count} artifacts, "
        f"commit={result.commit_sha}, generated={result.generated_at_utc}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
