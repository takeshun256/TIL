start：[[2023-10-07]] 09:48

### 参考

- [Dependabot を導入してみた | DevelopersIO](https://dev.classmethod.jp/articles/dependabot-101/)
  - 使ってみた記事
  - これ古いかも
- [Dependabot を使う - GitHub Docs](https://docs.github.com/ja/code-security/dependabot/working-with-dependabot)
  - ドキュメント
  - [Dependabot を使用してサプライ チェーンを安全に保つ - GitHub Docs](https://docs.github.com/ja/code-security/dependabot)
- [Dependabot を導入してライブラリのアップデートを習慣化した話 - M&A クラウド開発者ブログ](https://tech.macloud.jp/entry/2022/07/27/182109)
  - もっと踏み込んで、使ってみてどういうことに気をつけたら良いか
- [Dependabot 全体像とバージョンアップ戦略](https://zenn.dev/sumiren/articles/ffe6c0bd772718)
  - 色々なカスタマイズ
  - 仕組みが多いな...
  - リポジトリごとに最適化する必要がありそう
- [GitHub に Dependabot を導入して依存ライブラリを自動アップデートする | DevelopersIO](https://dev.classmethod.jp/articles/github-dependabot-2021/)
  - 導入記事参考
- [Dependabot と Github Actions で自動バージョンアップを実現する話 - Qiita](https://qiita.com/t-okibayashi/items/0ed33ff9c34c50e1582c)
  - 導入記事参考 2 つ目

### 導入

1. リポジトリの insight/dependency graph /dependabot で Enable にする
2. GUI 上で create config するか、ローカルで yaml ファイルを作成して push する

```bash
touch .githuub/dependabot.yml # workflows下ではないので注意
```

```python
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
      time: "14:00"
      timezone: "Asia/Tokyo"
    target-branch: "main"
```

- 監視したいディレクトリパスは、`directory` で設定する
- Docker とか pip とかのパッケージの種類は、`package-ecosystem`で指定する
- schedule で定期実行

【メモ】

dependabot の導入は、Private リポジトリだと、設定ファイルを配置することで有効化される.

- [Dependabot と Github Actions で自動バージョンアップを実現する話 - Qiita](https://qiita.com/t-okibayashi/items/0ed33ff9c34c50e1582c)

dependnecy graph を enable するとリポジトリ内の依存関係が全て把握できるらしい

## 次回やること

[Dependabot と Github Actions で自動バージョンアップを実現する話 - Qiita](https://qiita.com/t-okibayashi/items/0ed33ff9c34c50e1582c)
