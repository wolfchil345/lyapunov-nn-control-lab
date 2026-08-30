🌐 言語: [English](../en/quality_gate.md) | [日本語](../ja/quality_gate.md) | [한국어](../ko/quality_gate.md) | [ไทย](../th/quality_gate.md)

# Quality Gate ガイド

quality gate は、マージ・発表・リリース・提出の前に行う最終的な準備完了チェックです。

## 実行内容

quality gate は次を実行します。

```bash
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/check_environment.py
python scripts/list_results.py
python scripts/check_docs_i18n_parity.py
python scripts/run_checks.py
```

これらのコマンドは、プロジェクト構成、環境の健全性、生成済み結果ファイル、4言語 i18n の構造的整合性、ドキュメントリンク、テスト、quick-start の実行を確認します。

## ローカルでの実行方法

次を実行します。

```bash
python scripts/quality_gate.py
```

または:

```bash
make quality-gate
```

## 実行するタイミング

次の前に quality gate を実行します。

- feature ブランチを `main` にマージする前。
- デモを行う前。
- 重要な結果を更新する前。
- レポートや発表資料を準備する前。
- リポジトリをポートフォリオ証拠として提出する前。

## 失敗の読み方

quality gate は最初に失敗したコマンドで停止します。

失敗したら、次の後に表示されたコマンドを読みます。

```text
Quality gate failed at:
```

そのコマンドだけを単独で実行すると、詳細なエラーを確認できます。

## よくある対処

### 環境の失敗

次を実行します。

```bash
python scripts/check_environment.py
```

Python パッケージ、PyTorch、またはプロジェクトファイルが不足していないか確認します。

### テストの失敗

次を実行します。

```bash
python -m pytest
```

quality gate 全体をやり直す前に、最初に失敗したテストを修正します。

### ドキュメントリンクの失敗

次を実行します。

```bash
python scripts/check_docs_links.py
```

不足している、または誤っているドキュメントリンクを修正します。

### 結果一覧の問題

次を実行します。

```bash
python scripts/list_results.py
```

生成ファイルが不足していないか、分かりにくくないか、不要ではないかを確認します。

## GitHub Actions

ワークフロー `.github/workflows/quality-gate.yml` は、`main` への push と pull request に対して quality gate を自動実行します。

## 最終ルール

重要な変更は、ローカルで quality gate が通るまでマージしないでください。

## workflow badge の失敗

次を実行します。

```bash
python scripts/check_workflow_badges.py
```

README に `tests.yml` と `quality-gate.yml` の badge が含まれていることを確認してください。
