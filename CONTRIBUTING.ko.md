🌐 언어: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# 기여 가이드

Lyapunov NN Control Lab 개선에 참여해 주셔서 감사합니다.

## 설정

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## Workflow

1. 최신 `main`에서 목적이 분명한 branch 생성.
2. 과학, code, documentation 변경 범위 구분.
3. Behavior 변경에 test 추가.
4. Viewer-facing documentation을 영어, 일본어, 한국어, 태국어로 업데이트.
5. `git diff --check`, `make checks`, `make quality-gate` 실행.
6. Pull request를 open하고 모든 required check 후 merge.

## 과학적 결과

변경에 필요하지 않으면 result를 재생성하거나 commit하지 않습니다. Seed와 experiment setting을 기록하고 모든 수치 및 figure diff를 검토하며 sampled stability evidence를 정확히 설명합니다.

## 좋은 기여

- Controller baseline과 신중하게 설계한 robustness experiment.
- Numerical, reporting, documentation tool test.
- 명확한 plot, example, translation, methodology 설명.
- Reproducibility, safety, failure-case 개선.

`Add noise robustness test`, `Clarify Lyapunov limitations` 같은 짧은 명령형 commit message를 사용합니다.
