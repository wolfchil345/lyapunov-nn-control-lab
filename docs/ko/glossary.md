🌐 언어: [English](../en/glossary.md) | [日本語](../ja/glossary.md) | [한국어](../ko/glossary.md) | [ไทย](../th/glossary.md)

# Glossary

이 glossary는 Lyapunov Neural-Network Control Lab에서 사용하는 중요한 용어를 설명합니다.

## Control engineering terms

### State
normalized, dimensionless 좌표 `x = [q, v]`를 말합니다. 여기서 `q`는 position-like coordinate이고 `v = dq/dtau`는 normalized time에서의 velocity입니다.

### State norm
Euclidean normalized-state magnitude
`||x||_2 = sqrt(q^2 + v^2)`를 의미합니다. 물리적 displacement나 velocity를 뜻하지 않습니다.

### Control input
model에 적용되는 normalized scalar input `u`입니다. 물리 force unit은 정의하지 않습니다.

### Plant
제어되는 system을 의미합니다. 이 project에서 plant는 mass-spring-damper system입니다.

### Closed-loop system
controller가 current state의 feedback을 사용해 control input을 선택하는 system입니다.

### LQR
Linear Quadratic Regulator. state error와 control effort를 포함하는 quadratic cost를 최소화하는 고전적 optimal controller입니다.

### Actuator saturation
normalized control input 크기에 대한 제한입니다.

## Stability terms

### Equilibrium
system이 변화 없이 머무를 수 있는 state입니다. 이 project에서 target equilibrium은 원점입니다.

### Lyapunov function
안정성을 연구하기 위한 energy-like function입니다. trajectory를 따라 감소하면 system이 equilibrium으로 이동 중일 가능성이 큽니다.

### Lyapunov derivative
system trajectory를 따라 Lyapunov function이 변하는 비율입니다.

### Region of attraction
원점 equilibrium에 대해
`R = {x0 : x(t; x0) -> 0 as t -> infinity}`
인 집합을 뜻합니다. 유한 시뮬레이션이나 Lyapunov sublevel set 그림만으로는 이 집합을 단독으로 인증할 수 없습니다.

### Finite-horizon convergence map
normalized-time horizon `T`와 normalized-state Euclidean tolerance `epsilon`에 대해 strict final-state criterion `||x(T)||_2 < epsilon`이 성립할 때 initial state를 분류하는 sampled map입니다. 결과는 해당 설정에 의존하며 region of attraction 자체가 아닙니다.

### Integrated squared control effort
normalized time에 대한 normalized `u^2` 적분입니다. historical field name인 `control_energy`는 같은 수치를 가리키지만 물리 에너지는 아닙니다.

## Machine-learning terms

### Neural-network controller
neural network로 표현되는 controller입니다. system state를 control input으로 매핑합니다.

### Imitation learning
다른 controller의 동작을 복사하도록 model을 학습하는 방법입니다. 이 project에서 neural network는 LQR을 모방합니다.

### Stability-aware training
imitation accuracy뿐 아니라 Lyapunov stability 관련 penalty를 포함하는 training입니다.

### Ablation study
설계 요인 하나를 변경하거나 제거해 그 영향을 분석하는 실험입니다. 이 project는 stability penalty weight를 바꿉니다.
