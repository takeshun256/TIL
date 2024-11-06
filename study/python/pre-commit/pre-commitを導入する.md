start：[[2023-10-08]] 07:18

## 経緯・背景・興味・目標

[[Pythonの開発用テンプレート作成2]] で pre-commit を導入していたが、実際に pre-commit の仕様について調べてみる

## タスク

- [ ] ruff の pre-commit があったら導入する
  - [ ] 変更元としては、flake8, isort らへんが対象になりそう
  - [ ] [Usage - Ruff](https://docs.astral.sh/ruff/usage/)
  - [ ] [GitHub - astral-sh/ruff-pre-commit: A pre-commit hook for Ruff.](https://github.com/astral-sh/ruff-pre-commit)
    - [ ] ruff のやつは、black や isort の後におくべきらしい
    - [ ] これは format -> lint の順が良いためらしい
  - [ ] [[Ruffの基本的な使い方]]
    - [ ] isort は設定で ruff で代用可能
    - [ ] 大体、ruff + black が良さそう

## 内容

### 導入

- [pre-commit](https://pre-commit.com/)：公式インストールドキュメント

```python
# re-commit コマンドを追加
poetry add --group dev pre-commit
poetry run pre-commit --version
touch .pre-commit-config.yaml
(poetry run pre-commit sample-config)

# pre-commit-hookをインストール
poetry run pre-commit install
(poetry run pre-commit uninstall) # uninstall時

# option: pre-commitを全てのファイルに手動で適用してみる
poetry run pre-commit run --all-files
(=poetry run pre-commit run -a)

# 変更をcommit
git add .
git cm -m "add: pre-commit install"  # pre-commit実行される
(git cm --no-verify) # pre-commitを実行しない
```

実行すると一気に変更が入るので注意(Formattter の追加時と同じ)

![[Pasted image 20231008075609.png]]

基本的な `.pre-commit-config.yaml` の表示

```python
$poetry run pre-commit sample-config                                                                             ─╯
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
```

- リポジトリのインストール設定に`pre-commit install` が必要になりそう

commit 時の pre-commit 結果

- これ回るなら、事前に`poetry run pre-commit run --all-files` してても良いかも

### マイカスタマイズ

- mypy と bandit は個人開発にしては制約が厳しすぎるのでコメントアウト

- 注意点として、poetry 環境を使うので、poetry run で commit しなくてはならない...

```python
poetry run git commit -m "..."
```

```python
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      # list of supported hooks: https://pre-commit.com/hooks.html
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: debug-statements
      - id: detect-private-key
      - id: check-yaml
      - id: check-toml
      - id: check-json
        exclude: ^.vscode/
      - id: check-byte-order-marker
      - id: check-docstring-first
      - id: check-executables-have-shebangs
      - id: check-case-conflict
      - id: check-added-large-files

  - repo: local
    hooks:
      - id: black-diff
        name: black-diff
        entry: black
        language: system
        types_or:
          - python
          - pyi
        require_serial: true
        args:
          - "--diff"
          - "--color"
        verbose: true
      - id: black
        name: black
        entry: black
        language: system
        types_or:
          - python
          - pyi
        require_serial: true
      - id: isort-diff
        name: isort-diff
        entry: isort
        language: system
        require_serial: true
        types_or:
          - cython
          - pyi
          - python
        args:
          - "--diff"
          - "--filter-files"
        verbose: true
      - id: isort
        name: isort
        entry: isort
        language: system
        require_serial: true
        types_or:
          - cython
          - pyi
          - python
        args:
          - "--filter-files"
      # - id: mypy
      #   name: mypy
      #   entry: mypy
      #   language: system
      #   types_or:
      #     - python
      #     - pyi
      #   require_serial: true
      #   pass_filenames: false

  # python upgrading syntax to newer version
  - repo: https://github.com/asottile/pyupgrade
    rev: v3.3.1
    hooks:
      - id: pyupgrade
        args: [--py38-plus]

  # python docstring formatting
  - repo: https://github.com/myint/docformatter
    rev: v1.7.4
    hooks:
      - id: docformatter
        args: [--in-place, --wrap-summaries=99, --wrap-descriptions=99]

  # yaml formatting
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.0.0-alpha.6
    hooks:
      - id: prettier
        types: [yaml]

  # shell scripts linter
  - repo: https://github.com/shellcheck-py/shellcheck-py
    rev: v0.8.0.4
    hooks:
      - id: shellcheck

  # md formatting
  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.14
    hooks:
      - id: mdformat
        args: ["--number"]
        additional_dependencies:
          - mdformat-gfm
          - mdformat-tables
          - mdformat_frontmatter

  # word spelling linter
  - repo: https://github.com/codespell-project/codespell
    rev: v2.1.0
    hooks:
      - id: codespell

  # # python security linter
  # - repo: https://github.com/PyCQA/bandit
  #   rev: "1.7.5"
  #   hooks:
  #     - id: bandit
  #       args: ["-s", "B101"]

```

【メモ】

pre-commit で black を使用する hook 設定を使っても black をインストールはしなくて良い

- pre-commi とは別に black をインストールする必要がある

pre-commit の Python 系の hook の設定は、`pyproject.toml` で設定できる

- [Python レポジトリ用の pre-commit 環境を整える](https://rcmdnk.com/blog/2023/02/07/computer-python/)
- なので、Python の依存関係を `pyproject.toml` で管理する `poetry` と管理面で相性が良い=依存関係のバージョンを一緒にできたり

- Python のまとまった設定 - [Python レポジトリ用の pre-commit 環境を整える](https://rcmdnk.com/blog/2023/02/07/computer-python/)
  ![[Pythonレポジトリ用のpre-commit環境を整える.mht]]

repo: local すると、ローカルの依存関係を利用する。ない場合はエラーが出る

- local をつけないと、原則外から持ってきて Initialize する

## 参考

- [Python レポジトリ用の pre-commit 環境を整える](https://rcmdnk.com/blog/2023/02/07/computer-python/)
  - 便利な設定で有効な設定が書いてある
  - pyproject.toml での導入が詳しく書かれている　神!
  - 最後にまとめた Template も置いている
- [.pre-commit-config.yaml](https://github.com/matsuo-group24-PinkTrombone/SpeechGeneration/blob/d1520024727ce7dff12e635963d9212ee04a4ea3/.pre-commit-config.yaml#L5)
  - PinkTrombone での hydra-template の pre-commit のやつ
  - マシマシって感じ
- [pre-commit](https://pre-commit.com/)
  - インストールがわかりやすい
- [pre-commit で ShellCheck を使う](https://rcmdnk.com/blog/2023/01/09/computer-shell-python/)

  - shellcheck の Python 製で pre-commit や poetry で管理できるものの紹介

- [GitHub - nbQA-dev/nbQA: Run ruff, isort, pyupgrade, mypy, pylint, flake8, and more on Jupyter Notebooks](https://github.com/nbQA-dev/nbQA)

  - ノートブック系に強い Lint, Format

- [pre-commit でコミット時にコードの整形やチェックを行う](https://zenn.dev/yiskw713/articles/3c3b4022f3e3f22d276d)
- [pyproject-pre-commit: Python プロジェクト用の pre-commit 集](https://rcmdnk.com/blog/2023/05/01/computer-python/)

## 振り返り

大体こういうのはできもののやつを使うのが良いのかも

- hydra-template とか...

それか必要最低限のもの

- pre-commit で pr workflow よりも厳格なルールのため、厳しすぎると大変
- pre-commit のデフォルトのやつと、ruff と black くらいで良いかも
