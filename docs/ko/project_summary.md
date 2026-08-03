🌐 언어: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# 프로젝트 요약

## 목적

Lyapunov NN Control Lab은 기계 system, 고전 제어, neural network, 안정성 해석을 연결하는 재현 가능한 research 및 portfolio project입니다.

## 접근 방법

Mass-spring-damper plant를 model화하고 LQR baseline을 설계하며 LQR state-feedback law를 모방하는 neural controller를 학습합니다. Training에는 sampled Lyapunov penalty도 포함됩니다. 여러 initial state, quantitative metric, actuator saturation, measurement noise, plant-parameter variation, sampled Lyapunov behavior, estimated region of attraction으로 평가합니다.

## 근거

- Automated test, quick-start example, CI, quality gate.
- 추적 figure, CSV metric, 생성 experiment report.
- Fixed random seed와 documented reproduction workflow.
- Empirical sampled evidence와 formal proof의 정직한 구분.

## 현재 결과

추적 test setting에서 neural controller는 LQR baseline을 가깝게 따르고 선택 initial state에서 수렴하며 sampled Lyapunov violation이 zero입니다. 이 결과는 documented model, region, threshold, uncertainty scenario에 한정됩니다.

## 포트폴리오 가치

System modeling, optimal control, PyTorch training, numerical simulation, scientific evaluation, software testing, GitHub workflow, release management, 다국어 technical communication을 보여줍니다.
