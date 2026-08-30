🌐 言語: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# 依存関係のトラブルシューティング

このガイドでは、依存関係と環境に関するよくある問題の解決方法を説明します。

## 最初の診断コマンド

パッケージを変更する前に環境チェッカーを実行します。

```bash
python scripts/check_environment.py
```

## PyTorch の import エラー

PyTorch の import が shared library エラーで失敗する場合は、CPU wheel を再インストールします。

```bash
python -m pip uninstall -y torch torchvision torchaudio
python -m pip cache purge
python -m pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
python -c "import torch; print(torch.__version__)"
```

PyTorch を再インストールしたら、次を実行します。

```bash
python scripts/check_environment.py
python scripts/run_checks.py
```

## 依存関係をリセットする

仮想環境が乱れてきたら、作り直します。

```bash
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python scripts/run_checks.py
```

## Codespaces をリセットする

Codespaces の動作がおかしい場合は、Codespaces のコマンドパレットからコンテナーを再構築してください。

再構築後は次を実行します。

```bash
python scripts/check_environment.py
python scripts/run_checks.py
```

## 助けを求めるタイミング

それでもチェックが失敗する場合は、最初の FAIL 行から末尾までの端末出力をそのままコピーしてください。
