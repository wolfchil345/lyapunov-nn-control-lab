🌐 언어: [English](../en/faq.md) | [日本語](../ja/faq.md) | [한국어](../ko/faq.md) | [ไทย](../th/faq.md)

# 자주 묻는 질문

## 이 project는 무엇인가?

Mass-spring-damper system에서 LQR을 모방하는 neural controller를 학습하고 performance, sampled Lyapunov behavior, robustness를 평가합니다.

## 왜 LQR을 teacher로 사용하는가?

LQR은 투명하고 재현 가능하며 공칭 linear plant를 안정화하므로 유용한 baseline과 label source입니다.

## 안정성을 증명하는가?

아닙니다. 이차 Lyapunov candidate를 사용한 simulation과 finite-grid evidence를 제공합니다. Formal continuous-domain verification은 현재 범위 밖입니다.

## 일반 machine-learning demo와 무엇이 다른가?

Closed-loop trajectory, control effort, cost, saturation, noise, model variation, Lyapunov behavior, estimated region of attraction을 재현 가능한 software check와 함께 평가합니다.

## 어떻게 검증하는가?

`python examples/quick_start.py`, `make checks`, `make quality-gate`를 실행합니다. 전체 실험은 `python main.py`를 사용합니다.

## 무엇부터 읽어야 하는가?

[프로젝트 요약](project_summary.md), [방법론](methodology.md), [실험 workflow](experiment_workflow.md), [한계](limitations.md)를 읽습니다.
