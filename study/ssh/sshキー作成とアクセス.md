start：[[2023-06-11]] 22:54

- キー一覧を作成

```python
ls -al ~/.ssh
```

- 1 つの fingerprint とかの情報を表示(キー作成はされない)
  - 別に rsa などで作成すれば安全性は大丈夫っぽい
  - bit 長~~~ (RSA)

```python
ssh-keygen -l -f ~/.ssh/id_rsa.pub
```

- キーを作成

```python
ssh-keygen -t rsa -f key -C ""

cat key | pbcopy
->公開鍵をどこかに渡したりする。
```

- ssh 接続

```python
ssh -i <秘密鍵の絶対パス> ubuntu@ipaddress
```

## 参考

- [お前らの SSH Keys の作り方は間違っている - Qiita](https://qiita.com/suthio/items/2760e4cff0e185fe2db9)
  - github に ssh 接続する方法が書かれている。ありがたい
