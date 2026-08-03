from pathlib import Path

from scripts.check_i18n_docs import (
    audit_repository,
    check_index_coverage,
    duplicate_suffix_files,
    localized_filename,
)


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


def test_check_index_coverage_reports_an_unlinked_document(tmp_path):
    index_path = tmp_path / "index.md"
    index_path.write_text(
        "# Index\n\n- [Guide](guide.md)\n",
        encoding="utf-8",
    )

    problems = check_index_coverage(
        index_path,
        {"index.md", "guide.md", "missing.md"},
    )

    assert problems == [f"{index_path}: missing index entries missing.md"]


def test_duplicate_suffix_files_finds_sync_conflict_copy(tmp_path):
    (tmp_path / "guide.md").write_text("# Guide\n", encoding="utf-8")
    duplicate = tmp_path / "guide 2.md"
    duplicate.write_text("# Guide\n", encoding="utf-8")

    assert duplicate_suffix_files(tmp_path) == [duplicate]


def test_current_repository_passes_multilingual_audit():
    root = Path(__file__).resolve().parents[1]
    assert audit_repository(root) == []
