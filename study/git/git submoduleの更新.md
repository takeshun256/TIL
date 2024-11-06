start：[[2023-07-31]] 05:31

### submodule の更新

- とても参考

  - [git-submodule と git-subtree](https://zenn.dev/hikarin/articles/8701ed06fcb6e3a17eaf#%E5%8F%82%E7%85%A7%E3%81%99%E3%82%8B%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88%E3%81%AE%E5%A4%89%E6%9B%B4)

- <span style="background:#ff4d4f">submodule では必ずブランチを切って作業するべき</span>

  - detach の話もある
  - [git-submodule と git-subtree](https://zenn.dev/hikarin/articles/8701ed06fcb6e3a17eaf#submodule%E3%81%AE%E7%B7%A8%E9%9B%86)

- git submodule とすると、現在の親レポジトリと対応する submodule バージョンになる。
- -> submodule の commit は update されない
  - もしかしたら、submodule が detach じゃなければ違う？

#### <u>状態としたいこと</u>

【状態】
親ディレクトリで以下のような submodule の状態だとする。

- `(new commits)`：submodule の状態が変更されてそれが commit もされている状態
- `(modified content)`： submodule の状態が変更されて、それが commit されていない
- `(untracked content`：submodule の状態が変更されて、それが git 管轄でない
  - git 管轄のものが変更されてもそれは untracked にはならないので、新しくファイルが作成されている状態

submodule 内は detached されている状態になっていることがある

【したいこと】

1. submodule 内へ移動する
2. submodule 内で、ブランチを切って、そこで変更を commit する
   1. `takeshun256/add-new-files`
3. その変更を Fork したものへ push する
   1. `git push origin <branch: takeshun256/add-new-files>`
4. 親ディレクトリへ移動する(この時の git st が、上記の modified の状態)
5. git add
6. `git cm -m "update submodules"`
7. `git push origin main`

#### 実行

```sh
# submoduleは、jvs_hihoとする。
cd jvs_hiho
git st
# Detachの場合は、特定の切り離されたcommitの状態になっている。
git br -a

(git fetch origin)

git add .
git stash
git sw main
git swc takeshun256/add-new-files
(git sw takeshun256/add-new-files) # remoteにすでにあるなら
git add .
git cm -m "add: new-files"

# submoduleディレクトリで変更をブランチ切ってpush
cd ..
git st
git add .
git st # 緑色になるはず
git cm -m "update submodule"

# 親ディレクトリで変更をpush
git remote -vv # ちゃんとforkしたものを使用しているか
git push origin main
(git remote add takeshun git+...takehsun...)
(git remote -vv) # takeshunが追加されているはず
(git push takeshun main)

(gh rvw) # remoteが複数あり設定できていないので見れないことがある
```

- この後、別の clone から pull する場合

```python
git pull
git st
git submodule update
```

- 2 つ誤って実行した push の取り消し

```python
# 2つ前のcommitへ戻り、その変更を全てnot stagedへ
git reset HARD~2

---
# その後、別のブランチを切ってそれをpush
git add .
git stash
git swc <branch>
git stash pop
git add .
git cm
git push origin <branch>

# mainの変更を戻す
git sw main
git add .
git cm
git push
```

どうしても `gitignore`の変更でデータファイルが変更に出る場合は、info/exclude する

- 2 つ stash して 2 つ pop する

```python
git add .
git stash
--何らかの変更
git add .
git stash

# ブランチ切る
git swc <branch>
git stash list
git stash pop stash@{0}
git stash pop stash@{1}
```

- untracked を全て削除

```sh
git clean -n # dry-runで確認できる

git clean -f # untrackedを全て削除
```

- remote の変更も消した場合は force する
  - `git push origin +main`
  - `+`は force push
