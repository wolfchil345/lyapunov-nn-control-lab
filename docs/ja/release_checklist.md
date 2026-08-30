🌐 言語: [English](../en/release_checklist.md) | [日本語](../ja/release_checklist.md) | [한국어](../ko/release_checklist.md) | [ไทย](../th/release_checklist.md)

# Release Checklist

project release を作成する前、または repository を review 用に提出する前に、この checklist を使用してください。

## 1. Sync main

```bash
git switch main
git pull origin main
git status
```

## 2. Check environment

```bash
python scripts/check_environment.py
```

## 3. Run project checks

```bash
make checks
```

## 4. Generate and verify important results

```bash
python main.py
python scripts/list_results.py
python scripts/verify_run.py results/runs/<run_id>
```

## 5. Review documentation

README、docs index、release notes、methodology、results interpretation、limitations、troubleshooting guides を確認してください。

## 6. Review Git status

```bash
git status
git log --oneline -10
```

## 7. Tag release only after checks pass

```bash
VERSION=vX.Y.Z
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"
```

後続 release を作成する際は version number を更新してください。
