🌐 言語: [English](../en/maintenance.md) | [日本語](../ja/maintenance.md) | [한국어](../ko/maintenance.md) | [ไทย](../th/maintenance.md)

# Maintenance Guide

このガイドは、新しい features、docs、tests、workflows を追加した後に project を健全に保つ方法を説明します。

## Routine maintenance checklist

`main` へ merge する前に、次の checklist を実行します。

```bash
python scripts/check_environment.py
python scripts/project_status.py
python scripts/check_workflow_badges.py
python scripts/quality_gate.py
make checks
```

## Weekly project check

実行:

```bash
git switch main
git pull origin main
python scripts/quality_gate.py
```

その後、次を確認します。

- GitHub Actions が通っている。
- README badges が表示されている。
- 重要 docs が `docs/{en,ja,ko,th}/index.md` 配下の適切な language index からリンクされている。
- 新しい scripts に可能な範囲で tests がある。
- 新しい重要ファイルが `scripts/project_status.py` に追跡対象として登録されている。

## After adding a new script

1. script を `scripts/` 配下に追加する。
2. script にロジックがある場合は `tests/` 配下に test を追加する。
3. コマンドを頻繁に使う場合は Makefile shortcut を追加する。
4. 利用者に説明が必要なら documentation を追加する。
5. core project structure の一部になる場合は `scripts/project_status.py` に追加する。

## After adding a new document

1. file を `docs/` 配下に配置する。
2. 適切な `docs/<language>/index.md` からリンクする。
3. 訪問者に重要な情報なら `README.md` からリンクする。
4. core guide なら `scripts/project_status.py` に追加する。

## After adding or changing a workflow

1. ローカルで quality gate を実行する。
2. workflow file が `.github/workflows/` 配下にあることを確認する。
3. 必要に応じて README badges を追加または更新する。
4. `python scripts/check_workflow_badges.py` を実行する。
5. Push して GitHub Actions が通ることを確認する。

## Before a demo or professor meeting

実行:

```bash
python scripts/quality_gate.py
python scripts/project_status.py
```

さらに README を開き、project goal、badges、docs、quick-start instructions が見つけやすいことを確認します。

## Portfolio note

保守された repository は一回限りの実験より強い価値を持ちます。この checklist は、project が安定し、文書化され、レビュー可能であることを示す助けになります。
