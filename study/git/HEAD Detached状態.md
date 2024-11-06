start：[[2023-02-11]] 08:00

## 経緯・背景

以下のようなエラーになったため、これを理解して、解決策を知る。

```bash
❯ git status
HEAD detached at origin/#208monitor_resource
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore

no changes added to commit (use "git add" and/or "git commit -a")
```

## 参考

- https://www.r-staffing.co.jp/engineer/entry/20201225_1
- https://qiita.com/Kuniwak/items/4e5d55d6888e5f6411fe

## 内容

- detached HEAD 状態
  - ブランチがない危険な状態
  - HEAD が commit id を直接指している状態

通常状態：HEAD -> branch -> commit-id
detached HEAD 状態 : HEAD -> commit-id

- 原因

  - git checkout commit-id とかで編集をしたため。

- 問題点

  - checkout とかすると、これまでの編集が消える
    - 実際に消えた...あれは detached HEAD の状態がだったからか...

- 解決策
  - detached HEAD の状態でチェックアウトしているコミットの上で、ブランチを作成
    - git branch ブランチ名
  - HEAD の参照先の SHA1 を特定して、どこのブランチのものかを特定して、そのブランチを作成
    - このブランチは、だいたい本来 checkout したかったブランチ名
    - https://qiita.com/Kuniwak/items/4e5d55d6888e5f6411fe

ただし、今回僕は、remote/origin/ブランチ名に checkout を間違えてしてしまっているようで、この方法では解決できない、

- git checkout origin/ブランチ名 をやって編集しているよう...

一時の変更であったため消去されてよく、git checkout で変更を全て消去されて、別のブランチへチェックアウトして解決した。

## 類似点・相違点・まとめ

- HEAD detached 状態は、HEAD がブランチではなく、commit-id を直接指定してしまっている状態、
  - このままだと、別のブランチにチェックアウトすると、変更が消えてしまう。
  - git branch ブランチ名で解消することができる。
