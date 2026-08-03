🌐 言語: [English](../en/experiment_log_template.md) | [日本語](../ja/experiment_log_template.md) | [한국어](../ko/experiment_log_template.md) | [ไทย](../th/experiment_log_template.md)

# 実験ログテンプレート

## 基本情報

- 日付:
- ブランチとコミットSHA:
- 研究課題:
- 目的:

## 実行環境と設定

- PythonとPyTorchのバージョン:
- 実行環境:
- 乱数シード:
- エポック数、学習率、データセットサイズ、ネットワーク構成:
- プラント、制御器、シミュレーション、Lyapunov、ノイズ、パラメータの設定:

## 実行コマンドと出力

- 使用したコマンド:
- 評価指標のCSV:
- レポート:
- 図:

## 結果の解釈

- 改善した点、または悪化した点は何か?
- LQRと比較して制御器はどのように振る舞ったか?
- サンプル点でLyapunov条件の違反やロバスト性の問題があったか?
- 前回の実験と設定を比較できるか?

## 判断

- 参照結果として保存するか? はい / いいえ
- レポートや発表に使用するか? はい / いいえ
- 次の実験:

`python scripts/new_experiment_log.py "short description" --language ja`で、タイムスタンプ付きのコピーを作成できます。
