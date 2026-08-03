🌐 언어: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# 브랜치 보호

활성화된 `Protect main` ruleset으로 기본 브랜치를 보호하세요.

## 권장 규칙

- 병합 전에 pull request를 요구합니다.
- 대화가 모두 해결되어야 병합할 수 있게 합니다.
- 안정적인 상태 검사를 통과하고 브랜치가 최신 상태이도록 요구합니다.
- 강제 push와 브랜치 삭제를 차단합니다.
- 독립적인 검토자가 없는 1인 저장소라면 필수 승인 수를 0으로 설정합니다.
- 관리자 우회는 pull request와 비상 상황에서만 허용합니다.

GitHub에 표시된 검사 이름을 그대로 사용하세요. 보통 Python tests, local checks, quality gate, CodeQL analysis가 포함됩니다.

저장소의 병합 전략도 함께 변경할 계획이 아니라면 선형 기록을 요구하지 마세요. 릴리스에 적용하기 전에 문서 풀 리퀘스트로 규칙을 시험하세요.
