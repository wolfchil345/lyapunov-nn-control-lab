🌐 言語: [English](../en/commands.md) | [日本語](../ja/commands.md) | [한국어](../ko/commands.md) | [ไทย](../th/commands.md)

# コマンドガイド

## セットアップと診断

```bash
python -m pip install -e .
python scripts/check_environment.py
```

## 実行と検証

```bash
python examples/quick_start.py
python main.py
python -m pytest
make checks
make quality-gate
```

## 結果

```bash
python scripts/list_results.py
python scripts/summarize_results.py
python scripts/new_experiment_log.py "short description" --language ja
```

`python scripts/clean_results.py` は `results/` 内の全ファイルを削除します。保存する参照 成果物は先にバックアップしてください。

## Git

```bash
git status -sb
git switch -c feature/short-description
git add <files>
git commit -m "Describe the change"
git push -u origin feature/short-description
```
