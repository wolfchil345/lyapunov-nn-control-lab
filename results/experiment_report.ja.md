🌐 言語: [English](experiment_report.md) | [日本語](experiment_report.ja.md) | [한국어](experiment_report.ko.md) | [ไทย](experiment_report.th.md)

# 実験レポート

このレポートはLyapunov NN Control Labで生成された実験結果を要約します。

## 主な実験

| 実験 | 出力 |
|---|---|
| モデル構成 | `model_architecture.png` |
| LQRとニューラルネットワークの比較 | `position_comparison.png` |
| 安定性を意識した学習損失 | `training_loss.png` |
| 複数の初期条件 | `multiple_initial_conditions.png` |
| アクチュエータ飽和の比較 | `saturation_comparison.png` |
| 観測ノイズに対するロバスト性 | `noise_robustness.png` |
| パラメータ変動に対するロバスト性 | `parameter_robustness.png` |
| 位相図 | `phase_portrait.png` |
| Lyapunov等高線図 | `lyapunov_contours.png` |
| 引き込み領域マップ | `region_of_attraction.png` |
| 制御器別の引き込み領域比較 | `region_of_attraction_comparison.png` |
| 安定性重みのアブレーション試験 | `stability_weight_ablation.png` |

## 利用可能な図

- [`model_architecture.png`](model_architecture.png)
- [`position_comparison.png`](position_comparison.png)
- [`training_loss.png`](training_loss.png)
- [`multiple_initial_conditions.png`](multiple_initial_conditions.png)
- [`saturation_comparison.png`](saturation_comparison.png)
- [`noise_robustness.png`](noise_robustness.png)
- [`parameter_robustness.png`](parameter_robustness.png)
- [`phase_portrait.png`](phase_portrait.png)
- [`lyapunov_contours.png`](lyapunov_contours.png)
- [`region_of_attraction.png`](region_of_attraction.png)
- [`region_of_attraction_comparison.png`](region_of_attraction_comparison.png)
- [`stability_weight_ablation.png`](stability_weight_ablation.png)

## 性能指標（抜粋）

| controller | initial_position | initial_velocity | final_state_norm | settling_time_s | quadratic_cost | control_energy | max_abs_control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LQR | 1.5 | 0.0 | 3.3512211263851475e-06 | 3.37 | 14.648088325259708 | 4.456642635355886 | 4.348469228349534 |
| LQR | -1.5 | 0.0 | 3.3512211263851475e-06 | 3.37 | 14.648088325259708 | 4.456642635355886 | 4.348469228349534 |
| LQR | 1.0 | 1.5 | 3.097042361828861e-06 | 3.5 | 13.582997380405825 | 7.576846237440828 | 6.530457677055545 |
| LQR | -1.0 | -1.5 | 3.097042361828861e-06 | 3.5 | 13.582997380405825 | 7.576846237440828 | 6.530457677055545 |
| LQR | 0.5 | -2.0 | 5.018394958296208e-07 | 2.56 | 3.5708128507878527 | 4.151303514719738 | 3.3924811792024077 |
| Neural network | 1.5 | 0.0 | 2.7497692462658866e-07 | 3.25 | 14.680261467448672 | 4.733569667999773 | 4.450384140014648 |
| Neural network | -1.5 | 0.0 | 2.845442886644117e-07 | 3.2600000000000002 | 14.674752308656242 | 4.693609391104969 | 4.505607604980469 |
| Neural network | 1.0 | 1.5 | 1.8043428851131705e-07 | 3.34 | 13.62549419698057 | 8.353344458862482 | 6.977767467498779 |

## 安定性重みのアブレーション結果（抜粋）

| stability_weight | lyapunov_violation_fraction | final_state_norm | settling_time_s | quadratic_cost | control_energy |
| --- | --- | --- | --- | --- | --- |
| 0.0 | 0.0 | 2.56460257589076e-08 | 2.99 | 14.77627249722799 | 5.410421142108917 |
| 1.0 | 0.0 | 7.738160083800791e-10 | 2.5500000000000003 | 14.834420901355982 | 5.515590194940069 |
| 10.0 | 0.0 | 4.003802800566632e-09 | 2.0300000000000002 | 14.904517715156533 | 5.859179145902849 |
| 50.0 | 0.0 | 1.3967706048153224e-07 | 3.35 | 14.760553849458393 | 3.7422401939648555 |

## 解釈ガイド

- `final_state_norm`が小さいほど、制御器は状態を平衡点へ近づけています。
- `settling_time_s`が短いほど、制御器は速く安定化しています。
- `control_energy`が小さいほど、必要な制御入力は少なくなります。
- `lyapunov_violation_fraction`が小さいほど、サンプル状態でLyapunov減少条件に違反する点が少なくなります。
- 引き込み領域の結果は、選択した設定で収束するサンプル初期状態を推定したものです。
- これらの結果は経験的証拠であり、形式的な安定性証明ではありません。
