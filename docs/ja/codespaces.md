🌐 言語: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces設定

dev containerはPython 3.11を使用し、`requirements.txt` をインストールし、推奨拡張機能とpytest discoveryを設定します。

## 最初のコマンド

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## 開発ワークフロー

feature branchを作成し、変更を限定して、`make quality-gate` を実行し、commit、push、pull requestを行います。生成図は意図したreference artifactの場合だけ保存します。

追跡対象のbinary assetをcheckoutする前にGit LFSが必要です。Codespaceが不整合になった場合は、環境生成ファイルをcommitせずcontainerをrebuildしてください。
