from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_pytest_has_one_canonical_configuration():
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")

    assert "[tool.pytest.ini_options]" in pyproject
    assert not (ROOT / "pytest.ini").exists()


def test_provenance_run_models_are_not_ignored():
    rules = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()

    assert rules.index("*.pt") < rules.index("!results/runs/**/*.pt")
    assert rules.index("*.pth") < rules.index("!results/runs/**/*.pth")
