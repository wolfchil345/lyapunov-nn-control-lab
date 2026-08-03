🌐 언어: [English](../pull_request_template.md) | [日本語](pull_request_template.ja.md) | [한국어](pull_request_template.ko.md) | [ไทย](pull_request_template.th.md)

# Pull Request

## 요약

집중된 변경과 필요한 이유를 설명하십시오.

## 유형

- [ ] Bug fix
- [ ] Experiment 또는 scientific change
- [ ] Documentation 또는 translation
- [ ] Test, tooling, refactoring

## 과학적 영향과 생성 파일

- 변경한 seed, parameter, architecture, loss, metric:
- 변경한 plot, CSV, report, model artifact:
- 예상 수치 차이와 limitations:

## 검증

- [ ] `git diff --check`
- [ ] `make checks`
- [ ] `make quality-gate`
- [ ] 필요한 viewer-facing documentation을 네 언어로 업데이트
- [ ] Generated artifact를 review하고 의도적으로 include

## Follow-up

미해결 work를 적거나 `None`이라고 쓰십시오.
