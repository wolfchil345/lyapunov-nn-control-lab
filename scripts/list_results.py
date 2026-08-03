from __future__ import annotations

import argparse
from pathlib import Path


def format_size(num_bytes: int) -> str:
    if num_bytes < 1024:
        return f"{num_bytes} B"
    if num_bytes < 1024 * 1024:
        return f"{num_bytes / 1024:.1f} KB"
    return f"{num_bytes / (1024 * 1024):.1f} MB"


def list_result_files(results_dir: Path) -> list[Path]:
    if not results_dir.exists():
        return []
    return sorted(path for path in results_dir.rglob("*") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="List generated result files.")
    parser.add_argument("--results-dir", default="results", help="Directory containing result files.")
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    files = list_result_files(results_dir)

    if not files:
        print(f"No result files found in {results_dir}.")
        return 0

    print(f"Result files in {results_dir}:")
    for path in files:
        size = format_size(path.stat().st_size)
        print(f"- {path.as_posix()} ({size})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
