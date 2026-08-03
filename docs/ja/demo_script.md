🌐 言語: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# 5分間デモ

## 0:00–0:30 — 目的

「このプロジェクトはLQRを模倣するニューラル制御器を、Lyapunov解析とロバスト性試験で評価します。」

## 0:30–1:30 — リポジトリの紹介

`README.md`、`src/`、`tests/`、`scripts/`、多言語`docs/`、`results/` を示します。

## 1:30–2:15 — 再現性

`python examples/quick_start.py` を実行するか、完了済みの `make quality-gate` の結果を示します。短いデモ中に完全な実験は開始しません。

## 2:15–3:30 — 手法

質量ばねダンパモデル、LQR 教師、ニューラル模倣、`u(0) = 0`、サンプル点に基づく Lyapunov ペナルティを説明します。

## 3:30–4:30 — 証拠

`position_comparison.png`、`training_loss.png`、`region_of_attraction_comparison.png` を示し、飽和、ノイズ、パラメータ試験に触れます。

## 4:30–5:00 — 誠実な結論

結果がシミュレーションとサンプル点に基づくことを明示し、次の研究課題を説明します。
