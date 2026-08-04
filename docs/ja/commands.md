🌐 言語: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# コマンドガイド

## セットアップと診断

```bash
python -m pip install -e ".[dev]"
python scripts/check_environment.py
```

## 実行と検証

```bash
python examples/quick_start.py
python main.py
python -m pytest
make lint
make checks
make quality-gate
```

## 結果

```bash
python scripts/list_results.py
python scripts/summarize_results.py
python scripts/new_experiment_log.py "short description" --language ja
```

`python scripts/clean_results.py` は既知の生成ファイルを一覧表示するドライランです。一覧を確認してから `python scripts/clean_results.py --yes` を使用してください。未知のファイルと実験ログのディレクトリは保持されます。

## Git

```bash
git status -sb
git switch -c feature/short-description
git add <files>
git commit -m "Describe the change"
git push -u origin feature/short-description
```
