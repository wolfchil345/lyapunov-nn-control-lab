🌐 언어: [English](../en/maintenance.md) | [日本語](../ja/maintenance.md) | [한국어](../ko/maintenance.md) | [ไทย](../th/maintenance.md)

# 유지관리

## 정기 체크리스트

- 최신 `main` 브랜치를 pull하고 생성 의존성 update를 검토.
- `python scripts/project_status.py`와 `make quality-gate` 실행.
- 워크플로 badge와 네 문서 색인 확인.
- 추적 결과가 의도치 않게 재생성되지 않았는지 검토.
- 새 거동 옆에 테스트를 추가하고 문서를 네 언어로 업데이트.

## 새 파일 추가 후

- 필요한 경우 필수 파일을 `KEY_FILES`에 추가.
- 사용자용 문서를 모든 언어별 색인에서 연결.
- Script나 checker에 거동가 추가되면 테스트 추가.

## 데모 또는 릴리스 전

작업 트리가 깨끗한 브랜치를 사용하고 Git 상태, 최근 커밋, 제약 사항을 검토하세요. 표시되는 결과가 현재 코드와 릴리스 노트와 일치하는지도 확인합니다.

과거 태그를 삭제하거나 공개된 릴리스를 강제로 덮어쓰지 마세요.
