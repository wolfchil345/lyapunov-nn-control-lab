🌐 言語: [English](../en/dependency_troubleshooting.md) | [日本語](../ja/dependency_troubleshooting.md) | [한국어](../ko/dependency_troubleshooting.md) | [ไทย](../th/dependency_troubleshooting.md)

# 依存関係のトラブルシューティング

まず次を実行します。

```bash
python scripts/check_environment.py
python -m pip check
```

## パッケージがない、またはPyTorchを読み込めない

`.venv`を有効にし、pipを更新してから `python -m pip install -e ".[dev]"` でプロジェクトを再インストールします。システムのPythonと仮想環境のパッケージを混在させないでください。

## パッケージ情報またはインポートのエラー

`python scripts/check_package.py` を実行します。失敗する場合は、開発用extra付きの編集可能プロジェクトを再インストールしてください。現在追跡している成果物にGit LFSは不要です。

## 環境を作り直す

システムのPythonを変更するのではなく、新しい仮想環境を作成します。Codespacesで環境の不整合が解消しない場合は、開発コンテナを再構築してください。

サポートを求める場合は、`python scripts/check_environment.py`、`python --version`、`python -m pip check` の出力を添えてください。
