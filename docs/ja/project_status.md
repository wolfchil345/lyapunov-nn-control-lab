🌐 言語: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# Project Status Guide

このガイドは project status checker の使い方を説明します。

## Purpose

project status checker は repository health の概要をすばやく確認するためのものです。

重要な files、folders、scripts、tests、workflows、documentation が存在することを確認できます。

## Command

実行:

```bash
python scripts/project_status.py
```

または:

```bash
make status
```

## What it checks

checker は重要な project files の存在を報告します。

例:

- Core documentation files.
- finite-horizon convergence evaluator とその regression tests.
- Important scripts.
- Test files.
- GitHub Actions workflow files.
- Legacy result files と manifest-verified provenance-aware runs.

各 provenance-aware run について、checker は run 数と、完全な artifact/checksum verification に合格した manifest 数を報告します。root-level historical files は、current manifest-backed runs とは分けて legacy/unverified として分類されます。

## When to run it

project status checker を実行するタイミング:

- 新機能を commit する前
- `main` へ merge する前
- 新しい documentation、scripts、tests、workflows を追加した後
- portfolio または研究成果として提示する前

## Relationship with the quality gate

quality gate は project status checker を自動で実行します。

実行:

```bash
python scripts/quality_gate.py
```

quality gate が project status step で失敗した場合は、`python scripts/project_status.py` を直接実行して不足項目を確認してください。

## How to update it

新しい重要ファイルが project structure の一部になったら、次の tracked file list に追加します。

```text
scripts/project_status.py
```

その後、次を実行します。

```bash
python scripts/project_status.py
python scripts/quality_gate.py
```

## Portfolio note

この script は、repository が単なる実験コードのフォルダではなく、保守された research software project として整理されていることを示すのに役立ちます。
