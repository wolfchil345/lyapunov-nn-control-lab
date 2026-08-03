🌐 언어: [English](../en/branch_protection.md) | [日本語](../ja/branch_protection.md) | [한국어](../ko/branch_protection.md) | [ไทย](../th/branch_protection.md)

# 브랜치 보호

Active `Protect main` ruleset으로 default branch를 보호합니다.

## 권장 규칙

- Merge 전 pull request 요구.
- Conversation 해결 요구.
- 안정된 status check와 up-to-date branch 요구.
- Force push와 branch deletion 차단.
- Solo repository에서는 독립 reviewer가 없으면 required approval 0.
- Administrator bypass는 pull request와 emergency에만 허용.

GitHub에 표시되는 정확한 check name을 사용합니다. 보통 Python tests, local checks, quality gate, CodeQL analysis입니다.

Repository의 merge strategy도 바꾸지 않는 한 linear history를 켜지 않습니다. Release에 의존하기 전에 documentation pull request로 rule을 시험합니다.
