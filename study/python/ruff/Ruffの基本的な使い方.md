start：[[2023-04-04]] 17:42

## 経緯・背景

Rust で書かれており、flake8 より高速かつ拡充されている Ruff という新めのリンターを使いたくなったため。

[GitHub - astral-sh/ruff: An extremely fast Python linter, written in Rust.](https://github.com/astral-sh/ruff)

## 内容

基本的に、ruff src/ tests/のように flake8 と同様に静的チェックが可能

きになる点

- settings.json はどうなるのか
  - pyproject.toml の設定を引き継いてくれる？それとも settings.json 上で設定する？
- ruff は fix も行えるが、静的 ruff + Black が良いかな
- flake8 から ruff に移行する手順
  - [x] flake8 -> ruff の設定
    - [ ] pflake8 の設定だったため、移行不可(pyproject.toml は対応していない)
  - [ ] settings.json を編集
  - [ ] pyproject.toml を編集
  - [ ] Makefile を編集
- [ ] pandas サポート

自分がほしい設定

- ruff による Lint
  - flake8
  - isort
- black による format
- 今までの設定との競合回避

#### Ruff の導入

```python
poetry add --group dev ruff
# poetry add --group dev flake8-to-ruff
```

- Ruff の vscode の拡張機能を入れる
- ついでに、おなじ warning が 2 つ出てくることを防ぐために、flake8 を無効化する

##### flake8-to-ruff

pyproject.toml をサポートしていないので、内容を.flake8 の書き方に chatgpt でかえる

```python
[flake8]
ignore = E203, W503
max-complexity = 12
max-line-length = 88
```

```sh
touch .flake8
vi .flake8
flake8-to-ruff .flake8
rm .flake8
```

出力

```toml
warning: Unsupported prefix code: E203
warning: Unsupported prefix code: W503
Inferred plugins from settings: [
    mccabe,
]
warning: Unsupported prefix code: E203
warning: Unsupported prefix code: W503
[tool.ruff]
ignore = []
line-length = 88
select = [
    "C9",
    "E",
    "F",
    "W",
]

[tool.ruff.mccabe]
max-complexity = 12
```

#### settings.json を編集

```json
{
  "[python]": {
    "editor.formatOnSaveMode": "file", // BlackはSaveModeがfileのみ対応
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": true,
      "source.organizeImports.ruff": true
    },
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

以下削除したもの(これを削除しても拡張機能の flake8 を削除しないと消えないので注意)

```json
  "flake8.args": [
    "--ignore=E203, W503",
    "--max-complexity=12",
    "--max-line-length=88",
  ],
```

いい感じに Linting してくれている

### pyproject.toml を編集

```toml
[tool.ruff]
line-length = 88
select = [
    "I", # isort
    "N", # pep8-naming
    "E", # pycodestyle
    "F", # pyflakes
    "W", # pycodestyle
    "D", # pydocstyle
]
ignore = []
unfixable = ["F401", "F841"]
target-version = "py39"

[tool.ruff.pydocstyle]
convention = "google"

[tool.ruff.mccabe]
max-complexity = 12
```

- doc で D203 と D211 は競合するが、pydocstyle を設定することで防ぐことがきる

削除したもの

```toml
[tool.flake8]
max-line-length = 88
max-complexity = 10
extend_ignore = ["E203", "W503"]
exclude = ["**/__pycache__", "**/.venv", "**/.git", "**/.mypy_cache", "**/.pytest_cache"]
```

#### Makefile

```json
lint:
	-poetry run ruff check $(SRC_DIR)
	-poetry run mypy $(SRC_DIR)

format:
	-poetry run black $(SRC_DIR)
	-poetry run ruff check $(SRC_DIR) --fix-only --exit-zero
```

変更点
![[Pasted image 20230827150209.png]]

#### 使い方

```python
ruff check .                        # Lint all files in the current directory (and any subdirectories)
ruff check path/to/code/            # Lint all files in `/path/to/code` (and any subdirectories)
ruff check path/to/code/*.py        # Lint all `.py` files in `/path/to/code`
ruff check path/to/code/to/file.py  # Lint `file.py`
```

```python
ruff --fix # lint and format
ruff --fix-only # format
ruff --watch # dry run format
```

【メモ】

## 参考

Rust の紹介

- [新しい静的コード解析ツール「Ruff」をご紹介 | gihyo.jp](https://gihyo.jp/article/2023/03/monthly-python-2303)
- [Python の静的解析ツール"Ruff"を導入した話とおすすめの導入方法 - Qiita](https://qiita.com/yuji38kwmt/items/63e82126076204923520)
- [Python の Ruff Linter を VSCode で使う](https://zenn.dev/enven/articles/python-ruff-with-vscode)
- [Python の Ruff Linter を VSCode で使う](https://zenn.dev/enven/articles/python-ruff-with-vscode)

Ruff ドキュメント関連

- [Editor Integrations - Ruff](https://beta.ruff.rs/docs/editor-integrations/)
- Rules
  - [Rules - Ruff](https://beta.ruff.rs/docs/rules/#pyflakes-f)
- repo
  - [GitHub - astral-sh/ruff: An extremely fast Python linter, written in Rust.](https://github.com/astral-sh/ruff)

## まとめ(類似点・相違点)

拡張機能の方に Linter とか Formertter が映ったおかけで設定が簡潔で見やすくなった気がする

## 振り返り

正解はないのだから、自分が開発で必要そうだと思ったものを書くこと

## 次回やること

- [ ] pre-commit

- [ ] git actions

- [ ] tox

[GitHub - astral-sh/ruff: An extremely fast Python linter, written in Rust.](https://github.com/astral-sh/ruff?tab=readme-ov-file#usage)を参考
