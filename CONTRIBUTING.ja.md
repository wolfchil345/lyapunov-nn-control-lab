🌐 言語: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# コントリビューションガイド

Lyapunov NN Control Lab の改善にご協力いただき、ありがとうございます。

## セットアップ

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## 作業手順

1. 最新の `main` から目的を限定したブランチを作成します。
2. 科学的変更、コード変更、ドキュメント変更の範囲を明確に分けます。
3. 動作を変更した場合はテストを追加します。
4. 利用者向けのドキュメントを英語、日本語、韓国語、タイ語の4言語で更新します。
5. `git diff --check`、`make checks`、`make quality-gate` を実行します。
6. プルリクエストを作成し、必須チェックがすべて完了してからマージします。

## 科学的結果

変更に必要な場合を除き、結果の再生成やコミットは行いません。乱数シードと実験設定を記録し、数値と図の差分をすべて確認した上で、サンプル点に基づく安定性の証拠を正確に説明してください。

## 歓迎する貢献

- 基準制御器と、慎重に設計されたロバスト性実験。
- 数値計算、レポート生成、ドキュメントツールのテスト。
- より明確な図、例、翻訳、手法の説明。
- 再現性、安全性、失敗例に関する改善。

コミットメッセージには、`Add noise robustness test` や `Clarify Lyapunov limitations` のような短い命令形を使ってください。
