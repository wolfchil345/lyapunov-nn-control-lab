from pathlib import Path

from scripts.check_i18n_docs import audit_repository, localized_filename


def test_localized_filename_uses_plain_english_name():
    assert localized_filename("README", "en") == "README.md"
    assert localized_filename("README", "ja") == "README.ja.md"


def test_audit_repository_reports_missing_language_trees(tmp_path):
    (tmp_path / "docs" / "en").mkdir(parents=True)
    (tmp_path / "docs" / "en" / "index.md").write_text(
        "🌐 Language: [English](../en/index.md) | [日本語](../ja/index.md) | "
        "[한국어](../ko/index.md) | [ไทย](../th/index.md)\n\n# Index\n",
        encoding="utf-8",
    )

    problems = audit_repository(tmp_path)

    assert any("docs/ja: missing index.md" in problem for problem in problems)
    assert any("README: missing languages" in problem for problem in problems)


def test_current_repository_passes_multilingual_audit():
    root = Path(__file__).resolve().parents[1]
    assert audit_repository(root) == []
