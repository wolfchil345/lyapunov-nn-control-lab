🌐 언어: [English](../en/project_status.md) | [日本語](../ja/project_status.md) | [한국어](../ko/project_status.md) | [ไทย](../th/project_status.md)

# 프로젝트 상태

다음을 실행하세요.

```bash
python scripts/project_status.py
```

이 명령은 주요 저장소 파일을 확인하고 문서, 스크립트, 테스트, workflow, 결과 산출물의 개수를 보고합니다. 이는 파일 구성 점검이며 테스트나 과학적 검토를 대신하지 않습니다.

## 사용 시점

- 파일 구조를 재정리한 후.
- pull request, 데모, 릴리스 전.
- 문서, 스크립트, 테스트, workflow를 추가한 후.

새 파일이 필수 항목이 되면 `scripts/project_status.py`의 `KEY_FILES`를 업데이트하세요. [품질 검사](quality_gate.md)는 더 넓은 검증 절차의 하나로 이 상태 명령을 실행합니다.
