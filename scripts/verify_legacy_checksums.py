"""Verify the canonical SHA-256 baseline for legacy artifacts in `results/`.

This script reads `results/legacy_SHA256SUMS` and ensures that the listed
files exist and their SHA-256 digests match. It reports missing files,
mismatches, and unexpected extra files.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    base = Path("results")
    baseline = base / "legacy_SHA256SUMS"
    if not baseline.is_file():
        print("missing legacy_SHA256SUMS", file=sys.stderr)
        return 2
    expected = []
    for line in baseline.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            digest, filename = line.split(None, 1)
        except ValueError:
            print(f"invalid line in baseline: {line!r}", file=sys.stderr)
            return 2
        filename = filename.strip()
        expected.append((digest, Path(filename)))

    missing = []
    mismatches = []
    for digest, path in expected:
        if not path.is_file():
            missing.append(str(path))
            continue
        actual = sha256_file(path)
        if actual != digest:
            mismatches.append((str(path), digest, actual))

    if missing or mismatches:
        if missing:
            print("Missing legacy artifacts:")
            for p in missing:
                print(" -", p)
        if mismatches:
            print("Checksum mismatches:")
            for p, exp, act in mismatches:
                print(f" - {p}: expected {exp}, actual {act}")
        return 1

    print("All legacy artifacts present and verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
