🌐 언어: [English](../en/maintenance.md) | [日本語](../ja/maintenance.md) | [한국어](../ko/maintenance.md) | [ไทย](../th/maintenance.md)

# 유지관리

## 정기 checklist

- 최신 `main` branch를 pull하고 open dependency update를 검토.
- `python scripts/project_status.py`와 `make quality-gate` 실행.
- Workflow badge와 네 documentation index 확인.
- 추적 result가 의도치 않게 재생성되지 않았는지 검토.
- 새 behavior 옆에 test를 추가하고 문서를 네 언어로 업데이트.

## 새 file 추가 후

- 필요한 경우 essential file을 `KEY_FILES`에 추가.
- User-facing document를 모든 localized index에서 연결.
- Script나 checker에 behavior가 추가되면 test 추가.

## Demo 또는 release 전

Clean branch를 사용하고 Git status, recent commit, limitations를 검토하며 표시 result가 현재 code와 release note에 일치하는지 확인합니다.

Historical tag를 삭제하거나 published release를 force-update하지 마십시오.
