🌐 言語: [English](../en/troubleshooting.md) | [日本語](../ja/troubleshooting.md) | [한국어](../ko/troubleshooting.md) | [ไทย](../th/troubleshooting.md)

# トラブルシューティング

## Importまたはtestが失敗する

terminalがリポジトリのルートにあることを確認し、`.venv` を有効化し、`python -m pip install -e .` の後に `python -m pytest` を実行します。

## PlotやCSVが古い

`git status` を確認し、追跡対象artifactをbackupします。その後だけ `python scripts/clean_results.py` と `python main.py` を実行します。

## 数値が少し異なる

Python、dependency version、固定seedを確認します。小さなplatform差はあり得ますが、大きな差は調査が必要です。

## 学習が遅い

setup確認にはquick startを使います。完全な実験には学習、robustness sweep、region-of-attraction simulationが含まれます。

## Git branchが分からない

`git status -sb` と `git branch --show-current` を実行します。環境ファイルや無関係な生成結果をcommitしないでください。

インストール固有の問題は[依存関係のトラブルシューティング](dependency_troubleshooting.md)を参照してください。
