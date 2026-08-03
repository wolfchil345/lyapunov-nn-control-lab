🌐 言語: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

[![Python tests](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/tests.yml)
[![Local checks](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/local-checks.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/local-checks.yml)
[![Quality gate](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml/badge.svg)](https://github.com/wolfchil345/lyapunov-nn-control-lab/actions/workflows/quality-gate.yml)
[![Release](https://img.shields.io/github/v/release/wolfchil345/lyapunov-nn-control-lab)](https://github.com/wolfchil345/lyapunov-nn-control-lab/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# Lyapunov NN Control Lab

LQR制御器を模倣するニューラルネットワーク制御器を学習し、閉ループ挙動をサンプル点におけるLyapunov解析、ロバスト性試験、引き込み領域の推定で評価する、再現可能なPython・PyTorch制御実験です。

機械工学、制御理論、機械学習の接点を理解しやすくするため、質量ばねダンパ系をテストベッドとして使用します。

## 特長

- LQRベースラインと、その挙動を模倣するニューラルネットワーク制御器。
- サンプル点に基づくLyapunovペナルティを用いた安定性を意識した学習。
- 複数初期条件および定量的な性能評価。
- アクチュエータ飽和、観測ノイズ、パラメータ変動の試験。
- 位相図、Lyapunov等高線、引き込み領域の比較。
- 再現可能なスクリプト、自動テスト、CIワークフロー、生成レポート。
- 英語、日本語、韓国語、タイ語のドキュメント。

## 制御ループ

```text
状態 x = [position, velocity]
            │
            ▼
 neural-network controller ──► 制御力 u
            ▲                         │
            │                         ▼
            └──── mass-spring-damper plant
```

原点が平衡点となるよう、制御器には `u(0) = 0` の制約を与えています。

## システムと安定性モデル

対象プラントは

```text
m q'' + c q' + k q = u
```

であり、状態空間表現は

```text
x_dot = A x + B u
```

です。LQR制御器は模倣学習の目標 `u = -Kx` を与えます。二次形式のLyapunov候補 `V(x) = x^T P x` に対して、本プロジェクトでは

```text
V_dot(x) = 2 x^T P (A x + B u)
```

をサンプル点で評価し、次の条件への違反をペナルティ化します。

```text
V_dot(x) <= -alpha * ||x||^2
```

これらは経験的な証拠であり、連続状態空間全体に対する形式的証明ではありません。

## 手法

1. 公称の質量ばねダンパ系を定義し、LQRベースラインを設計します。
2. 状態をサンプリングし、LQR制御則で教師ラベルを作ります。
3. 模倣損失とLyapunovペナルティを組み合わせてニューラル制御器を学習します。
4. 複数の初期状態からLQR、ニューラル、飽和制御器をシミュレーションします。
5. 最終状態ノルム、整定時間、二次コスト、制御エネルギー、最大制御入力を計測します。
6. サンプル点でのLyapunov挙動、ロバスト性、推定引き込み領域を評価します。
7. 図、CSV指標、学習済みモデル、実験レポートを保存します。

## 実験と出力

| 実験 | 目的 | 出力 |
|---|---|---|
| アーキテクチャ | ニューラル閉ループ制御構造を説明 | `results/model_architecture.png` |
| 制御器比較 | LQRとニューラル軌道を比較 | `results/position_comparison.png` |
| 安定性を意識した学習 | 総損失、模倣損失、Lyapunov損失を追跡 | `results/training_loss.png` |
| 初期条件 | 複数状態からの収束を確認 | `results/multiple_initial_conditions.png` |
| アクチュエータ飽和 | 制御力制限の影響を評価 | `results/saturation_comparison.png` |
| ノイズロバスト性 | ノイズを含む状態観測を評価 | `results/noise_robustness.png` |
| パラメータロバスト性 | 質量、減衰、ばね定数を変更 | `results/parameter_robustness.png` |
| 状態空間解析 | 位相軌道とLyapunov等高線を表示 | `results/phase_portrait.png`, `results/lyapunov_contours.png` |
| 引き込み領域 | 初期状態グリッド上の収束を比較 | `results/region_of_attraction_comparison.png` |
| 安定性アブレーション | Lyapunovペナルティ重みを比較 | `results/stability_weight_ablation.csv` |
| 自動レポート | 生成された証拠を要約 | `results/experiment_report.ja.md` |

全数値指標は [`results/performance_metrics.csv`](results/performance_metrics.csv) にあります。

## 結果の概要

追跡されている結果は、リポジトリの固定乱数シードと現在の実験設定で生成されています。

| ケース | 最終状態ノルム | 整定時間 | 二次コスト |
|---|---:|---:|---:|
| LQR, `x0 = [1.5, 0.0]` | `3.35e-06` | `3.37 s` | `14.6481` |
| Neural network, `x0 = [1.5, 0.0]` | `2.75e-07` | `3.25 s` | `14.6803` |
| Saturated neural network, `x0 = [1.5, 0.0]` | `2.73e-07` | `3.28 s` | `14.8506` |

追跡されている安定性重みアブレーションでは、全ての重みでサンプルLyapunov違反率が `0.0` でした。実験領域と制約を示すドキュメントと併せて解釈してください。

## 結果ギャラリー

| アーキテクチャ | 制御応答 |
|---|---|
| ![閉ループモデルのアーキテクチャ](results/model_architecture.png) | ![LQRとニューラルネットワークの位置比較](results/position_comparison.png) |
| **安定性を意識した学習** | **引き込み領域の比較** |
| ![学習損失](results/training_loss.png) | ![制御器ごとの引き込み領域比較](results/region_of_attraction_comparison.png) |

生成図の一覧は[図のガイド](docs/ja/figures.md)を参照してください。

## インストール

Python 3.10以降が必要です。CPU実行で十分です。

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

Windows PowerShellでは `.venv\Scripts\Activate.ps1` で環境を有効化します。

## 実行と検証

短いサンプルを実行します。

```bash
python examples/quick_start.py
```

実験全体を実行します。

```bash
python main.py
```

標準チェックまたは完全な準備状況チェックを実行します。

```bash
make checks
make quality-gate
```

便利なコマンドは[コマンドガイド](docs/ja/commands.md)にまとめています。`python scripts/clean_results.py` は `results/` 内の全ファイルを削除するため、実行前に[実験ワークフロー](docs/ja/experiment_workflow.md)を確認してください。

## プロジェクト構成

```text
lyapunov-nn-control-lab/
├── main.py                 # Full experiment pipeline
├── src/                    # Dynamics, controllers, analysis, and plotting
├── tests/                  # Automated test suite
├── scripts/                # Checks and repeatable maintenance commands
├── examples/               # Minimal runnable example
├── docs/{en,ja,ko,th}/     # Localized documentation
└── results/                # Tracked reference outputs and generated model
```

詳細は[プロジェクト構成ガイド](docs/ja/project_structure.md)を参照してください。

## 科学的な制約

- 対象は線形質量ばねダンパ系のシミュレーションであり、実機ではありません。
- ニューラル制御器はLQR教師から学習するため、サンプル領域外へ一般化できない可能性があります。
- Lyapunov評価と引き込み領域評価は有限グリッドとシミュレーションに基づきます。
- ロバスト性実験は選択したノイズ、入力制限、パラメータ変動のみを対象とします。
- 依存関係のバージョンやプラットフォームによって小さな数値差が生じる場合があります。

研究上の結論を出す前に、[制約](docs/ja/limitations.md)、[結果の解釈](docs/ja/results_interpretation.md)、[再現性](docs/ja/reproducibility.md)を確認してください。

## ドキュメント

完全なドキュメント索引は4言語で提供しています。

- [English documentation](docs/en/index.md)
- [日本語ドキュメント](docs/ja/index.md)
- [한국어 문서](docs/ko/index.md)
- [เอกสารภาษาไทย](docs/th/index.md)

主要資料には[研究手法](docs/ja/methodology.md)、[実験ワークフロー](docs/ja/experiment_workflow.md)、[モデルカード](docs/ja/model_card.md)、[研究課題](docs/ja/research_questions.md)があります。

## コミュニティとプロジェクト情報

- [コントリビューション](CONTRIBUTING.ja.md)
- [セキュリティポリシー](SECURITY.ja.md)
- [行動規範](CODE_OF_CONDUCT.ja.md)
- [ロードマップ](ROADMAP.ja.md)
- [リリースノート](RELEASE_NOTES.ja.md)
- [引用メタデータ](CITATION.cff)

## ライセンスと作者

[MIT License](LICENSE)の下で公開しています。

作者は、制御工学、ニューラルネットワーク、安定性解析に関心を持つ機械工学学生のSirichet Sriamonthamです。
