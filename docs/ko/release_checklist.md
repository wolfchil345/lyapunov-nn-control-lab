🌐 언어: [English](../en/release_checklist.md) | [日本語](../ja/release_checklist.md) | [한국어](../ko/release_checklist.md) | [ไทย](../th/release_checklist.md)

# 릴리스 Checklist

1. Clean `main` branch를 동기화하고 `pyproject.toml`의 version 확인.
2. `python scripts/check_environment.py`, `make checks`, `make quality-gate` 실행.
3. Clean regeneration 전에 tracked result를 backup하고 모든 diff review.
4. 네 README, documentation index, release note, limitations, security guide review.
5. `git status -sb`, recent commit, tag가 local과 remote에 없는지 확인.
6. Release pull request를 merge하고 최종 `main`에서 gate 재실행.
7. Annotated tag를 만들고 그 tag만 push:

```bash
VERSION=vX.Y.Z
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"
```

Published version tag를 이동하거나 삭제하지 마십시오. 수정에는 새 patch version을 사용합니다.
