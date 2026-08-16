🌐 言語: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

# ![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)
# ![Quality gate](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml/badge.svg)

# Lyapunov NN Control Lab

このプロジェクトは、ニューラルネットワーク制御器を用いた制御工学実験リポジトリです。

質量ばねダンパ系を対象に、LQR制御器の振る舞いをニューラルネットワークで学習し、Lyapunov関数に基づく安定性解析を組み合わせます。

## 主な内容

- Python と PyTorch による制御器学習
- LQR制御器を教師としたニューラルネットワーク制御
- Lyapunovペナルティを用いた安定性を意識した学習
- シミュレーション、評価、ロバスト性確認、結果の可視化
- GitHub Actions、テスト、品質ゲートによる再現性チェック

## はじめ方

```bash
python scripts/check_environment.py
python examples/quick_start.py
python scripts/quality_gate.py
```

## 重要な技術的注記

正規化モデルの標準パラメータは次のとおりです：MASS = 1.0, DAMPING = 0.4, STIFFNESS = 2.0。これらの公称値における状態行列 `A` の固有値は概ね `-0.2 + 1.4j` と `-0.2 - 1.4j` であり，どちらも実数部が負であるため，公称の無制御線形プラントは既に漸近安定です。LQRは不安定なプラントを安定化する目的ではなく，過渡応答や制御のトレードオフを変えるものです。

このリポジトリでは，正規化された無次元2次モデルを採用します。`tau` は正規化時間，`q` は正規化位置様座標，`v = dq/dtau` は正規化速度，`u` は正規化制御入力，状態は `x = [q, v]` です。したがって `||x||_2 = sqrt(q^2 + v^2)` は正規化状態座標上のEuclideanノルムを意味します。既存のCSVフィールド名 `settling_time_s` は互換性のため維持されていますが，これは正規化時間を表すAPI上の古いフィールド名であることに注意してください。

## 重要ドキュメント

- [ドキュメント一覧](docs/ja/index.md)
- [プロジェクト概要](docs/ja/project_summary.md)
- [手法説明](docs/ja/methodology.md)
- [実験ワークフロー](docs/experiment_workflow.md)
- [結果の読み方](docs/results_interpretation.md)
- [オンボーディングガイド](docs/onboarding.md)
- [メンテナンスガイド](docs/maintenance.md)

## Lyapunov評価と学習

本プロジェクトはサンプリング点に基づくLyapunov評価を行います。Lyapunov関数の導関数は閉ループで次のように表されます：

```text
V-dot(x) = 2 x^T P (A x + B pi(x))
```

評価器は2つの条件を報告します：

```text
基本減少: V-dot(x) <= 0
減衰マージン: V-dot(x) + alpha * ||x||_2^2 <= 0
```

学習では，減衰残差の正の部分を罰則化します。実装上の表記を維持するとペナルティは次の通りです：

```text
decay residual = V-dot(x) + alpha * ||x||_2^2
Lyapunov penalty = mean(ReLU(decay residual))
```

デフォルトの減衰マージンは `alpha = 0.05` （`DEFAULT_DECAY_MARGIN = 0.05` と同等）です。数値許容誤差（例：`1e-9`）は `alpha` とは別に扱われ，評価の分類閾値のための小さなトレランスです。

## 有限時間収束評価

サンプルごとの有限時間収束評価は次の厳密な判定を用います：

```text
||x(T)||_2 < epsilon
```

この地図は有限のサンプルに基づく経験的結果であり，連続状態空間に対する形式的な吸引領域証明ではありません。

## 成果物と来歴（provenance）

実行は `results/runs/<run_id>/` に収集され，マニフェストとSHA-256チェックサムを含みます：`manifest.json`，`SHA256SUMS`，および `report.md`。古い履歴的成果物（例：`results/region_of_attraction.png`）は再現性のためそのまま保持しています（英語版の説明に従い歴史的ファイル名として扱います）。


## ポートフォリオとしての目的

このリポジトリは、制御工学、機械学習、安定解析、研究ソフトウェア管理を組み合わせたポートフォリオプロジェクトです。
