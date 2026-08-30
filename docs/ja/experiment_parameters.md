🌐 言語: [English](../en/experiment_parameters.md) | [日本語](../ja/experiment_parameters.md) | [한국어](../ko/experiment_parameters.md) | [ไทย](../th/experiment_parameters.md)

# Experiment Parameters ガイド

このガイドでは、実験の挙動と結果に影響する主要パラメータを説明します。

## なぜパラメータが重要か

ニューラルネットワーク制御実験では、学習設定、乱数シード、グリッド範囲、システム定数、ロバスト性設定を変えると結果が変わります。結果比較の前に、重要なパラメータ変更を記録してください。

## 主なパラメータ群

## 座標規約

この実験は normalized かつ無次元です。`tau` は normalized time、`x = [q, v]` は normalized position と velocity、`u` は normalized control input を表します。したがって閾値やノイズレベルも normalized coordinates で扱います。

## 1. システムパラメータ

これらは normalized な 2 次モデルを定義します。normalized mass、damping、stiffness 係数および状態空間行列が含まれます。これらの数値係数は kg や N/m のような SI 量ではありません。

重要ファイル:

- `src/system.py`
- `src/parameter_variation.py`

## 2. 制御器パラメータ

これらは LQR 参照制御器、neural network 制御器、saturation 挙動、学習済み制御出力に影響します。

重要ファイル:

- `src/system.py`
- `src/controllers.py`
- `main.py`

## 3. 学習パラメータ

これらは neural network の学習に影響します。

例:

- Random seed
- Number of epochs
- Learning rate
- Dataset size
- Loss weights
- Network hidden size

重要ファイル:

- `src/controllers.py`
- `main.py`

## 4. シミュレーションパラメータ

これらは閉ループ評価に影響します。

例:

- Initial condition
- Normalized simulation time
- Normalized time step
- Controller saturation limit

重要ファイル:

- `src/simulation.py`
- `main.py`

## 5. Lyapunov グリッドパラメータ

これらは sampled Lyapunov-style checks に影響します。

例:

- State range
- Grid density
- Controller used during grid evaluation

重要ファイル:

- `src/lyapunov.py`
- `main.py`

## 6. ロバスト性パラメータ

これらは noise 実験と model variation 実験に影響します。

例:

- normalized state の 2 座標へ独立適用する scalar noise standard deviation
- Parameter variation range
- Number of tested cases

重要ファイル:

- `src/noise.py`
- `src/parameter_variation.py`
- `src/stability_ablation.py`

## 安全な比較ルール

2 つの実験結果を比較する際は、可能な限り 1 回に 1 つのパラメータ群だけを変更してください。

stability-weight ablation は random seed を繰り返し nuisance factor として扱います。すべての weight は同じ明示的 seed list で学習します。既定の研究ワークフローでは 3 個の連続 seed を使い、呼び出し側は明示的 `ExperimentSeedPlan` を渡すか base seed と repeat count を設定できます。

measurement-noise 実験でも、すべての noise amplitude に同じ seed list を使います。各 seed について、1 つの standardized Gaussian sequence を各 standard deviation でスケーリングして使用します。この common-random-number 設計により、全ての確率的不確実性が除去されたとは主張せずに、seed 単位のペア比較を可能にします。

## 最終結果を保存する前に

次を実行します。

```bash
python scripts/check_environment.py
make checks
python main.py
python scripts/summarize_results.py
```

その後、どのパラメータをなぜ変更したかを記録してください。
