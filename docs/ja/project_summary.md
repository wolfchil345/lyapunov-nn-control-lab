🌐 言語: [English](../en/project_summary.md) | [日本語](../ja/project_summary.md) | [한국어](../ko/project_summary.md) | [ไทย](../th/project_summary.md)

# プロジェクト概要

Lyapunov NN Control Lab は、制御工学と機械学習を組み合わせた研究用ポートフォリオプロジェクトです。

このプロジェクトでは、質量ばねダンパ系を対象に、LQR制御器のふるまいをニューラルネットワーク制御器で近似します。さらに、Lyapunov関数に基づく考え方を使い、閉ループ系の安定性を意識した評価を行います。

## 目的

- ニューラルネットワーク制御器を学習する
- LQR制御器との挙動を比較する
- Lyapunov関数を使って安定性を確認する
- シミュレーション結果を可視化する
- 再現性のある研究ソフトウェアとして整理する

## 主な技術

- Python
- PyTorch
- LQR制御
- Lyapunov安定性
- シミュレーション評価
- GitHub Actions による自動チェック

## ポートフォリオとしての価値

このリポジトリは、制御工学、機械学習、安定解析、研究ソフトウェア管理を一つの流れで示すためのプロジェクトです。

## 公称プラント（補足）

このプロジェクトでの公称正規化パラメータは次の通りです：MASS = 1.0, DAMPING = 0.4, STIFFNESS = 2.0。これらの値に対する状態行列 `A` の固有値はおおむね `-0.2 + 1.4j` と `-0.2 - 1.4j` であり，どちらも実部が負であるため公称の無制御線形プラントは既に漸近安定です。LQRは不安定プラントの安定化を目的とするのではなく，過渡応答と制御トレードオフを変える基準器として用います。

## Key outputs

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png` (歴史的ファイル名、有限時間収束マップに由来)
- `results/region_of_attraction_comparison.png` (歴史的ファイル名、比較図)
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`
