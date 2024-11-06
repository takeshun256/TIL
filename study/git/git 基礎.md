start：[[2023-02-02]] 21:13

## 参考

スライド一覧

- https://www.sejuku.net/blog/5915

## 内容

### git 名称などのメモ

- commit 系列=コミットグラフ
  - たどって最古まで行くことができる
  - old(parent) <-- new(child) <-- ...
- commit はリビジョン(系列のある時の標子)
- git log は commit の親子の系列
  - 系列はフォークとかで分岐する。
- branch は、commit の系列の中に 1 点にタグをつく
  - ブランチは最新コミットの別名
  - git branch topic master
    - master から topic を作る
    - master = topic となる
- checkout は、commit 系列の好きな場所に移動する。
- 戻す
  - commit <--> reset
  - add <--> checkout
- diff
  - git diff: 前回の commit からのワークディレクトリ(.git が置かれているところ) の更新を表示
  - git diff HEAD
  - git diff --cached
- merge
  - fast-forward: 早送り
    - topic が master に commit を追加した単純なものなら、マージ(差分を見て調整)せずに、topic のリビジョンに master をそのまま進める。
      - master のコミットに、topic のコミットをそのまま足して、最終的に master=topic とする
      - topic の中に master の変更が全て入っている状態(わかりやすい)
    - まーじコミットにならない。
      - topic を戻すと、master はそのままコミットしている状態と等価になる。
      - revert や reset で commit=リビジョンを指定するときに、そのマージを捉えられなくなる。
  - non fast-forward : 分岐している(master も進んで, topic も進んでいる状態)
    - 早送り(fast-forward )ができない(マージ後の master != topic)
    - まーじコミットになる
    - 両方の変更を反映して、master とする。
  - git merge topic
    - 早送りできるなら、fast-forward して、できないなら、non fast-forward
  - topic から、git merge master
  -
  - git merge --no-ff
    - 常に、 non fast-forward
    - fast-forward のマージの取り消しずらさの問題やマージの履歴を見れないことから、fast-forward をしないこちらがおすすめ
  - git merge --ff-only
    - 常に、 fast-forward , できなければエラー
- git revert [commit]
  - commit=リビジョンを取り消すためのコミットを作る。
- git reset --hard [commit]
  - commit=リビジョン時点まで完全に巻き戻す
- rebase
  - ブランチをあたかも現在の master から伸ばしたかのようにする。
    - マージの記録はのこらない!!
    - マージ直前にやるとログが綺麗になる。
  - 分岐した状況で、topic から git rebase master する
    - topic ブランチの commit をパッチとして全て取り出す。
    - master に topic を移動させる。
    - そこから、topic ブランチに対して、順にパッチを適用する。
    - ただし、元の commit とパッチに適用するコミットのリビジョンは別物
  - rebase 後に push するとエラーになることがある。
    - すでに push したブランチに対して、rebase すると、push した際に新しいリビジョンの情報の中の 1 つ前のリビジョンを参照するが、それは rebase 前のリビジョンを参照しており、それは origin ではすでに子が作られているため、エラーになる。
  - 上記から、共有ブランチでは rebase してはいけない。
    - push -f で上書きでキルが、コミットログがおかしくなるのでやめる。
  - コンフリクト時の違い
    - merge は 1 回のコンフリクト解消ですむ
    - rebase は変更を commit ごとにパッチにして順に適用するので、複数回コンフリクトが 1 度に発生することがある。
      - 解決後、再開 or 中断 or スキップするが選べる。
      - つまり、コンフリクト解決のためのコード編集が終わっても rebase フェーズにあり、以下のどれかを入力する必要がある
        - git rebase --continue: マージコミットを作成して中断
        - git rebase --abort: rebase 自体を中断
        - git rebase --skip: 今のパッチをスキップして再開
  - rebase -i commit で過去のコミットをまとめられる。
    - これにも push 後の rebase 付加の問題があるので、旧友レポジトリ等では行わない。
  - Github のオープンソースプロジェクトで PR を送るさいは、rebase してから送るマナーがある。
- push
  - git push origin topic
    - topic を origin(サーバー)へ同期
  - 以下は等価
    - git push remote branchname
    - git fetch origin && git merge origin/master
    -
- commit に入っているもの
  - リビジョン: commit hash(SHA-1 ハッシュ)
  - author: コミットの作成者
  - committer: 受け取ったパッチを取り込んだ人?
  - tree: コミットの変更
  - 1 つ前のコミットのリビジョン

| 意味                                                               | コマンド                                                    |
| ------------------------------------------------------------------ | ----------------------------------------------------------- |
| 直前の commit に commit する                                       | git commit --amend                                          |
| エディターを起動せずにコミット                                     | git commit -m "message"                                     |
| ローカルブランチと同名のリモートブランチを作成                     | git push remote localbranchname                             |
| push したブランチを追跡にもする                                    | git push -u remote brachname                                |
| リモートブランチ削除                                               | git push --delete remote branchname                         |
|                                                                    | git branch -r -d remote/branchname                          |
| タグをリモートに反映                                               | git push --tags remote                                      |
| リモートタグ削除                                                   | git push --delete remote tagname                            |
| 追跡先を設定(remote や branch の省略が可能に)                      | git branch --set-upstream localbranchname remote/branchname |
|                                                                    | git branch --set-upstream-to remote/branchname              |
|                                                                    | git branch -u remote/branchname                             |
| リモートブランチの追跡を作成してチェックアウト                     | git checkout -t remote/branchname                           |
|                                                                    | git fetch origin;git checkout branchname                    |
| コミット前の変更を取り消す                                         | git checkout [path]                                         |
| すべてのリモートブランチの追跡ブランチを更新                       | git fetch --all                                             |
| 更新後、リモートサーバにない追跡ブランチを削除                     | git fetch --prune                                           |
| pull                                                               | git pull remote branchname                                  |
| ahead や behind 表記で 1 行で status 表示                          | git status -sb                                              |
| ファイル削除                                                       | git rm filename                                             |
| ディレクトリ削除                                                   | git rm -r dirname                                           |
| ステージングから削除(ステージング解除)                             | git rm --cached filename                                    |
| 直前の commit をステージング状態へ戻す                             | git reset --soft HEAD~                                      |
| 直前の commit を完全に編集状態へ戻す                               | git reset HEAD~                                             |
| 直前の commit を完全に編集状態に戻す+Untrack のものを削除          | git reset --hard HEAD~                                      |
| ある commit リビジョンまで戻す                                     | git reset [commit]                                          |
| リモートの追加削除                                                 | git remote add origin url / remote rm origin                |
| リモートサーバーに存在しない追跡ブランチ削除                       | git remote prune origin                                     |
| タグの作成・削除                                                   | git tag tagname [commit]/ tag -d tagname                    |
| ログを見る                                                         | git log                                                     |
| ログのハッシュと派生したブランチを見やすく(めちゃ見やすい)         | git log --oneline -decorate                                 |
| 変更されたファイルとパッチも見る(git log の変更数や変更箇所も出力) | git log --stat / log --patch-with-stat                      |
| 過去 commit を取り消す(打ち消すコミットを指定)                     | git revert [commit]                                         |
| topic ブランチの内容を main へ反映(merge)する                      | main ブランチ上で git merge topic                           |
|                                                                    |                                                             |

マージ時の conflict 画面意味

```bash
<<<<<<<<<<<<<<<<<<
merge前の状態 = pushならremoteの状態
==================
mergeしたい差分 = pushならlocalの状態
>>>>>>>>>>>>>>>>>>
```

- commit message editer の環境変数を設定
  - export GIT_EDITOR=vim or export EDITOR=vim
  - もしくは、git config --global core.editor vim
- git push のみはデフォルトでは、カレンとブランチのみを push するが、設定によっては追跡中のローカルブランチ全てをプッシュするのでとても危険
  - git push origin branchname を毎回使う
  - git config --global push.default upsteam
- git clone はローカルの.git ファイルのあるレポジトリのパスも clone できる
- mergetool を vim へ変更

  - git config --global merge.tool vimdiff
  - https://qiita.com/yuya_presto/items/5d99499cf96c0ebb09f8
  - conflict 状態でないのでいかが帰ってくる

- confilict 表示を 3way 方式にする
  - git config --global merge.conflictstyle diff3

```bash
<<<<<<<<<<<<<<<<<<
merge前の状態 = pushならremoteの状態
||||||||
分岐部分のjoutai = localとremoteで枝分かれする節点の部分
==================
mergeしたい差分 = pushならlocalの状態
>>>>>>>>>>>>>>>>>>
```

refspec = localbranch: remotebranch
remote = origin

運用

- ローカルで master と topic 間で git merge master と git merge topic を使い、コンフリクトする修正をしなければお互いに変更を更新し合える。

### エイリアス

- gitconfig

```bash
❯ cat ~/.gitconfig
[filter "lfs"]
	required = true
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
[user]
	name = takeshun256
	email = <>
[color]
	ui = true
[alias]
	co = checkout
	st = status
	br = branch
	cm = commit

        # 参考：https://qiita.com/peccul/items/90dd469e2f72babbc106
        # いい感じのグラフでログを表示
        gr = log --graph --date=short --decorate=short --pretty=format:'%Cgreen%h %Creset%cd %Cblue%cn %Cred%d %Creset%s'
        # Untracked filesを表示せず，not stagedと，stagedだけの状態を出力する
        stt = status -uno
        # ファイル名のみの差分を表示する
        difff = diff --name-only
        # staged diff
        diffs = diff --cached
[pager]
	branch = less -F -X
	diff = less -F -X
```
