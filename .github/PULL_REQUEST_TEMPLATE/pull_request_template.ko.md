🌐 언어: [English](../pull_request_template.md) | [日本語](pull_request_template.ja.md) | [한국어](pull_request_template.ko.md) | [ไทย](pull_request_template.th.md)

# 풀 리퀘스트

## 요약

집중된 변경과 필요한 이유를 설명하십시오.

## 유형

- [ ] 버그 수정
- [ ] 실험 또는 과학적 변경
- [ ] 문서 또는 번역
- [ ] 테스트, 개발 도구 또는 리팩터링

## 과학적 영향과 생성 파일

- 변경한 시드, 매개변수, 구조, 손실, 지표:
- 변경한 그래프, CSV, 보고서, 모델 산출물:
- 예상 수치 차이와 한계:

## 검증

- [ ] `git diff --check`
- [ ] `make checks`
- [ ] `make quality-gate`
- [ ] 필요한 사용자용 문서를 네 언어로 업데이트
- [ ] 생성된 산출물을 검토하고 의도한 파일만 포함함

## 후속 작업

미해결 작업을 적거나 `None`이라고 써 주세요.
