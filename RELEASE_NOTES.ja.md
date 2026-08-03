🌐 言語: [English](RELEASE_NOTES.md) | [日本語](RELEASE_NOTES.ja.md) | [한국어](RELEASE_NOTES.ko.md) | [ไทย](RELEASE_NOTES.th.md)

# v1.0.1 - ドキュメントとリリースの改善

このパッチリリースは、中核となる制御実験を変更せずに、インストールの信頼性、多言語ドキュメント、結果サマリーの出力を改善しました。

## 主な変更

- 不足していた実行時依存関係 `python-control` を追加
- 生成された仮想環境ファイルとパッケージメタデータを Git の対象外に設定
- 英語、日本語、韓国語、タイ語のドキュメント基盤を追加
- 4言語それぞれのドキュメント索引を追加
- 各 README から対応する言語のドキュメント索引へリンク
- 古いリンクと存在しないドキュメントへのリンクを削除
- アブレーションサマリーが `lyapunov_violation_fraction` を読み込むよう修正
- 今後のバージョンタグで使えるようリリースチェックリストを一般化

## 検証

- 57件のテストが合格
- クイックスタート例が合格
- 品質ゲートが合格
- 固定した乱数シードで実験結果の再生成に成功
- 再生成した図は、従来 Git で管理していた図とピクセル単位で一致
- Lyapunov グリッド検査の違反数は0
- 試験した制御器の引き込み領域検査では100%収束

## 互換性

中核となるシミュレーション、制御器アーキテクチャ、Git で管理する実験結果は `v1.0.0` から変更していません。

---

# v1.0.0 - 最初の完全版リリース

Lyapunov Neural-Network Control Lab の最初の完全版リリースです。

## 主な機能

- LQR 基準制御器
- 模倣学習で学習したニューラルネットワーク制御器
- Lyapunov 理論に基づく安定性検査
- 安定性を考慮した学習ペナルティ
- アクチュエータ飽和実験
- 計測ノイズに対するロバスト性実験
- パラメータ変動に対するロバスト性実験
- 位相面図の可視化
- Lyapunov 等高線の可視化
- 引き込み領域の推定
- 制御器ごとの引き込み領域の比較
- 安定性重みのアブレーションスタディ
- 実験レポートの自動生成
- モデルアーキテクチャ図
- 手法のドキュメント
- プロジェクト概要のドキュメント
- 引用メタデータ

## 主な出力

- `results/model_architecture.png`
- `results/position_comparison.png`
- `results/training_loss.png`
- `results/saturation_comparison.png`
- `results/noise_robustness.png`
- `results/parameter_robustness.png`
- `results/phase_portrait.png`
- `results/lyapunov_contours.png`
- `results/region_of_attraction.png`
- `results/region_of_attraction_comparison.png`
- `results/stability_weight_ablation.png`
- `results/experiment_report.md`

## 研究の焦点

このプロジェクトは、安定化可能な古典制御器をニューラルネットワーク制御器が模倣し、その挙動を Lyapunov 安定性の観点から評価できるかを研究します。
