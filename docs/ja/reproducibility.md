🌐 言語: [English](../en/reproducibility.md) | [日本語](../ja/reproducibility.md) | [한국어](../ko/reproducibility.md) | [ไทย](../th/reproducibility.md)

# Reproducibility ガイド

このガイドは、Lyapunov Neural-Network Control Lab の主要結果を再現する方法を説明します。

## 1. リポジトリを clone する

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
```

## 2. Python 環境を作成する

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell の場合:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. 依存関係をインストールする

```bash
python -m pip install -e ".[dev]"
```

## 4. テストを実行する

```bash
python -m pytest
```

結果を再生成する前に、すべてのテストが通る必要があります。

## 5. 実験結果を再生成する

```bash
python main.py
```

これにより、成果物の生成・ハッシュ化・manifest 記録・検証が完了した後にのみ、`results/runs/<run_id>/` 配下へ分離された run が公開されます。

重要な run ローカル出力には次が含まれます。

- `manifest.json`
- `SHA256SUMS`
- `report.md`
- `model_architecture.png`
- `performance_metrics.csv`
- paired raw and aggregate ablation/noise CSV files
- normalized-coordinate figures
- `nn_controller.pt`

## 6. 生成プロットを開く

GitHub Codespaces または VS Code で、選択した run directory からファイルを開きます。

例:

```bash
code results/runs/<run_id>/model_architecture.png
code results/runs/<run_id>/report.md
```

## 7. Reproducibility に関する注意

- Python、NumPy、PyTorch CPU、および利用可能な PyTorch CUDA generator は、1 つの project utility で seed されます。固定 seed は同一環境での CPU 比較の再現性を高めますが、CUDA の bitwise deterministic 実行やクロスプラットフォーム実行を普遍的に保証するものではありません。
- Stability weight は全 weight で paired seeds により比較されます。Raw の per-seed trial は、aggregate mean、sample standard deviation、standard error と分離して保持されます。
- Measurement-noise amplitude は common random-number realization を使用します。各 seed の同一 standardized sequence を各 amplitude にスケーリングして使います。Repeated matched seeds は noise realization の交絡を減らしますが、すべての実験不確かさを除去するわけではありません。
- OS、Python version、dependency version の違いにより、小さな数値差が生じる可能性があります。
- このプロジェクトは、neural-network controller に対する完全な形式証明ではなく、経験的 simulation と grid-based Lyapunov checks を使用します。
- 生成プロットは、実用的な stability と robustness の診断を目的としています。
- Finite-horizon convergence figure は、明示された normalized-coordinate grid 上で strict criterion `||x(T)||_2 < epsilon` のみを適用します。これは数学的 attraction-region certificate ではありません。
- `region_of_attraction` で始まる tracked file は historical pre-migration artifact であり、この terminology-only operation では意図的に再生成しません。
- Official run には clean な Git tree が必要です。`--allow-dirty` は manifest に `git_dirty: true` を記録した明示的 exploratory run を作成します。
- `configuration_sha256` は canonical sorted scientific configuration JSON をハッシュします。timestamp と platform metadata は configuration identity に影響しません。
- `python scripts/verify_run.py results/runs/<run_id>` で run を検証してください。

## 8. 推奨検証ワークフロー

新しい実験結果を信頼する前に、次を実行します。

```bash
python -m pytest
python main.py
python scripts/verify_run.py results/runs/<run_id>
python -m pytest
```

これにより、生成前にコードを確認し、公開されたファイル群を正確に検証できます。
