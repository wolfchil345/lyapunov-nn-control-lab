🌐 언어: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# 프로젝트 상태

실행:

```bash
python scripts/project_status.py
```

이 command는 주요 repository file을 확인하고 documentation, script, test, workflow, result artifact 수를 보고합니다. Inventory check이며 test나 과학적 review를 대신하지 않습니다.

## 사용 시점

- File 재구성 후.
- Pull request, demo, release 전.
- Documentation, script, test, workflow 추가 후.

새 file이 필수 요소가 되면 `scripts/project_status.py`의 `KEY_FILES`를 업데이트합니다. [Quality gate](quality_gate.md)는 더 넓은 validation sequence의 일부로 이 status command를 실행합니다.
