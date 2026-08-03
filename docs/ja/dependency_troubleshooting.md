🌐 言語: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# 依存関係のトラブルシューティング

最初に次を実行します。

```bash
python scripts/check_environment.py
python -m pip check
```

## Package不足またはPyTorch import error

`.venv` を有効化し、pipをupgradeし、`python -m pip install -e .` で再installします。system Pythonとvirtual environmentのpackageを混在させないでください。

## Git LFS error

Git LFSをinstallし、`git lfs install` と `git lfs pull` を実行して追跡対象binary assetを復元します。

## Clean reset

system interpreterを変更せず、新しいvirtual environmentを作ります。Codespacesで不整合が続く場合はdev containerをrebuildします。

相談時には `python scripts/check_environment.py`、`python --version`、`python -m pip check` の出力を添えてください。
