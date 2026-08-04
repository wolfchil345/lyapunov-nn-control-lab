🌐 언어: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# 기여 가이드

Lyapunov NN Control Lab 개선에 참여해 주셔서 감사합니다.

## 설정

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## 작업 절차

1. 최신 `main`에서 목적이 분명한 브랜치를 만듭니다.
2. 과학적 변경, 코드 변경, 문서 변경의 범위를 명확히 구분합니다.
3. 동작을 바꾸는 경우 테스트를 추가합니다.
4. 사용자용 문서를 영어, 일본어, 한국어, 태국어 네 언어로 갱신합니다.
5. `git diff --check`, `make checks`, `make quality-gate`를 실행합니다.
6. 풀 리퀘스트를 열고 필수 검사가 모두 완료된 뒤 병합합니다.

## 과학적 결과

변경에 필요한 경우가 아니면 결과를 다시 생성하거나 커밋하지 마십시오. 난수 시드와 실험 설정을 기록하고, 모든 수치 및 그림 차이를 검토하며, 표본점에서 얻은 안정성 근거를 정확히 설명하십시오.

## 환영하는 기여

- 기준 제어기와 신중하게 설계된 강건성 실험.
- 수치 계산, 보고서 생성, 문서 도구에 대한 테스트.
- 더 명확한 그림, 예제, 번역, 방법론 설명.
- 재현성, 안전성, 실패 사례에 대한 개선.

커밋 메시지는 `Add noise robustness test` 또는 `Clarify Lyapunov limitations`처럼 짧은 명령형으로 작성합니다.
