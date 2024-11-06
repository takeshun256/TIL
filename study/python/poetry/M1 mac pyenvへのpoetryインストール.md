start：[[2023-03-21]] 03:15

## 参考

- https://python-poetry.org/docs/ : 公式ドキュメント
- https://github.com/python-poetry/poetry/issues/6854
- https://zenn.dev/yamaday/scraps/51008245130dac
- https://python-poetry.org/docs/#oh-my-zsh

## 内容

今思ったけど、brew install poetry でよかったかも...

### インストール

pyenv でインストールした python は、python3 ではなく、python で実行するので以下を実行

```python
curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python -
```

zshrc に poetry のパスを指定

```python
# poetry path
export POETRY_ROOT="$HOME/.local/"
export PATH="$POETRY_ROOT/bin:$PATH"
```

以下のような古いバージョンに関する警告が出たので、設定ふぁいるを移動

```python
mv /Users/$USER/Library/Application\ Support/pypoetry/config.toml /Users/$USER/Library/Preferences/pypoetry/config.toml
```

### Oh my zsh 用に補完の設定を記載

- https://python-poetry.org/docs/#oh-my-zsh
- あんまり意味ないかも

### poetry の venv をプロジェクト内に作られるようにする

- https://zenn.dev/yamaday/scraps/51008245130dac

```python
poetry config virtualenvs.in-project true
poetry config --list # 確認
```

## まとめ(類似点・相違点)

pyenv 上で実行することに注意

公式ドキュメントを見て、インストールしてみて、エラーが出たら色々調べる

## 振り返り

これで、ローカルで仮想環境を作成できるようになったけど、色々 Docker もしくは conda-forge 上の方が便利な気がしてきた
