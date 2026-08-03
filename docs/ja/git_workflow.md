🌐 言語: [English](../en/git_workflow.md) | [日本語](../ja/git_workflow.md) | [한국어](../ko/git_workflow.md) | [ไทย](../th/git_workflow.md)

# Gitワークフロー

## 標準フロー

```bash
git switch main
git pull --ff-only origin main
git switch -c docs/short-description
# edit and validate
git status -sb
git diff --check
make quality-gate
git add <intentional-files>
git commit -m "Describe the change"
git push -u origin docs/short-description
```

プルリクエストを作成し、必須チェックの完了を待ち、未解決の会話を解消してから、保護された `main` ブランチへマージします。

## ルール

- 一つのブランチに一つの目的。
- 明示的なファイルを段階し、生成成果物を別にレビュー。
- 明確な命令形コミット メッセージを使用。
- `main` への強制プッシュ、公開済みタグの書き換え、機密情報や環境ファイルのコミットは行わない。
- `main` を同期した後、マージ済みの作業ブランチを削除する。
