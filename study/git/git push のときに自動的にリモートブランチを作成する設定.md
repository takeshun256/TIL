start：[[2023-09-25]] 13:57

## 内容

- [git push のときに自動的にリモートブランチを作成する設定](https://shogo82148.github.io/blog/2022/08/11/2022-08-11-git-push-auto-setup-remote/)

以下を実行することで、pushすると自動でブランチを発行してくれるようになる
```
git config --global --add --bool push.autoSetupRemote true
```


結構、誤爆の多そうなので、localで指定するのが良さそう

```python
git config --local --add --bool push.autoSetupRemote true
```

