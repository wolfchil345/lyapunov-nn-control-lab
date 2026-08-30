🌐 言語: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# コマンド早見表

このページでは、Lyapunov Neural-Network Control Lab の実行と保守に役立つコマンドをまとめます。

## セットアップ

開発用ツールを含めてプロジェクトをインストールします。

```bash
python -m pip install -e ".[dev]"
```

## クイックスタート

初心者向けの小さな例を実行します。

```bash
python examples/quick_start.py
```

## ローカルチェックをすべて実行

テストとクイックスタートの例を実行します。

```bash
python scripts/run_checks.py
```

## テストのみを実行

```bash
python -m pytest
```

## メイン実験を実行

```bash
python main.py
```

## 生成結果を要約

```bash
python scripts/summarize_results.py
```

## provenance 対応 run を検証

```bash
python scripts/verify_run.py results/runs/<run_id>
```

## 不完全な staging ディレクトリを整理

```bash
python scripts/clean_results.py
```

## 現在の Git ブランチを確認

```bash
git branch --show-current
git status
```

## 新しい機能ブランチを開始

```bash
git switch main
git pull origin main
git switch -c feature/my-new-feature
```

## 機能ブランチをコミットして push

```bash
git add .
git commit -m "Describe the change"
git push -u origin feature/my-new-feature
```

## 機能ブランチを main にマージ

```bash
git switch main
git pull origin main
git merge --no-ff feature/my-new-feature
python scripts/run_checks.py
git push origin main
```

## Makefile ショートカット

このリポジトリには、よく使うコマンドのショートカットをまとめた `Makefile` があります。

```bash
make check-env
make checks
make test
make quickstart
make experiment
make clean
make summarize
make verify-run RUN_DIR=results/runs/<run_id>
```

## CI コマンド

GitHub Actions では `make checks` を使って、開発時と同じローカルチェックを実行します。
