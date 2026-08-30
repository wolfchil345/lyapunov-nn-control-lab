🌐 言語: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# プロジェクト概要

## Overview

このプロジェクトは、Lyapunov に着想を得た安定性解析を伴う neural-network control の Python 研究ラボです。

対象システムは質量ばねダンパプラントです。本プロジェクトは、古典的 LQR 制御器と、模倣学習で学習した neural-network 制御器を比較します。

## Main goal

主目的は、neural-network 制御器が LQR 参照を模倣しつつ、有用な過渡特性、ロバスト性、サンプル Lyapunov 挙動を維持できるかを研究することです。公称の無制御線形プラントはすでに漸近安定であり、制御器は閉ループ性能を変えます。

## Nominal plant (canonical)

リポジトリ全体で使用する canonical な normalized plant parameters は次のとおりです。

- MASS = 1.0
- DAMPING = 0.4
- STIFFNESS = 2.0

これらのパラメータに対して状態行列 `A` の固有値はおおむね `-0.2 + 1.4j` と `-0.2 - 1.4j` で、いずれも実部が負です。これらの値は canonical baseline の一部であり、このファイルの全言語版で逐語的に保持する必要があります。

## Main features

- LQR baseline controller
- neural-network controller
- stability-aware training penalty
- Lyapunov grid check
- actuator saturation experiment
- measurement-noise robustness experiment
- parameter robustness experiment
- phase portrait visualization
- Lyapunov contour visualization
- finite-horizon convergence mapping with explicit sampling metadata
- controller comparison using an explicit finite-horizon final-state tolerance
- stability-weight ablation study
- automatic experiment report generation

## Key outputs

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png` (finite-horizon map に対する historical filename)
- `results/region_of_attraction_comparison.png` (finite-horizon comparison に対する historical filename)
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## Why this project matters

neural-network 制御器は強力ですが、安定性は制御工学における主要な懸念です。

このプロジェクトは、学習ベース制御と古典的安定解析の考え方を結び付けます。neural-network 制御器の完全な形式証明を与えることは主張しませんが、安定挙動を研究するための実用的な経験的ツールを提供します。

## Portfolio value

このリポジトリは、制御工学、Python、PyTorch、数値シミュレーション、テスト、可視化、GitHub Actions、ドキュメント作成、再現可能な研究ワークフローの技能を示します。
