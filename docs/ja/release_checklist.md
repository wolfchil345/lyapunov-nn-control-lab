🌐 言語: [English](../en/release_checklist.md) | [日本語](../ja/release_checklist.md) | [한국어](../ko/release_checklist.md) | [ไทย](../th/release_checklist.md)

# リリースチェックリスト

1. Cleanな `main` branchを同期し、`pyproject.toml` のversionを確認。
2. `python scripts/check_environment.py`、`make checks`、`make quality-gate` を実行。
3. Clean regeneration前にtracked resultをbackupし、全diffをreview。
4. 4つのREADME、documentation index、release note、limitations、security guideをreview。
5. `git status -sb`、recent commit、tagがlocalとremoteに存在しないことを確認。
6. Release pull requestをmergeし、最終 `main` でgateを再実行。
7. Annotated tagを作成し、そのtagだけをpush:

```bash
VERSION=vX.Y.Z
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"
```

Published version tagを移動または削除しません。修正には新しいpatch versionを使います。
