🌐 言語: [English](../en/release_checklist.md) | [日本語](../ja/release_checklist.md) | [한국어](../ko/release_checklist.md) | [ไทย](../th/release_checklist.md)

# リリースチェックリスト

1. クリーンな `main` ブランチを同期し、`pyproject.toml` のバージョンを確認。
2. `python scripts/check_environment.py`、`make checks`、`make quality-gate` を実行。
3. クリーン regeneration前にtracked 結果をバックアップし、全差分をレビュー。
4. 4つのREADME、ドキュメント 索引、リリース 注記、制約、セキュリティ guideをレビュー。
5. `git status -sb`、最近のコミット、ローカルとリモートに同名タグが存在しないことを確認する。
6. リリース プルリクエストをマージし、最終 `main` でゲートを再実行。
7. 注釈付きタグを作成し、そのタグだけをプッシュする:

```bash
VERSION=vX.Y.Z
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"
```

公開済みのバージョンタグを移動または削除してはいけません。修正には新しいパッチバージョンを使います。
