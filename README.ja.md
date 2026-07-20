🌐 言語: [English](README.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [ไทย](README.th.md)

# Lyapunov NN Control Lab

このプロジェクトは、ニューラルネットワーク制御器を用いた制御工学実験リポジトリです。

質量ばねダンパ系を対象に、LQR制御器のふるまいをニューラルネットワークで学習し、Lyapunov関数に基づく安定性の考え方を組み合わせます。

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

## 重要ドキュメント

- [プロジェクト概要](docs/ja/project_summary.md)
- [手法説明](docs/ja/methodology.md)
- [実験ワークフロー](docs/experiment_workflow.md)
- [結果の読み方](docs/results_interpretation.md)
- [オンボーディングガイド](docs/onboarding.md)
- [メンテナンスガイド](docs/maintenance.md)

## ポートフォリオとしての目的

このリポジトリは、制御工学、機械学習、安定解析、研究ソフトウェア管理を組み合わせたポートフォリオプロジェクトです。
