🌐 言語: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# 再現性

## チェックの再現

```bash
python -m pip install -e .
make checks
make quality-gate
```

## 実験の再現

追跡resultをbackupしてから実行します。

```bash
python scripts/run_full_experiment.py
```

CodeはPython、NumPy、PyTorchをseedします。全resultにcommit、Python version、dependency version、experiment settingを記録してください。

## 想定される差

Systemやlibrary versionにより小さな数値差やPNG encoding差が生じることがあります。変更採用前に数値metricを比較し、figureはpixel contentを確認します。

## 範囲

再現性とはdocumented pipelineで同等の証拠を再生成できることです。サンプルLyapunovやregion-of-attraction checkを形式的安定性証明に変えるものではありません。
