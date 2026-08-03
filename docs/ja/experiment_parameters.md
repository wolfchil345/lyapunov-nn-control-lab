🌐 言語: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# 実験パラメータ

## パラメータ群

| 群 | 例 | 主な場所 |
|---|---|---|
| プラント | 質量、減衰係数、ばね定数 | `src/system.py`, `src/parameter_variation.py` |
| 制御器 | `Q`, `R`, ネットワークサイズ、飽和限界 | `src/system.py`, `src/controllers.py`, `main.py` |
| 学習 | シード、エポック数、学習率、データセットサイズ、損失の重み | `src/controllers.py`, `main.py` |
| シミュレーション | 初期状態, シミュレーション時間, 評価 評価時刻 | `src/simulation.py`, `main.py` |
| 安定性 | 状態範囲、グリッド密度、減少余裕 | `src/lyapunov.py`, `main.py` |
| ロバスト性 | ノイズ, パラメータ ケース, アブレーション 重み | `src/noise.py`, `src/parameter_variation.py`, `src/stability_ablation.py` |

## 公平な比較

一度に一つのパラメータ群だけ変更します。変更自体が研究課題でない限り、シード、初期状態、シミュレーション 評価時間、評価 指標を固定します。

新しい参照結果を採用する前に、正確な設定を[実験ログ](experiment_log_template.md)へ記録してください。
