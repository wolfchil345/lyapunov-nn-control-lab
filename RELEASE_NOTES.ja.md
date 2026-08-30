🌐 言語: [English](RELEASE_NOTES.md) | [日本語](RELEASE_NOTES.ja.md) | [한국어](RELEASE_NOTES.ko.md) | [ไทย](RELEASE_NOTES.th.md)

# v1.0.1 - ドキュメントとリリースの仕上げ

このパッチリリースは、コア制御実験を変更せずに、インストールの信頼性、多言語ドキュメント、結果サマリ報告を改善します。

## ハイライト

- 不足していたランタイム依存関係 `python-control` を追加
- 生成される仮想環境ファイルとパッケージメタデータファイルを無視対象に追加
- 英語・日本語・韓国語・タイ語のドキュメント基盤を追加
- 4言語すべてに対してローカライズ済みドキュメント索引を追加
- 各 README を対応するローカライズ済みドキュメント索引へリンクするよう更新
- 廃止済みおよび存在しないドキュメントリンクを削除
- アブレーション要約が `lyapunov_violation_fraction` を参照するよう修正
- 将来のバージョンタグに対応できるようリリースチェックリストを一般化

## 検証

- 57 テストが通過
- クイックスタート例が通過
- クオリティゲートが通過
- 固定乱数シードで実験結果を再生成成功
- 再生成した結果図は、以前に追跡されていた図とピクセル単位で一致
- Lyapunov グリッドチェックは違反ゼロを報告
- 歴史的な有限時間チェックでは、テスト対象コントローラと設定で最終状態許容誤差の満足率が 100% と報告された。これは数学的な引き込み領域証明ではない

## 互換性

コアシミュレーション、コントローラアーキテクチャ、追跡対象の実験結果は `v1.0.0` から変更ありません。

---

# v1.0.0 - 最初の完全リリース

これは Lyapunov Neural-Network Control Lab の最初の完全リリースです。

## ハイライト

- LQR ベースラインコントローラ
- 模倣学習で学習したニューラルネットワークコントローラ
- Lyapunov に着想を得た安定性チェック
- 安定性を意識した学習ペナルティ
- アクチュエータ飽和実験
- 測定ノイズに対するロバスト性実験
- パラメータロバスト性実験
- フェーズポートレート可視化
- Lyapunov 等高線可視化
- 標本化有限時間収束マッピング（元リリースでは旧来用語で説明）
- 有限時間のコントローラ比較（元リリースでは旧来用語で説明）
- 安定性重みアブレーション研究
- 自動実験レポート生成
- モデルアーキテクチャ図
- 方法論ドキュメント
- プロジェクト要約ドキュメント
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

## 研究上の焦点

このプロジェクトは、ニューラルネットワークコントローラが LQR 参照を模倣できるかどうかを、過渡特性、ロバスト性、標本化 Lyapunov 診断で評価することを研究します。公称の無制御プラントはすでに漸近安定です。
