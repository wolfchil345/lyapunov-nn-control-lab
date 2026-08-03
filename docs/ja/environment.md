🌐 言語: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# 環境構築

## 要件

- Python 3.10以上。CIではPython 3.11と3.12を使用します。
- Git。追跡対象のバイナリ成果物を扱う場合はGit LFSも必要です。
- 同梱されている実験はCPUで実行できます。

## インストール

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Windows PowerShellでは `.venv\Scripts\Activate.ps1` で仮想環境を有効にします。

## 環境の確認

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

コマンドはリポジトリのルートで実行してください。インポートに失敗する場合は、`.venv`を再度有効にし、`python -m pip install -e .` で再インストールします。
