🌐 言語: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces設定

開発コンテナはPython 3.11を使用し、`requirements.txt` をインストールし、推奨拡張機能とpytestのテスト検出を設定します。

## 最初のコマンド

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## 開発ワークフロー

作業用ブランチを作成し、変更を明確な範囲に限定します。`make quality-gate` を実行してからコミット、プッシュ、pull requestを行います。生成図は、意図して保存する参照成果物の場合だけ追跡します。

追跡対象のbinary 成果物をcheckoutする前にGit LFSが必要です。Codespaceが不整合になった場合は、環境生成ファイルをコミットせずコンテナをrebuildしてください。
