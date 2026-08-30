🌐 言語: [English](../en/model_card.md) | [日本語](../ja/model_card.md) | [한국어](../ko/model_card.md) | [ไทย](../th/model_card.md)

# Model Card

この model card は、Lyapunov Neural-Network Control Lab で使用する neural-network controller を要約したものです。

## Model purpose

neural-network controller は system state を 1 つの scalar control input に写像します。

このモデルは、stability-aware training penalty を用いながら LQR controller を模倣するよう学習されます。

## System state

model input は 2 次元 state です。

- normalized position `q`
- normalized velocity `v = dq/dtau`

## Model output

model output は 1 つの scalar control input です。

- model に適用される normalized scalar control input `u`

## Training target

training target は LQR controller から生成されます。

neural network は LQR の state-to-control mapping を近似するよう学習します。

## Stability-aware training

training process には Lyapunov-style penalty を含めることができます。

これにより、sampled states 周辺で Lyapunov function を減少させる挙動が促進されます。

## Intended use

この controller は、simulation-based control experiments、教育、研究探索を目的としています。

neural-network control、Lyapunov-style checks、robustness tests、controller comparison の検討に有用です。

## Out-of-scope use

この model を安全認証済み real-world controller として使用すべきではありません。

hardware deployment、危険な system、安全性が重要な環境については検証されていません。

## Evaluation methods

controller は次を用いて評価されます。

- closed-loop simulation
- final normalized-state norm
- normalized settling time
- quadratic LQR-style cost
- integrated squared normalized control effort
- maximum absolute normalized control input
- Lyapunov derivative grid checks
- robustness experiments
- finite-horizon final-state tolerance mapping

## Known limitations

- plant model は単純です。
- controller は学習領域外で一般化できない可能性があります。
- grid-based Lyapunov checks は global stability を証明しません。
- simulation results は環境によりわずかに変動する可能性があります。
- robustness tests は選択されたケースのみを対象とします。

## Recommended reporting

結果を報告する際は、次を含めてください。

- training settings
- random seed
- system parameters
- controller type
- evaluation metrics
- Lyapunov check results
- robustness settings
- finite-horizon convergence settings: horizon, tolerance, bounds, grid,
  tested count, and converged count

## Future improvements

- controller architectures を増やす。
- KAN-based controllers と比較する。
- より強い formal verification を追加する。
- neural Lyapunov functions を直接学習する。
- より多くの nonlinear systems を検証する。
