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

CodeはPython、NumPy、PyTorchをシードします。全結果にコミット、Python バージョン、依存関係 バージョン、実験 設定を記録してください。

## 想定される差

システムやlibrary バージョンにより小さな数値差やPNG encoding差が生じることがあります。変更採用前に数値指標を比較し、図はpixel contentを確認します。

## 範囲

再現性とは文書化された パイプラインで同等の証拠を再生成できることです。サンプルLyapunovや引き込み領域 確認を形式的安定性証明に変えるものではありません。
