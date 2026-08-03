🌐 언어: [English](../en/pull_request_review.md) | [日本語](../ja/pull_request_review.md) | [한국어](../ko/pull_request_review.md) | [ไทย](../th/pull_request_review.md)

# Pull Request Review

## 일반 review

- [ ] Title과 summary가 하나의 집중된 변경을 설명한다.
- [ ] Test와 required check가 pass한다.
- [ ] User-facing behavior가 바뀌면 문서를 네 언어로 업데이트한다.
- [ ] Generated file을 의도적으로 include 또는 ignore한다.
- [ ] Merge 전에 conversation을 해결한다.

## 과학적 review

- [ ] Seed, plant parameter, controller architecture, loss, evaluation setting 변경이 명확하다.
- [ ] 수치와 figure diff를 설명한다.
- [ ] Sampled check를 formal proof로 표현하지 않는다.
- [ ] Failure case와 limitations를 유지한다.

## Local commands

```bash
git diff --check
make checks
make quality-gate
```

Latest commit이 모든 required check를 통과한 뒤 protected `main` branch를 통해서만 merge합니다.
