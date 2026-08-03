🌐 言語: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# 再現性

## チェックの再現

```bash
python -m pip install -e .
make checks
make quality-gate
```

## 実験の再現

追跡結果をバックアップしてから実行します。

```bash
python scripts/run_full_experiment.py
```

コードではPython、NumPy、PyTorchの乱数シードを設定します。すべての結果に、コミット、Pythonのバージョン、依存関係のバージョン、実験設定を記録してください。

## 想定される差

システムやライブラリのバージョンにより、小さな数値差やPNGエンコードの違いが生じることがあります。変更を採用する前に数値指標を比較し、図はピクセル内容も確認します。

## 範囲

再現性とは、文書化されたパイプラインで同等の証拠を再生成できることです。サンプル点でのLyapunov確認や引き込み領域の評価を、形式的な安定性証明に変えるものではありません。
