🌐 言語: [English](../en/onboarding.md) | [日本語](../ja/onboarding.md) | [한국어](../ko/onboarding.md) | [ไทย](../th/onboarding.md)

# オンボーディングガイド

## 最初の1時間

1. 日本語READMEと[プロジェクト概要](project_summary.md)を読みます。
2. [環境構築ガイド](environment.md)に従います。
3. `python examples/quick_start.py` を実行します。
4. `make checks` を実行し、`results/` を確認します。
5. [研究手法](methodology.md)、[実験ワークフロー](experiment_workflow.md)、[制約](limitations.md)を読みます。

## コード変更前

```bash
git switch main
git pull --ff-only origin main
git switch -c feature/short-description
```

科学的変更とドキュメント変更を分け、実験設定を記録し、review依頼前に `make quality-gate` を実行します。

完全な手順は[Gitワークフロー](git_workflow.md)と[コントリビューションガイド](../../CONTRIBUTING.ja.md)を参照してください。
