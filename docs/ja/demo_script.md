🌐 言語: [English](../en/demo_script.md) | [日本語](../ja/demo_script.md) | [한국어](../ko/demo_script.md) | [ไทย](../th/demo_script.md)

# 5分間デモ

## 0:00–0:30 — 目的

「このprojectはLQRを模倣するneural controllerを、Lyapunov形式とrobustness checkで評価します。」

## 0:30–1:30 — Repository tour

`README.md`、`src/`、`tests/`、`scripts/`、多言語`docs/`、`results/` を示します。

## 1:30–2:15 — 再現性

`python examples/quick_start.py` を実行するか、完了済み `make quality-gate` resultを示します。短いdemo中にfull experimentを開始しません。

## 2:15–3:30 — 手法

Mass-spring-damper model、LQR teacher、neural imitation、`u(0) = 0`、sampled Lyapunov penaltyを説明します。

## 3:30–4:30 — 証拠

`position_comparison.png`、`training_loss.png`、`region_of_attraction_comparison.png` を示し、saturation、noise、parameter testに触れます。

## 4:30–5:00 — 誠実な結論

結果がsimulation-basedかつsampledであると述べ、次の研究課題を説明します。
