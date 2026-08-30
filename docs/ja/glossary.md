🌐 言語: [English](../en/glossary.md) | [日本語](../ja/glossary.md) | [한국어](../ko/glossary.md) | [ไทย](../th/glossary.md)

# Glossary

この glossary は、Lyapunov Neural-Network Control Lab で使用される重要用語を説明します。

## Control engineering terms

### State
normalized かつ dimensionless な座標 `x = [q, v]` を指します。ここで `q` は position-like coordinate、`v = dq/dtau` は normalized time における velocity です。

### State norm
Euclidean normalized-state magnitude
`||x||_2 = sqrt(q^2 + v^2)` を指します。これは物理的な displacement や velocity ではありません。

### Control input
model に適用される normalized scalar input `u` です。物理的な force unit は定義していません。

### Plant
制御対象の system です。この project では mass-spring-damper system が plant です。

### Closed-loop system
controller が current state の feedback を使って control input を選ぶ system です。

### LQR
Linear Quadratic Regulator。state error と control effort を含む quadratic cost を最小化する古典的最適 controller です。

### Actuator saturation
normalized control input の大きさに対する制限です。

## Stability terms

### Equilibrium
system が変化せずに留まれる state です。この project では target equilibrium は原点です。

### Lyapunov function
安定性を調べるための energy-like function です。軌道に沿って減少する場合、system は equilibrium へ向かっている可能性が高いと解釈します。

### Lyapunov derivative
system trajectory に沿った Lyapunov function の変化率です。

### Region of attraction
原点 equilibrium に対して、集合
`R = {x0 : x(t; x0) -> 0 as t -> infinity}`
を指します。有限シミュレーションや Lyapunov sublevel set の図だけでは、この集合を単独で証明できません。

### Finite-horizon convergence map
normalized-time horizon `T` と normalized-state Euclidean tolerance `epsilon` に対して、strict final-state criterion `||x(T)||_2 < epsilon` が成り立つときに initial state を分類する sampled map です。結果はこれらの設定に依存し、region of attraction そのものではありません。

### Integrated squared control effort
normalized time にわたる normalized `u^2` の積分です。historical field name である `control_energy` は同じ値を指しますが、物理エネルギーではありません。

## Machine-learning terms

### Neural-network controller
neural network で表現される controller です。system state を control input に写像します。

### Imitation learning
別の controller の挙動を模倣するよう model を学習する方法です。この project では neural network が LQR を模倣します。

### Stability-aware training
imitation accuracy だけでなく、Lyapunov stability に関連する penalty を含む training です。

### Ablation study
設計要因の 1 つを変更または除去し、その影響を調べる実験です。この project では stability penalty weight を変更します。
