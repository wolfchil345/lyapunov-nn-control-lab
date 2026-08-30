🌐 言語: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# 環境セットアップ

このガイドでは、Lyapunov neural network control lab 用のローカル Python 環境を整える方法を説明します。

## 推奨 Python バージョン

Python 3.10 以降を使用してください。

## 仮想環境を作成する

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
```

## プロジェクトをインストールする

通常利用の場合:

```bash
python -m pip install -e .
```

開発、テスト、パッケージビルドの場合:

```bash
python -m pip install -e ".[dev]"
```

## ローカルチェックを実行する

```bash
python scripts/run_checks.py
```

このコマンドは、ドキュメントリンクの確認、単体テスト、クイックスタートの例を実行します。

## メイン実験を実行する

```bash
python main.py
```

## よくある問題

- import が失敗する場合は、リポジトリのルートからコマンドを実行しているか確認してください。
- 実行時パッケージが見つからない場合は、再度 `python -m pip install -e .` を実行してください。
- テストツールまたはビルドツールが見つからない場合は、`python -m pip install -e ".[dev]"` を実行してください。
- 生成結果が古く見える場合は、再実験の前に results ディレクトリを整理してください。

## 環境を確認する

Codespaces またはローカルマシンで依存関係の問題がある場合は、環境チェッカーを使用します。

```bash
python scripts/check_environment.py
```

これにより、Python、必要なプロジェクトファイル、インストール済みパッケージ、および宣言済みの実行時 import を確認します。
