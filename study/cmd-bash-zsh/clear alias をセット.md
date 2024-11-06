start：[[2024-07-04]] 02:57

bashrc に設定

```python
alias cls="echo -ne '\033c'"
```

=> エスケープシーケンスを送信することでターミナルリセットしているらしい \ec?
=> これは、ほぼ端末リセットなので注意 =reset

【メモ】

corsor でショートカットの設定は、ctrl+M ctrl+S

ショートカットが衝突するときは、不要なバインドを解除するか or 新しく短い alias を登録する

設定は簡単
ctrl , で設定とか
ctrl + M ctrl + S
