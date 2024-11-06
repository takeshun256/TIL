start：[[2024-10-23]] 19:06

## 内容

要件/手順

1. 新しく Github 上で Private リポジトリを作成
2. remote リポジトリを書き換え
3. 既存の remote リポジトリへの push を禁止
4. 現在の branch の upstream を変更

```python
# remote repo確認
git remote -vv

git remote rename origin sample-origin

git remote add origin git@github.com:〜.git

git remote set-url --push sample-origin no_push

# upstream確認 => sample-originがデフォルトになっているはず
git for-each-ref --format='%(refname:short) %(upstream:short)' refs/heads/
git branch -M main
git branch --set-upstream-to=origin/main

# 問題なければprivateへpushされる
git push
git pull
```
