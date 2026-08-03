🌐 Language: [English](../en/release_checklist.md) | [日本語](../ja/release_checklist.md) | [한국어](../ko/release_checklist.md) | [ไทย](../th/release_checklist.md)

# Release Checklist

1. Synchronize a clean `main` branch and confirm the intended version in `pyproject.toml`.
2. Run `python scripts/check_environment.py`, `make checks`, and `make quality-gate`.
3. Back up tracked results before clean regeneration; review every resulting diff.
4. Review all four READMEs, documentation indexes, release notes, limitations, and security guidance.
5. Confirm `git status -sb`, recent commits, and that the tag does not already exist locally or remotely.
6. Merge the release pull request and rerun the gate on final `main`.
7. Create an annotated tag and push only that tag:

```bash
VERSION=vX.Y.Z
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"
```

Never move or delete a published version tag. Use a new patch version for corrections.
