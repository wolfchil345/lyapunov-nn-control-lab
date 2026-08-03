🌐 言語: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# 環境構築

## 必要条件

- Python 3.10以降。CIではPython 3.11と3.12を使用します。
- Git、および追跡対象のバイナリ資産にはGit LFS。
- 収録実験はCPUで実行できます。

## インストール

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Windows PowerShellでは `.venv\Scripts\Activate.ps1` を使用します。

## 環境の確認

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

コマンドはリポジトリのルートで実行してください。importに失敗する場合は `.venv` を再度有効化し、`python -m pip install -e .` を実行します。
