🌐 言語: [English](../en/environment.md) | [日本語](../ja/environment.md) | [한국어](../ko/environment.md) | [ไทย](../th/environment.md)

# 環境構築

## 要件

- Python 3.10以上。CIではPython 3.10と3.12をテストします。
- Git。現在追跡しているバイナリ成果物は通常のGitを使用し、Git LFSは不要です。
- 同梱されている実験はCPUで実行できます。

## インストール

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows PowerShellでは `.venv\Scripts\Activate.ps1` で仮想環境を有効にします。

## 環境の確認

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

コマンドはリポジトリのルートで実行してください。インポートに失敗する場合は、`.venv`を再度有効にし、`python -m pip install -e ".[dev]"` で再インストールします。
