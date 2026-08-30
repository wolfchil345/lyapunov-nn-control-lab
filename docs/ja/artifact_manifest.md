🌐 言語: [English](../en/artifact_manifest.md) | [日本語](../ja/artifact_manifest.md) | [한국어](../ko/artifact_manifest.md) | [ไทย](../th/artifact_manifest.md)

# Artifact Manifest

このドキュメントは、Lyapunov neural network control lab で生成または使用される主要ファイルを説明します。

## 目的

このプロジェクトは、neural network 制御の性能、Lyapunov 安定挙動、ロバスト性、再現性を評価するために、プロット、レポート、サマリーファイルを生成します。

## 主なソースファイル

| Path | Purpose |
| --- | --- |
| `main.py` | メイン実験パイプラインを実行します。 |
| `src/system.py` | 質量ばねダンパ系と LQR 参照制御器を定義します。 |
| `src/controllers.py` | neural network 制御器、学習データ、Lyapunov-aware training logic を定義します。 |
| `src/simulation.py` | 閉ループ系の挙動をシミュレーションします。 |
| `src/lyapunov.py` | Lyapunov 値と Lyapunov derivative grid checks を計算します。 |
| `src/metrics.py` | 状態誤差、制御努力、コストなどの performance metrics を計算します。 |
| `src/plotting.py` | 軌道、位相平面、ロバスト性、安定性解析の図を生成します。 |
| `src/lyapunov_nn_control_lab/finite_horizon_convergence.py` | 明示的 finite horizon で bounded grid 上の strict final-state tolerance を評価し、sampling metadata を記録します。 |

## 主なスクリプト

| Path | Purpose |
| --- | --- |
| `scripts/run_checks.py` | ドキュメントリンクチェック、ユニットテスト、quick start example を実行します。 |
| `scripts/run_full_experiment.py` | 非破壊の full experiment workflow を実行します。 |
| `scripts/verify_run.py` | 完了した manifest と記録された SHA-256 checksums を検証します。 |
| `scripts/summarize_results.py` | 生成された実験出力を要約します。 |
| `scripts/clean_results.py` | 新しい実行が必要なときに生成済み result artifacts を削除します。 |
| `scripts/check_docs_links.py` | ドキュメント内部リンクをチェックします。 |

## 結果アーティファクト

Historical files は `results/` 直下に維持されます。新しい出力は `results/runs/<run_id>/` に分離され、run 間で混在しません。

| Artifact type | Meaning |
| --- | --- |
| Trajectory plots | 異なる制御器下での状態応答を比較します。 |
| Control plots | 制御入力挙動と saturation の影響を比較します。 |
| Lyapunov plots | Lyapunov 関数の挙動と導関数領域を可視化します。 |
| Finite-horizon convergence plots | horizon、tolerance、bounds、grid、counts を明示した sampled final-state tolerance 結果を示します。attraction-region certificate ではありません。 |
| Robustness plots | noise または parameter variation 下での制御器挙動を示します。 |
| CSV summaries | 比較・報告用の数値 metrics を保存します。 |
| Experiment reports | 主要な数値結果と可視化結果を説明します。 |

## Reproducibility note

最終的な thesis 図を作成する前に、ローカルチェックを実行し、clean な Git 状態から official run を作成してください。

```bash
python scripts/run_checks.py
python main.py
python scripts/verify_run.py results/runs/<run_id>
```

`manifest.json` には schema version、Git provenance、runtime versions、effective configuration、exact seeds、pairing methodology、inventory、sizes、hashes が記録されます。legacy-artifact policy は [`../../results/README.md`](../../results/README.md) を参照してください。

## このドキュメントの使い方

thesis、プレゼンテーション、研究ミーティングでリポジトリ構造を説明する際に、この manifest を使用してください。
