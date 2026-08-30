🌐 言語: [English](../en/ci_workflows.md) | [日本語](../ja/ci_workflows.md) | [한국어](../ko/ci_workflows.md) | [ไทย](../th/ci_workflows.md)

# CI ワークフローガイド

このプロジェクトでは、コード品質、ドキュメントの健全性、リポジトリの準備状況を確認するために GitHub Actions を使います。

## ワークフロー概要

### Python テスト

ファイル:

```text
.github/workflows/tests.yml
```

目的:

- Python テストスイートを実行する。
- 主要モジュールとスクリプトが引き続き動作することを確認する。
- 意図しないコード破損からプロジェクトを守る。

### Local checks (historical)

注: 以前の `local-checks` GitHub Actions ワークフローは active workflows から削除されています。ローカルの pre-push チェックは、ローカル検証用の `quality_gate` コマンドと `scripts/run_checks.py` で引き続き案内しています。

ローカル専用のワークフローを維持する場合は、共有の `.github/workflows/` ディレクトリに入れず、個人用ユーティリティであることを明確に記載して、利用者を混乱させないようにしてください。

### Quality gate

ファイル:

```text
.github/workflows/quality-gate.yml
```

目的:

- 最終的な準備完了チェックを実行する。
- project status、workflow badges、environment health、result inventory、tests、docs links、quick-start execution を確認する。

### CodeQL

ファイル:

```text
.github/workflows/codeql.yml
```

目的:

- セキュリティと信頼性の問題をコードスキャンする。
- このリポジトリを公開ポートフォリオとしてより安全にする。

## バッジ

README には workflow badge が含まれており、訪問者がプロジェクトの健全性をすぐ確認できます。

必要なバッジ:

- `tests.yml` 用の Python tests badge。
- `quality-gate.yml` 用の Quality gate badge。

バッジの有無は次で確認します。

```bash
python scripts/check_workflow_badges.py
```

## push 前のローカルコマンド

次を実行します。

```bash
python scripts/quality_gate.py
```

または:

```bash
make quality-gate
```

## 推奨マージルール

ブランチを `main` にマージする前に、ローカルで quality gate を実行し、push 後に GitHub Actions も通過することを確認します。

## ワークフローが失敗したとき

1. GitHub で失敗した workflow run を開く。
2. 最初に失敗した step を見つける。
3. 対応するローカルコマンドを実行する。
4. ローカルのエラーを修正する。
5. もう一度 push して Actions を再確認する。

## ポートフォリオ向けメモ

ワークフローが通ることは、このプロジェクトが単なる実験コードではなく、実際の研究ソフトウェアプロジェクトのようにテストされ、文書化され、保守されていることを示します。
