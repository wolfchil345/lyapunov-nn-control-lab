🌐 言語: [English](../en/vscode.md) | [日本語](../ja/vscode.md) | [한국어](../ko/vscode.md) | [ไทย](../th/vscode.md)

# VS Code セットアップ

このガイドでは、VS Code または GitHub Codespaces でこのプロジェクトを使う方法を説明します。

## 推奨拡張機能

このリポジトリには、Python 開発と GitHub Actions 用の推奨拡張機能を定めた `.vscode/extensions.json` があります。

推奨拡張機能:

- Python
- Pylance
- GitHub Actions

## プロジェクトを開く

リポジトリのルートフォルダを VS Code で開いてください。ルートフォルダには `README.md`、`main.py`、`src/`、`tests/`、`scripts/` が含まれている必要があります。

## Python インタープリターを選択する

仮想環境を作成したら、VS Code で `.venv` のインタープリターを選択します。

## ターミナルからチェックを実行する

```bash
python scripts/run_checks.py
```

## VS Code からテストを実行する

このリポジトリには `.vscode/settings.json` があり、VS Code が `tests/` フォルダの pytest テストを検出できるようになっています。

## Codespaces に関する注意

Codespaces では、ターミナルを開いてローカルと同じコマンドを実行します。

```bash
python -m pip install -e ".[dev]"
python scripts/run_checks.py
```

## 一般的な作業手順

```bash
git switch main
git pull origin main
git switch -c feature/my-new-change
python scripts/run_checks.py
git status
```
