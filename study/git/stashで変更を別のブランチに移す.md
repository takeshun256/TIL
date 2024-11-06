start：[[2023-10-07]] 07:40


```python
# 変更をGit管理下に入れる
git add -A
# 変更をstashに保存する
gi stash

# ブランチを作成する
git swc feature/**

# stashから変更を取り出して適用する
git stash pop
```

すでにcommitしている場合は、comitの取り消しが必要になってくる
