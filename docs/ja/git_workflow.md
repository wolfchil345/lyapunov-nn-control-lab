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

Pull requestをopenし、required checkを待ち、conversationを解決し、protected `main` branch経由でmergeします。

## ルール

- 一つのbranchに一つの目的。
- 明示的なfileをstageし、生成artifactを別にreview。
- 明確な命令形commit messageを使用。
- `main` をforce-pushせず、published tagを書き換えず、secretやenvironment fileをcommitしない。
- `main` 同期後にmerge済みfeature branchを削除。
