start：[[2023-03-24]] 02:04

### requirements.txt を生成する

- 出力形式を f
- 出力ファイル名を o で指定

```python
poetry export -f requirements.txt -o requirements.txt
```

### エラー対処

- black がインストールできない

  - poetry init 時に、black とかを依存関係なしに追加するとエラーが出る。
  - pyproject.toml を削除して、再度 poetry init で何も入れずにインストールすると、うまくいく
    - poetry init 後に、poetry add black isort pytest

- [python - Poetry install on an existing project Error "does not contain any element" - Stack Overflow](https://stackoverflow.com/questions/75397736/poetry-install-on-an-existing-project-error-does-not-contain-any-element) による対処
  - poetry install 時にエラー
