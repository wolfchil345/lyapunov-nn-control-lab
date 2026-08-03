🌐 言語: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# コントリビューション

Lyapunov NN Control Labの改善に協力いただきありがとうございます。

## セットアップ

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

## ワークフロー

1. 最新 `main` から目的を限定したbranchを作成。
2. 科学、code、documentation変更の範囲を明確化。
3. Behavior変更にtestを追加。
4. Viewer-facing documentationを英語、日本語、韓国語、タイ語で更新。
5. `git diff --check`、`make checks`、`make quality-gate` を実行。
6. Pull requestをopenし、全required checkを待ってからmerge。

## 科学的結果

変更に必要でない限りresultを再生成・commitしません。Seedとexperiment settingを記録し、全数値・figure diffを確認し、sampled stability evidenceを正確に説明します。

## 良い貢献

- Controller baselineと慎重に設計したrobustness experiment。
- Numerical、reporting、documentation toolのtest。
- 明確なplot、example、translation、methodology説明。
- Reproducibility、safety、failure-caseの改善。

`Add noise robustness test` や `Clarify Lyapunov limitations` のような短い命令形commit messageを使います。
