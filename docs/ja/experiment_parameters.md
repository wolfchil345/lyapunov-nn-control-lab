🌐 言語: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# 実験パラメータ

## パラメータ群

| 群 | 例 | 主な場所 |
|---|---|---|
| Plant | mass, damping, stiffness | `src/system.py`, `src/parameter_variation.py` |
| Controller | `Q`, `R`, network size, saturation limit | `src/system.py`, `src/controllers.py`, `main.py` |
| Training | seed, epochs, learning rate, dataset size, loss weights | `src/controllers.py`, `main.py` |
| Simulation | initial state, duration, evaluation times | `src/simulation.py`, `main.py` |
| Stability | state range, grid density, decay margin | `src/lyapunov.py`, `main.py` |
| Robustness | noise, parameter cases, ablation weights | `src/noise.py`, `src/parameter_variation.py`, `src/stability_ablation.py` |

## 公平な比較

一度に一つのparameter群だけ変更します。変更自体が研究課題でない限り、seed、initial state、simulation horizon、evaluation metricを固定します。

新しいreference resultを採用する前に、正確な設定を[実験ログ](experiment_log_template.md)へ記録してください。
