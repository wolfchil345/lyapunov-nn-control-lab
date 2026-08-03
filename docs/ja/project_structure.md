🌐 言語: [English](../en/project_structure.md) | [日本語](../ja/project_structure.md) | [한국어](../ko/project_structure.md) | [ไทย](../th/project_structure.md)

# プロジェクト構成

```text
lyapunov-nn-control-lab/
├── main.py                    # 実験全体の実行パイプライン
├── src/                       # 制御、シミュレーション、解析、レポート作成
├── tests/                     # 自動テスト
├── scripts/                   # 検査、保守、実験支援ツール
├── examples/                  # 実行可能な最小例
├── docs/{en,ja,ko,th}/        # 各言語のドキュメント
├── results/                   # 参照用の図、CSVデータ、レポート
├── .github/                   # ワークフローと貢献用テンプレート
├── pyproject.toml             # パッケージ情報と依存関係
└── README*.md                 # 4言語のエントリーページ
```

## ソースの責務

`src/system.py` はプラントとLQR基準制御器を定義します。制御器の学習は `src/controllers.py` にあり、シミュレーション、評価指標、Lyapunov検査、ロバスト性実験、プロット、レポート作成は目的ごとのモジュールに分けられています。

## 生成ファイル

`results/nn_controller.pt` は実行時に生成され、Git管理の対象外です。一部の図、CSVファイル、レポートは参照用の検証資料として追跡します。コミット前に内容を確認してください。
