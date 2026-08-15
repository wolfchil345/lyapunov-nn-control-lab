from __future__ import annotations

import json
from pathlib import Path

import pytest

import lyapunov_nn_control_lab.result_provenance as provenance
from lyapunov_nn_control_lab.result_provenance import (
    GitProvenance,
    RunValidationError,
    canonical_json_sha256,
    discover_runs,
    get_git_provenance,
    make_run_id,
    publish_run,
    validate_run_id,
    verify_run,
)


CLEAN_GIT = GitProvenance(
    available=True,
    commit_sha="a" * 40,
    short_commit_sha="a" * 8,
    branch="fix/result-provenance",
    dirty=False,
)


def configuration() -> dict:
    return {
        "normalized_coordinate_convention": {
            "identifier": "normalized dimensionless second-order coordinates"
        },
        "plant": {"mass": 1.0, "A": [[0.0, 1.0], [-2.0, -0.4]]},
        "stability_weight_ablation": {
            "weights": [0.0, 10.0],
            "seeds": [700, 701],
            "repeat_count": 2,
            "pairing_strategy": "paired seeds across all stability weights",
        },
        "measurement_noise": {
            "noise_levels": [0.0, 0.1],
            "seeds": [7, 8],
            "repeat_count": 2,
            "pairing_strategy": (
                "common random-number realizations across noise amplitudes"
            ),
        },
    }


def producer_with_value(value: str):
    def producer(context):
        (context.staging_dir / "report.md").write_text(
            f"# Run {context.run_id}\n\nvalue={value}\n",
            encoding="utf-8",
        )
        (context.staging_dir / "trials.csv").write_text(
            f"seed,value\n7,{value}\n8,{value}\n",
            encoding="utf-8",
        )

    return producer


def publish_fake_run(tmp_path, monkeypatch, *, run_id="run-001", value="one"):
    monkeypatch.setattr(provenance, "get_git_provenance", lambda _root: CLEAN_GIT)
    monkeypatch.setattr(provenance, "package_version", lambda: "1.0.1")
    return publish_run(
        producer_with_value(value),
        configuration(),
        results_dir=tmp_path / "results",
        repo_root=tmp_path,
        run_id=run_id,
        generation_command="python main.py --run-id controlled-run",
    )


@pytest.mark.parametrize(
    "run_id",
    ["run-001", "20260808T010203Z_deadbeef", "a.b_c-9"],
)
def test_validate_run_id_accepts_portable_ids(run_id):
    assert validate_run_id(run_id) == run_id


@pytest.mark.parametrize(
    "run_id",
    ["../escape", "a/b", "a\\b", ".hidden", "trailing-", "", "a" * 129],
)
def test_validate_run_id_rejects_malformed_or_traversal_ids(run_id):
    with pytest.raises(RunValidationError):
        validate_run_id(run_id)


def test_make_run_id_adds_collision_suffix(tmp_path):
    runs_dir = tmp_path / "runs"
    runs_dir.mkdir()
    first = make_run_id(
        runs_dir,
        generated_at_utc="2026-08-08T01:02:03Z",
        short_commit_sha="deadbeef",
    )
    (runs_dir / first).mkdir()
    second = make_run_id(
        runs_dir,
        generated_at_utc="2026-08-08T01:02:03Z",
        short_commit_sha="deadbeef",
    )
    assert first == "20260808T010203Z_deadbeef"
    assert second == "20260808T010203Z_deadbeef_01"


def test_configuration_digest_is_independent_of_dictionary_order():
    left = {"b": [2, 3], "a": {"y": 2, "x": 1}}
    right = {"a": {"x": 1, "y": 2}, "b": [2, 3]}
    assert canonical_json_sha256(left) == canonical_json_sha256(right)


def test_git_provenance_handles_detached_and_missing_git(monkeypatch, tmp_path):
    def detached(_root, *args):
        if args == ("rev-parse", "HEAD"):
            return "b" * 40
        if args[0] == "status":
            return ""
        return None

    monkeypatch.setattr(provenance, "_run_git", detached)
    result = get_git_provenance(tmp_path)
    assert result.available and result.branch is None and result.dirty is False

    monkeypatch.setattr(provenance, "_run_git", lambda *_args: None)
    assert get_git_provenance(tmp_path) == GitProvenance(
        False, None, None, None, None
    )


def test_official_run_rejects_dirty_or_missing_git(tmp_path, monkeypatch):
    for git in (
        GitProvenance(True, "a" * 40, "a" * 8, "main", True),
        GitProvenance(False, None, None, None, None),
    ):
        monkeypatch.setattr(provenance, "get_git_provenance", lambda _root, git=git: git)
        with pytest.raises(RunValidationError):
            publish_run(
                producer_with_value("x"),
                configuration(),
                results_dir=tmp_path / git.short_commit_sha if git.short_commit_sha else tmp_path / "nogit",
                repo_root=tmp_path,
                run_id="blocked-run",
            )


def test_dirty_run_is_explicitly_exploratory_when_allowed(tmp_path, monkeypatch):
    dirty_git = GitProvenance(True, "c" * 40, "c" * 8, "feature", True)
    monkeypatch.setattr(provenance, "get_git_provenance", lambda _root: dirty_git)
    run_dir = publish_run(
        producer_with_value("dirty"),
        configuration(),
        results_dir=tmp_path / "results",
        repo_root=tmp_path,
        run_id="dirty-run",
        allow_dirty=True,
    )
    manifest = json.loads((run_dir / "manifest.json").read_text())
    assert manifest["git"]["dirty"] is True
    assert manifest["run_kind"] == "exploratory"


def test_manifest_inventory_seed_provenance_and_checksums(tmp_path, monkeypatch):
    run_dir = publish_fake_run(tmp_path, monkeypatch)
    verification = verify_run(run_dir)
    manifest_text = (run_dir / "manifest.json").read_text()
    manifest = json.loads(manifest_text)

    assert verification.verified and verification.artifact_count == 2
    assert manifest["schema_version"] == 1
    assert manifest["status"] == "complete"
    assert manifest["package"] == {
        "name": "lyapunov-nn-control-lab",
        "version": "1.0.1",
    }
    assert manifest["scientific_configuration"]["stability_weight_ablation"][
        "seeds"
    ] == [700, 701]
    assert manifest["scientific_configuration"]["measurement_noise"]["seeds"] == [7, 8]
    csv_record = next(record for record in manifest["artifacts"] if record["path"] == "trials.csv")
    assert csv_record["row_count"] == 2
    assert len(csv_record["sha256"]) == 64
    assert "/Users/" not in manifest_text
    assert str(tmp_path) not in manifest_text


def test_missing_tampered_incomplete_and_extra_runs_are_rejected(tmp_path, monkeypatch):
    run_dir = publish_fake_run(tmp_path, monkeypatch)
    (run_dir / "trials.csv").write_text("tampered\n", encoding="utf-8")
    with pytest.raises(RunValidationError, match="size mismatch|checksum mismatch"):
        verify_run(run_dir)

    run_dir = publish_fake_run(tmp_path, monkeypatch, run_id="run-002")
    (run_dir / "report.md").unlink()
    with pytest.raises(RunValidationError, match="file set differs|missing artifact"):
        verify_run(run_dir)

    run_dir = publish_fake_run(tmp_path, monkeypatch, run_id="run-003")
    manifest_path = run_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["status"] = "incomplete"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(RunValidationError, match="not complete"):
        verify_run(run_dir)

    run_dir = publish_fake_run(tmp_path, monkeypatch, run_id="run-004")
    (run_dir / "unexpected.txt").write_text("extra", encoding="utf-8")
    with pytest.raises(RunValidationError, match="file set differs"):
        verify_run(run_dir)


def test_failure_cleans_only_staging_and_preserves_previous_run(tmp_path, monkeypatch):
    previous = publish_fake_run(tmp_path, monkeypatch)
    previous_manifest = (previous / "manifest.json").read_bytes()

    def failing(context):
        (context.staging_dir / "partial.csv").write_text("x\n", encoding="utf-8")
        raise RuntimeError("injected mid-run failure")

    with pytest.raises(RuntimeError, match="injected mid-run failure"):
        publish_run(
            failing,
            configuration(),
            results_dir=tmp_path / "results",
            repo_root=tmp_path,
            run_id="failed-run",
        )

    assert (previous / "manifest.json").read_bytes() == previous_manifest
    assert verify_run(previous).verified
    assert not (tmp_path / "results" / "runs" / "failed-run").exists()
    assert not list((tmp_path / "results" / "runs").glob(".staging-*"))


def test_two_runs_never_mix_artifacts(tmp_path, monkeypatch):
    first = publish_fake_run(tmp_path, monkeypatch, run_id="run-one", value="one")
    second = publish_fake_run(tmp_path, monkeypatch, run_id="run-two", value="two")
    assert "value=one" in (first / "report.md").read_text()
    assert "value=two" in (second / "report.md").read_text()
    assert (first / "trials.csv").read_bytes() != (second / "trials.csv").read_bytes()
    assert verify_run(first).verified and verify_run(second).verified


def test_unsupported_manifest_schema_and_legacy_classification(tmp_path, monkeypatch):
    results_dir = tmp_path / "results"
    results_dir.mkdir()
    (results_dir / "historical.png").write_bytes(b"legacy")
    run_dir = publish_fake_run(tmp_path, monkeypatch)
    manifest_path = run_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["schema_version"] = 999
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(RunValidationError, match="unsupported"):
        verify_run(run_dir)
    runs = discover_runs(results_dir)
    assert runs[0]["verified"] is False
    assert (results_dir / "historical.png").read_bytes() == b"legacy"
