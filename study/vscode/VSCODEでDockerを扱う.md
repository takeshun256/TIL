start：[[2023-03-16]] 09:57

## 参考様

- https://qiita.com/nokoxxx1212/items/da1832468cbd9a762a46

## 入り方

- まず、vscode のターミナルでコンテナを立ち上げる

```python
docker-compose up -d --build
```

- vscode の左下から attach to running container を打って、所望のコンテナに入る
- 入った初期の階層が異なっているがあるので、ワーキングディレクトリに移動する
- PythonExtension を container 内に入れる
