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

## 4. Clean and regenerate important results

```bash
python scripts/clean_results.py
python main.py
python scripts/summarize_results.py
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
git tag v1.0.0
git push origin v1.0.0
```

Update the version number when creating later releases.
