start：[[2023-03-24]] 18:41

## 経緯・背景

poetry shell をしても入れない

- source .venv/bin/activate すると入れる
- poetry run でも一時的に入れる

## 参考

- [poetry shell does not activate virtualenv · Issue #571 · python-poetry/poetry · GitHub](https://github.com/python-poetry/poetry/issues/571#issuecomment-470734363)

## 内容

原因

- pyenv と poetry の設定を zprofile ではなく zshrc に書いているのが原因らいい
- [poetry shell does not activate virtualenv · Issue #571 · python-poetry/poetry · GitHub](https://github.com/python-poetry/poetry/issues/571#issuecomment-470734363)

解決策

- zshrc の pyenv と poetry のパス設定を zprofile に移動

解決しない...
直接 venv のやつを source する方法でお願いします!
