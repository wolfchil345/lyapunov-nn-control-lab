🌐 言語: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# 実験ログテンプレート

## 識別情報

- 日付:
- Branchとcommit SHA:
- 研究課題:
- 目的:

## 環境と設定

- PythonとPyTorchのversion:
- Runtime:
- Random seed:
- Epochs, learning rate, dataset size, network architecture:
- Plant, controller, simulation, Lyapunov, noise, parameter設定:

## コマンドと出力

- 使用コマンド:
- Metrics CSV:
- Report:
- Figures:

## 解釈

- 改善点と悪化点は何か?
- LQRと比べてどうか?
- サンプルLyapunov違反またはrobustness failureがあったか?
- 前回runと設定を比較できるか?

## 判断

- Reference resultとして保存する? Yes / No
- Reportまたはpresentationに使う? Yes / No
- 次の実験:

`python scripts/new_experiment_log.py "short description" --language ja` でtimestamp付きcopyを作成できます。
