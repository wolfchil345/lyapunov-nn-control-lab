🌐 언어: [English](../en/release_checklist.md) | [日本語](../ja/release_checklist.md) | [한국어](../ko/release_checklist.md) | [ไทย](../th/release_checklist.md)

# 릴리스 체크리스트

1. 깨끗한 `main` 브랜치를 동기화하고 `pyproject.toml`의 버전 확인.
2. `python scripts/check_environment.py`, `make checks`, `make quality-gate` 실행.
3. 결과를 새로 생성하기 전에 추적 중인 결과를 백업하고 모든 차이를 검토함.
4. 4개 언어의 README, 문서 색인, 릴리스 노트, 한계, 보안 안내를 검토함.
5. `git status -sb`, 최근 커밋, 로컬과 원격에 동일한 태그가 없는지 확인.
6. 릴리스 풀 리퀘스트를 병합하고 최종 `main`에서 게이트 재실행.
7. 주석 태그를 만들고 그 태그만 푸시:

```bash
VERSION=vX.Y.Z
git tag -a "$VERSION" -m "Release $VERSION"
git push origin "$VERSION"
```

공개된 버전 태그를 이동하거나 삭제하지 마세요. 수정할 때는 새 패치 버전을 사용합니다.
