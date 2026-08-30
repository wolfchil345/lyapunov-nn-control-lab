🌐 言語: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# Git ワークフローガイド

このガイドでは、このプロジェクトで使っているブランチ運用を説明します。

## 基本ルール

`main` で直接作業しないでください。

feature ブランチを作成し、1 つの焦点を絞った改善を行い、テストしてから `main` にマージします。

## 標準的なブランチの流れ

```bash
git switch main
git pull origin main
git switch -c feature/example-name
```

ファイルを編集した後は、次のチェックを実行します。

```bash
python scripts/check_environment.py
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/quality_gate.py
make checks
```

コミットして push します。

```bash
git add path/to/changed_file.md
git commit -m "Describe the focused change"
git push -u origin feature/example-name
```

`main` にマージします。

```bash
git switch main
git pull origin main
git merge --no-ff feature/example-name
python scripts/quality_gate.py
make checks
git push origin main
```

feature ブランチを削除します。

```bash
git branch -d feature/example-name
git push origin --delete feature/example-name
```

## ブランチ名の付け方

目的が分かる短い名前を使います。

- `feature/add-new-guide`
- `feature/test-new-script`
- `feature/status-new-file`
- `feature/update-quality-gate`

## コミットメッセージの付け方

明確な動作を表すフレーズを使います。

- `Add maintenance guide`
- `Track maintenance guide in project status`
- `Add workflow badge checker tests`

## Git が commit するものがないと言うとき

Git が commit するものがないと言う場合、変更はすでにコミット済みかもしれません。

次を実行します。

```bash
git status
git log --oneline -5
```

正しいコミットがあるなら、そのブランチを push します。

```bash
git push -u origin feature/example-name
```

## ポートフォリオ向けメモ

このワークフローは、このプロジェクトが慎重なバージョン管理、分離された変更、再現可能なチェックで保守されていることを示します。
