"""Provenance-aware, non-destructive scientific result runs."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
import csv
import hashlib
from importlib import metadata
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import uuid
from typing import Any


SCHEMA_VERSION = 1
PACKAGE_NAME = "lyapunov-nn-control-lab"
MANIFEST_NAME = "manifest.json"
CHECKSUMS_NAME = "SHA256SUMS"
RUN_ID_PATTERN = re.compile(
    r"^[A-Za-z0-9](?:[A-Za-z0-9._-]{0,126}[A-Za-z0-9])?$"
)


class RunValidationError(ValueError):
    """Raised when a run or manifest is incomplete, unsafe, or inconsistent."""


@dataclass(frozen=True, slots=True)
class GitProvenance:
    """Portable repository provenance without private filesystem paths."""

    available: bool
    commit_sha: str | None
    short_commit_sha: str | None
    branch: str | None
    dirty: bool | None


@dataclass(frozen=True, slots=True)
class RunContext:
    """Information available to one staging-directory producer."""

    run_id: str
    staging_dir: Path
    generated_at_utc: str
    git: GitProvenance
    package_version: str
    scientific_configuration: dict[str, Any]
    configuration_sha256: str


@dataclass(frozen=True, slots=True)
class RunVerification:
    """Successful verification summary for a completed run."""

    run_id: str
    commit_sha: str | None
    generated_at_utc: str
    artifact_count: int
    verified: bool = True


def validate_run_id(run_id: str) -> str:
    """Return one filesystem-safe, human-readable run identifier."""

    if not isinstance(run_id, str):
        raise TypeError("run_id must be a string.")
    if not RUN_ID_PATTERN.fullmatch(run_id):
        raise RunValidationError(
            "run_id must be 1-128 characters, start and end with an "
            "alphanumeric character, and contain only letters, digits, '.', "
            "'_', or '-'."
        )
    if run_id in {".", ".."}:
        raise RunValidationError("run_id must not be a traversal segment.")
    return run_id


def _run_git(repo_root: Path, *arguments: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", os.fspath(repo_root), *arguments],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def get_git_provenance(repo_root: Path) -> GitProvenance:
    """Read commit, branch, and dirty state; tolerate detached/no-git use."""

    repo_root = Path(repo_root)
    commit_sha = _run_git(repo_root, "rev-parse", "HEAD")
    if not commit_sha:
        return GitProvenance(False, None, None, None, None)

    branch = _run_git(repo_root, "symbolic-ref", "--quiet", "--short", "HEAD")
    status = _run_git(
        repo_root,
        "status",
        "--porcelain",
        "--untracked-files=normal",
    )
    return GitProvenance(
        available=True,
        commit_sha=commit_sha,
        short_commit_sha=commit_sha[:8],
        branch=branch or None,
        dirty=None if status is None else bool(status),
    )


def utc_timestamp() -> str:
    """Return an RFC 3339 UTC timestamp without local timezone information."""

    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def make_run_id(
    runs_dir: Path,
    *,
    generated_at_utc: str,
    short_commit_sha: str | None,
) -> str:
    """Create a timestamp/commit run ID with deterministic collision suffixes."""

    timestamp = generated_at_utc.replace("-", "").replace(":", "")
    timestamp = timestamp.replace("+00:00", "Z")
    commit = short_commit_sha or "nogit"
    base = validate_run_id(f"{timestamp}_{commit}")
    candidate = base
    index = 1
    while (Path(runs_dir) / candidate).exists():
        candidate = validate_run_id(f"{base}_{index:02d}")
        index += 1
    return candidate


def canonical_json_sha256(value: Mapping[str, Any]) -> str:
    """Hash scientific configuration independently of dictionary order."""

    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def sha256_file(path: Path) -> str:
    """Return the SHA-256 digest of one file using bounded reads."""

    digest = hashlib.sha256()
    with Path(path).open("rb") as input_file:
        for block in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _distribution_version(name: str) -> str:
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return "unavailable"


def environment_provenance() -> dict[str, Any]:
    """Return useful, privacy-safe runtime and dependency versions."""

    return {
        "python": {
            "implementation": platform.python_implementation(),
            "version": platform.python_version(),
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "dependencies": {
            "numpy": _distribution_version("numpy"),
            "scipy": _distribution_version("scipy"),
            "torch": _distribution_version("torch"),
            "matplotlib": _distribution_version("matplotlib"),
            "python-control": _distribution_version("control"),
        },
    }


def package_version() -> str:
    """Return the installed project version, or an explicit unavailable value."""

    return _distribution_version(PACKAGE_NAME)


def _artifact_role(path: Path) -> str:
    name = path.name
    if name == "report.md":
        return "human-readable experiment report"
    if path.suffix == ".png":
        return "scientific figure"
    if path.suffix == ".csv":
        if "summary" in name:
            return "aggregate data table"
        if "trial" in name:
            return "raw trial data table"
        return "scientific data table"
    if path.suffix in {".pt", ".pth"}:
        return "trained model state"
    if path.suffix == ".json":
        return "structured scientific data"
    return "scientific artifact"


def _csv_row_count(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        return max(sum(1 for _row in reader) - 1, 0)


def build_artifact_inventory(run_dir: Path) -> list[dict[str, Any]]:
    """Inventory actual run artifacts, excluding self-referential metadata."""

    run_dir = Path(run_dir)
    inventory: list[dict[str, Any]] = []
    for path in sorted(candidate for candidate in run_dir.rglob("*") if candidate.is_file()):
        relative = path.relative_to(run_dir).as_posix()
        if relative in {MANIFEST_NAME, CHECKSUMS_NAME}:
            continue
        record: dict[str, Any] = {
            "path": relative,
            "role": _artifact_role(path),
            "sha256": sha256_file(path),
            "size_bytes": path.stat().st_size,
        }
        if path.suffix == ".csv":
            record["row_count"] = _csv_row_count(path)
        inventory.append(record)
    if not inventory:
        raise RunValidationError("a completed run must contain artifacts.")
    return inventory


def _write_checksums(run_dir: Path, inventory: Sequence[Mapping[str, Any]]) -> None:
    lines = [f"{record['sha256']}  {record['path']}" for record in inventory]
    (Path(run_dir) / CHECKSUMS_NAME).write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def _validate_manifest_shape(manifest: Mapping[str, Any]) -> None:
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise RunValidationError(
            f"unsupported manifest schema version: {manifest.get('schema_version')!r}"
        )
    required = {
        "run_id",
        "status",
        "generated_at_utc",
        "git",
        "package",
        "environment",
        "scientific_configuration",
        "configuration_sha256",
        "generation_command",
        "expected_artifact_paths",
        "artifacts",
    }
    missing = sorted(required - set(manifest))
    if missing:
        raise RunValidationError(f"manifest is missing fields: {', '.join(missing)}")


def verify_run(run_dir: Path) -> RunVerification:
    """Verify manifest completeness, inventory, sizes, and SHA-256 checksums."""

    run_dir = Path(run_dir)
    manifest_path = run_dir / MANIFEST_NAME
    if not manifest_path.is_file():
        raise RunValidationError("completed run is missing manifest.json.")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RunValidationError("manifest.json is unreadable or invalid.") from exc
    _validate_manifest_shape(manifest)
    if manifest["status"] != "complete":
        raise RunValidationError("run manifest status is not complete.")
    validate_run_id(manifest["run_id"])

    artifacts = manifest["artifacts"]
    if not isinstance(artifacts, list) or not artifacts:
        raise RunValidationError("manifest artifact inventory must be nonempty.")
    expected = manifest["expected_artifact_paths"]
    recorded_paths = [record.get("path") for record in artifacts]
    if expected != recorded_paths:
        raise RunValidationError("expected artifact paths do not match inventory.")

    allowed = {MANIFEST_NAME, CHECKSUMS_NAME, *recorded_paths}
    actual = {
        path.relative_to(run_dir).as_posix()
        for path in run_dir.rglob("*")
        if path.is_file()
    }
    if actual != allowed:
        missing = sorted(allowed - actual)
        extra = sorted(actual - allowed)
        raise RunValidationError(
            f"run file set differs from manifest; missing={missing}, extra={extra}."
        )

    for record in artifacts:
        relative = record["path"]
        candidate = run_dir / relative
        try:
            candidate.resolve().relative_to(run_dir.resolve())
        except ValueError as exc:
            raise RunValidationError("artifact path escapes the run directory.") from exc
        if not candidate.is_file():
            raise RunValidationError(f"missing artifact: {relative}")
        if candidate.stat().st_size != record["size_bytes"]:
            raise RunValidationError(f"artifact size mismatch: {relative}")
        if sha256_file(candidate) != record["sha256"]:
            raise RunValidationError(f"artifact checksum mismatch: {relative}")

    checksum_lines = (run_dir / CHECKSUMS_NAME).read_text(encoding="utf-8").splitlines()
    expected_lines = [f"{record['sha256']}  {record['path']}" for record in artifacts]
    if checksum_lines != expected_lines:
        raise RunValidationError("SHA256SUMS does not match the manifest inventory.")
    git = manifest["git"]
    return RunVerification(
        run_id=manifest["run_id"],
        commit_sha=git.get("commit_sha"),
        generated_at_utc=manifest["generated_at_utc"],
        artifact_count=len(artifacts),
    )


def publish_run(
    producer: Callable[[RunContext], None],
    scientific_configuration: Mapping[str, Any],
    *,
    results_dir: Path = Path("results"),
    repo_root: Path = Path("."),
    run_id: str | None = None,
    allow_dirty: bool = False,
    official: bool = True,
    generation_command: str = "python main.py",
) -> Path:
    """Generate in staging, verify, then atomically publish one complete run."""

    results_dir = Path(results_dir)
    repo_root = Path(repo_root)
    git = get_git_provenance(repo_root)
    if official and not git.available:
        raise RunValidationError("official runs require an available Git checkout.")
    if git.dirty and not allow_dirty:
        raise RunValidationError(
            "refusing an official run from a dirty working tree; use --allow-dirty "
            "for an explicitly exploratory run."
        )

    generated_at = utc_timestamp()
    runs_dir = results_dir / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    resolved_id = validate_run_id(run_id) if run_id else make_run_id(
        runs_dir,
        generated_at_utc=generated_at,
        short_commit_sha=git.short_commit_sha,
    )
    final_dir = runs_dir / resolved_id
    if final_dir.exists():
        raise FileExistsError(f"run already exists: {resolved_id}")
    staging_dir = runs_dir / f".staging-{resolved_id}-{uuid.uuid4().hex[:8]}"
    staging_dir.mkdir(parents=False, exist_ok=False)

    configuration = json.loads(
        json.dumps(scientific_configuration, allow_nan=False)
    )
    configuration_sha256 = canonical_json_sha256(configuration)
    context = RunContext(
        run_id=resolved_id,
        staging_dir=staging_dir,
        generated_at_utc=generated_at,
        git=git,
        package_version=package_version(),
        scientific_configuration=configuration,
        configuration_sha256=configuration_sha256,
    )

    try:
        producer(context)
        inventory = build_artifact_inventory(staging_dir)
        _write_checksums(staging_dir, inventory)
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "run_id": resolved_id,
            "status": "complete",
            "run_kind": "official" if official and not git.dirty else "exploratory",
            "generated_at_utc": generated_at,
            "git": {
                "available": git.available,
                "commit_sha": git.commit_sha,
                "short_commit_sha": git.short_commit_sha,
                "branch": git.branch,
                "dirty": git.dirty,
            },
            "package": {"name": PACKAGE_NAME, "version": context.package_version},
            "environment": environment_provenance(),
            "normalized_coordinate_convention": configuration.get(
                "normalized_coordinate_convention"
            ),
            "scientific_configuration": configuration,
            "configuration_sha256": configuration_sha256,
            "generation_command": generation_command,
            "expected_artifact_paths": [record["path"] for record in inventory],
            "artifacts": inventory,
        }
        (staging_dir / MANIFEST_NAME).write_text(
            json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        verify_run(staging_dir)
        staging_dir.rename(final_dir)
        verify_run(final_dir)
    except BaseException:
        if staging_dir.exists() and not staging_dir.is_symlink():
            shutil.rmtree(staging_dir)
        raise
    return final_dir


def discover_runs(results_dir: Path) -> list[dict[str, Any]]:
    """Classify completed runs without treating legacy files as manifest runs."""

    runs_dir = Path(results_dir) / "runs"
    if not runs_dir.exists():
        return []
    records: list[dict[str, Any]] = []
    for run_dir in sorted(path for path in runs_dir.iterdir() if path.is_dir() and not path.name.startswith(".staging-")):
        try:
            verification = verify_run(run_dir)
            records.append(
                {
                    "run_id": verification.run_id,
                    "commit_sha": verification.commit_sha,
                    "generated_at_utc": verification.generated_at_utc,
                    "status": "complete",
                    "verified": True,
                    "artifact_count": verification.artifact_count,
                }
            )
        except (OSError, RunValidationError) as exc:
            records.append(
                {
                    "run_id": run_dir.name,
                    "commit_sha": None,
                    "generated_at_utc": None,
                    "status": "invalid",
                    "verified": False,
                    "artifact_count": 0,
                    "error": str(exc),
                }
            )
    return records
