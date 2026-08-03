🌐 言語: [English](../en/model_card.md) | [日本語](../ja/model_card.md) | [한국어](../ko/model_card.md) | [ไทย](../th/model_card.md)

# モデルカード

## モデル

Controllerは `[position, velocity]` から一つのforce commandへmappingする小さなPyTorch multilayer perceptronです。Outputをshiftして `u(0) = 0` を強制します。

## 学習

Bounded regionからstateをsampleし、公称LQR controllerでlabelを作ります。Trainingはimitation MSEとweighted sampled Lyapunov penaltyを最小化します。Repositoryはfixed random seedを設定します。

## 想定用途

- Learning-based controlの教育とresearch prototyping。
- 収録simulationにおけるLQRとのreproducible comparison。
- Stability-aware objectiveとrobustness diagnosticの探索。

## 対象外

- Safety-criticalまたはhardwareへの直接deployment。
- Formal、global、distribution-free stabilityの主張。
- 検証済みstate、actuator、plant range外での運用。

## 評価

Closed-loop trajectory、final norm、settling time、cost、control energy、maximum input、sampled `V_dot`、robustness scenario、estimated region of attraction。

Model再利用前に[制約](limitations.md)と[再現性](reproducibility.md)を確認してください。
