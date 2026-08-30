🌐 言語: [English](CONTRIBUTING.md) | [日本語](CONTRIBUTING.ja.md) | [한국어](CONTRIBUTING.ko.md) | [ไทย](CONTRIBUTING.th.md)

# コントリビューティングガイド

Lyapunov NN Control Lab への貢献ありがとうございます。以下は開発者が実装やドキュメント、テストを変更するときに従うべき手順と推奨事項です。

## 開発環境のセットアップ

```bash
git clone https://github.com/wolfchil345/lyapunov-nn-control-lab.git
cd lyapunov-nn-control-lab
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## テストの実行

```bash
python -m pytest
```

## 実験の実行（ローカル）

```bash
python main.py
```

## ブランチワークフロー

変更を行う前に機能ブランチを作成してください。

```bash
git switch main
git pull origin main
git switch -c feature/your-feature-name
```

## コミットのスタイル

短く明瞭なコミットメッセージを使ってください。例:

- Add noise robustness experiment
- Add reproducibility guide
- Fix Lyapunov metric handling

## 推奨される貢献領域

- 新しいコントローラ基準の追加
- 追加のロバストネス実験
- プロットやドキュメントの改善
- 数値ユーティリティのためのテスト
- 初学者向けの実例追加

## 変更を送る前に

テストや主要な例を実行して、変更が既存の動作を壊していないことを確認してください。

```bash
python -m pytest
python main.py
```

上記は日本語訳ですが、コマンドやファイル名は原文どおりに記載しています。
