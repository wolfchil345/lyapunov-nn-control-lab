🌐 언어: [English](../en/results_interpretation.md) | [日本語](../ja/results_interpretation.md) | [한국어](../ko/results_interpretation.md) | [ไทย](../th/results_interpretation.md)

# 결과 해석

## 성능 지표

- `final_state_norm`: 마지막 시점에서 목표 평형점까지의 거리.
- `settling_time_s`: 이후 상태가 threshold 안에 유지되는 첫 시간.
- `quadratic_cost`: LQR 형태 상태 및 제어 penalty의 적분.
- `control_energy`: 제어 입력 제곱의 적분.
- `max_abs_control`: 가장 큰 절대 actuator command.

한 metric만으로 안정성이나 제어기 품질을 판단할 수 없습니다. 수렴, 제어 노력, cost, robustness를 함께 비교합니다.

## 안정성 근거

표본에서 음수인 `V_dot`는 평가 grid 안의 국소 감소를 지지하지만 grid 사이, 영역 밖, 미시험 불확실성을 증명하지 않습니다.

## 강건성과 인력 영역

Noise, parameter variation, actuator saturation은 scenario test입니다. Region-of-attraction map은 선택한 horizon과 threshold 아래의 표본 초기조건만 분류합니다.

## 읽는 순서

1. 설정과 seed 확인.
2. 궤적과 제어 제한 확인.
3. 정량 metric 비교.
4. Lyapunov와 region-of-attraction 진단 검토.
5. [한계](limitations.md)를 읽고 failure case 기록.
