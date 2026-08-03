🌐 언어: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# 의존성 업데이트

Dependabot은 설정된 일정에 따라 Python package와 GitHub Actions를 확인합니다.

## Review checklist

1. upstream release note를 읽고 breaking change를 찾습니다.
2. 한 번에 한 dependency group만 업데이트합니다.
3. `python -m pip check`, `make checks`, `make quality-gate`를 실행합니다.
4. dependency가 수치 또는 plot에 영향을 줄 수 있을 때만 과학적 결과를 다시 생성합니다.
5. 변경된 모든 artifact를 확인하고 의미 있는 수치 차이를 기록합니다.

CI가 green이라는 이유만으로 merge하지 말고 제어 거동과 문서화된 결과의 신뢰성을 확인하십시오.
