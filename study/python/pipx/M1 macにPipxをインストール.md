start：[[2023-03-21]] 04:52

## 経緯・背景

docker を調べているときに pipx というものを発見した

- https://github.com/devcontainers/images/tree/main/src/python
  pip が拡張されたもの

## 参考

公式 Doc

- https://pypa.github.io/pipx/

## 内容

### インストール

```bash
brew install pipx
pipx ensurepath
```

### Pipx の立ち位置

- mac の homebrew に似ている、アプリ管理用のコマンド
- pip よりも環境分離がしやすいらしい
- pip よりも安全便利信頼の場所からインストールする
- install と unsintall が隔離された環境で実行できる
  - 依存関係でエラーが出ることがない
- pipx は sudo で実行する必要がない
- pipx install package で自動的に仮想環境を作成し、パッケージの関連アプリケーション(エントリポイント)を PATH 上の場所に追加
  - グローバルにパッケージを利用できるようになるが、パッケージは独自の仮想環境でまとめられる。
- pipx run で一時的に最新バージョンの状態を作成して実行できる
  - poetry run に近いかも

* グローバル環境で使用するのに向いているので、仮想環境上で、pipx を使用する必要はない
  - そもそも、バージョンがそれぞれ固有なのでグローバルで使うことがない...

## まとめ(類似点・相違点)

pipx は入れておいて損はなさそう
使用例

- https://github.com/rasa/python-best-practices-cookiecutter
