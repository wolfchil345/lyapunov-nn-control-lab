🌐 言語: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# トラブルシューティング

## インポートまたはテストが失敗する

ターミナルがリポジトリのルートにあることを確認し、`.venv` を有効化して、`python -m pip install -e .` の後に `python -m pytest` を実行します。

## 図やCSVが古い

`git status` を確認し、追跡対象成果物をバックアップします。その後だけ `python scripts/clean_results.py` と `python main.py` を実行します。

## 数値が少し異なる

Pythonと依存関係のバージョン、固定シードを確認します。小さなプラットフォーム差はあり得ますが、大きな差は調査が必要です。

## 学習が遅い

環境設定の確認にはクイックスタートを使います。完全な実験には、学習、ロバスト性の網羅的な評価、引き込み領域のシミュレーションが含まれます。

## Git ブランチが分からない

`git status -sb` と `git branch --show-current` を実行します。環境ファイルや無関係な生成結果をコミットしないでください。

インストール固有の問題は[依存関係のトラブルシューティング](dependency_troubleshooting.md)を参照してください。
