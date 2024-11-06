start：[[2023-03-15]] 12:50

## 内容

まず、問題は多分、ローカルとリモートが異なる履歴(それぞれ別々で初期化した場合)であるのにファイル構成が別々の場合で起きる。

まず、新しく作成する場合は、以下の 2 つ方法がメインである。

1. git clone
2. git init / git remote add origin url/ git add . / git cm /git br -M main/git push -u origin main

この時、どちらにも変更がある場合は諦めて、上記の 2 つのどちらかを選択することをお勧めする。一応以下の方法がある

```python
git init
git remote add origin url
git fetch origin
git merge origin/main --allow-unrelated-histories
git add -A
git cm -m "Initial commit"
git br -M main
git push -u origin main
```

あと、README はリモートでは作成しない方がよい

## まとめ(類似点・相違点)

どちらもに変更がある場合は、git graph が枝分かれした状態のなので、それを避けることが重要
