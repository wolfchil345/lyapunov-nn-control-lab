
from scripts.check_docs_links import check_file, markdown_files


def test_markdown_files_scans_nested_and_root_files(tmp_path):
    (tmp_path / "README.md").write_text("# Root\n", encoding="utf-8")
    nested = tmp_path / "docs" / "ja"
    nested.mkdir(parents=True)
    (nested / "guide.md").write_text("# Guide\n", encoding="utf-8")
    ignored = tmp_path / ".venv"
    ignored.mkdir()
    (ignored / "ignored.md").write_text("[missing](no.md)\n", encoding="utf-8")

    files = markdown_files(tmp_path)

    assert [path.relative_to(tmp_path).as_posix() for path in files] == [
        "README.md",
        "docs/ja/guide.md",
    ]


def test_check_file_validates_links_images_and_unicode_anchors(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    target = docs / "target.md"
    target.write_text("# 日本語の見出し\n", encoding="utf-8")
    image = tmp_path / "plot.png"
    image.write_bytes(b"png")
    source = tmp_path / "README.md"
    source.write_text(
        "[section](docs/target.md#日本語の見出し)\n"
        "![plot](plot.png)\n"
        "[external](https://example.com)\n",
        encoding="utf-8",
    )

    assert check_file(source, tmp_path) == []


def test_check_file_reports_missing_target_anchor_and_escape(tmp_path):
    target = tmp_path / "target.md"
    target.write_text("# Existing\n", encoding="utf-8")
    source = tmp_path / "README.md"
    source.write_text(
        "[missing](missing.md)\n"
        "[anchor](target.md#absent)\n"
        "[escape](../outside.md)\n",
        encoding="utf-8",
    )

    problems = check_file(source, tmp_path)

    assert any("missing missing.md" in problem for problem in problems)
    assert any("missing anchor #absent" in problem for problem in problems)
    assert any("target leaves repository" in problem for problem in problems)
