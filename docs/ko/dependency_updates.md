🌐 언어: [English](../en/dependency_updates.md) | [日本語](../ja/dependency_updates.md) | [한국어](../ko/dependency_updates.md) | [ไทย](../th/dependency_updates.md)

# 의존성 업데이트

Dependabot은 설정된 일정에 따라 Python 패키지와 GitHub Actions를 확인합니다.

## 검토 체크리스트

1. 상위 프로젝트의 릴리스 노트를 읽고 호환성을 깨뜨리는 변경이 있는지 확인합니다.
2. 한 번에 한 의존성 group만 업데이트합니다.
3. `python -m pip check`, `make checks`, `make quality-gate`를 실행합니다.
4. 의존성가 수치 또는 그래프에 영향을 줄 수 있을 때만 과학적 결과를 다시 생성합니다.
5. 변경된 모든 산출물를 확인하고 의미 있는 수치 차이를 기록합니다.

CI가 green이라는 이유만으로 병합하지 말고 제어 거동과 문서화된 결과의 신뢰성을 확인하십시오.
