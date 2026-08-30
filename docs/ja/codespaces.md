🌐 言語: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces セットアップ

このガイドでは、GitHub Codespaces でこのリポジトリを使う方法を説明します。

## 目的

このリポジトリには `.devcontainer/devcontainer.json` が含まれており、Codespaces が Python の開発環境を自動的に準備できるようになっています。

## 開発コンテナーの動作

- Python 3.11 を使用します。
- Codespace 作成後に、`pyproject.toml` からパッケージ本体と開発依存関係をインストールします。
- Python、Pylance、GitHub Actions の拡張機能を推奨します。
- `tests/` フォルダから pytest のテスト検出を有効にします。

## Codespaces を開いた直後の最初のコマンド

```bash
python scripts/run_checks.py
```

## 実験を実行する

```bash
python main.py
```

## 通常の Git ワークフロー

```bash
git switch main
git pull origin main
git switch -c feature/my-change
python scripts/run_checks.py
git status
```
