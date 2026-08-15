# Release Checklist

Use this checklist before creating a project release or submitting the repository for review.

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

Check README, docs index, release notes, methodology, results interpretation, limitations, and troubleshooting guides.

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

Update the version number when creating later releases.
