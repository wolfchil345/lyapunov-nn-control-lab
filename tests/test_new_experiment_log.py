from __future__ import annotations

import importlib.util
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "new_experiment_log.py"

spec = importlib.util.spec_from_file_location("new_experiment_log", SCRIPT_PATH)
new_experiment_log = importlib.util.module_from_spec(spec)
assert spec is not None
assert spec.loader is not None
spec.loader.exec_module(new_experiment_log)


def test_slugify_keeps_safe_name_parts():
    assert new_experiment_log.slugify("Baseline Seed 0") == "baseline_seed_0"
    assert new_experiment_log.slugify("noise=0.05 / grid 21") == "noise_0_05_grid_21"


def test_slugify_uses_default_for_empty_text():
    assert new_experiment_log.slugify("!!!") == "experiment"


def test_create_log_from_template(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    docs_dir = Path("docs")
    docs_dir.mkdir()
    template_path = docs_dir / "experiment_log_template.md"
    template_path.write_text("# Template\n\n- Seed:\n", encoding="utf-8")

    output_path = new_experiment_log.create_log("Baseline Seed 0")

    assert output_path.parent == Path("results") / "experiment_logs"
    assert output_path.name.endswith("_baseline_seed_0.md")
    assert output_path.read_text(encoding="utf-8") == "# Template\n\n- Seed:\n"


def test_create_log_never_overwrites_same_timestamp_and_title(
    tmp_path,
    monkeypatch,
):
    monkeypatch.chdir(tmp_path)
    docs_dir = Path("docs")
    docs_dir.mkdir()
    (docs_dir / "experiment_log_template.md").write_text(
        "# Template\n",
        encoding="utf-8",
    )

    fixed_time = datetime(2026, 8, 7, 12, 34, 56, 123456)

    class FixedDatetime:
        @classmethod
        def now(cls):
            return fixed_time

    monkeypatch.setattr(new_experiment_log, "datetime", FixedDatetime)

    paths = [new_experiment_log.create_log("Same title") for _ in range(3)]

    assert len(set(paths)) == 3
    assert [path.name for path in paths] == [
        "20260807_123456_123456_same_title.md",
        "20260807_123456_123456_same_title_1.md",
        "20260807_123456_123456_same_title_2.md",
    ]
    assert all(path.read_text(encoding="utf-8") == "# Template\n" for path in paths)
