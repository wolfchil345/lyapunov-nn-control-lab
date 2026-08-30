🌐 言語: [English](../en/onboarding.md) | [日本語](../ja/onboarding.md) | [한국어](../ko/onboarding.md) | [ไทย](../th/onboarding.md)

# 導入ガイド

このガイドは、新しい利用者がプロジェクトを始めるための手順を案内します。

## 対象読者

初めてリポジトリを開く場合、ポートフォリオ用のプロジェクトとして確認する場合、あるいは実験を実行する準備をする場合にこのガイドを使ってください。

## 1. プロジェクトを開く

推奨 विकल्प:

- ブラウザベースの開発には GitHub Codespaces。
- ローカル開発には VS Code。

## 2. 環境を確認する

次を実行します。

```bash
python scripts/check_environment.py
```

これにより、Python と主要な依存関係が利用可能であることを確認します。

## 3. クイックスタートを実行する

次を実行します。

```bash
python examples/quick_start.py
```

この quick start の例で、主要なプロジェクトモジュールが import でき、実行できることを確認します。

## 4. テストを実行する

次を実行します。

```bash
python -m pytest
```

または:

```bash
make test
```

## 5. quality gate を実行する

次を実行します。

```bash
python scripts/quality_gate.py
```

または:

```bash
make quality-gate
```

quality gate では、リポジトリの状態、workflow badge、環境の健全性、結果一覧、4言語 i18n の構造的整合性、テスト、docs リンク、quick start の実行を確認します。

## 6. 主要なドキュメントを読む

最初に読むことを勧めるドキュメント:

- `project_summary.md` はプロジェクト全体の概要。
- `methodology.md` は制御と学習の手法。
- `experiment_workflow.md` は実験の流れ。
- `results_interpretation.md` は出力の読み方。
- `git_workflow.md` はブランチとマージのルール。
- `maintenance.md` は定期点検。

## 7. 変更する前に

feature ブランチを作成します。

```bash
git switch main
git pull origin main
git switch -c feature/example-name
```

編集後は次を実行します。

```bash
python scripts/quality_gate.py
make checks
```

## ポートフォリオ向けメモ

この導入ガイドは、リポジトリが他の人にとって理解し、実行し、確認し、拡張できる状態にあることを示すのに役立ちます。
