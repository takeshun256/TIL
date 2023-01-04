# GithubActionsを使って定期commitする方法

以下のサイトの方法で作成しました。
https://zenn.dev/bun913/articles/study-history-on-github

参考：
https://docs.github.com/ja/actions/using-workflows/workflow-syntax-for-github-actions#onschedule

## 手順
1. 定期commitするレポジトリを作成する(例：tilというprivateレポジトリを作成)
2. レポジトリのActionsからworkspaceを作成する(たしか、~by oneselfみたいなボタンだった気がする)
	1. そしたら、.github/workflows/main.ymlが立ち上がる
3. main.ymlのコードを以下のコードで書き換える(上記の参考サイトのコード)
```
name: CommitMyTIL
on:
  # 手動でもWorkflowを利用できるようにしておく
  workflow_dispatch:
  schedule:
    # JSTで8:45に毎日１回実行
    - cron: '45 23 * * *'
jobs:
  output_study_history:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
    - name: Run index.py
      run: |
        python index.py
    - name: Commit and Push diff
      env:
          # コマンドを実行するための環境変数をセット
          GIT_USER: ${{ secrets.GIT_USER }}
          GIT_MAIL: ${{ secrets.GIT_MAIL }}
      run: |
        # git remote set-url origin https://github.com/${GIT_USER}/til
        git config --global user.name "${GIT_USER}"
        git config --global user.email "${GIT_MAIL}"
        if (git diff --shortstat | grep '[0-9]'); then \
          git add .; \
          git commit -m 'Updated TIL repository regularly!!'; \
          git push origin HEAD; \
        fi
```
4. あとは、右上のstart commitみたいなボタンを押すと完了
5. レポジトリにアクセスするために、secretsを作成
	1. レポジトリのsettings/secrets/actionsに登録
	確認方法は、[git configの使い方](https://note.nkmk.me/git-config-setting/)
		1. NAME=GIT_USER
		2. value=(git configで入手した個人情報)



## コードの意味
1. レポジトリに差分がある場合、毎日8:45に自動commitされる
2. index.pyが実行され、index.txtにファイル構造が印字される


## コードの注意点
1. ~: todoみたいな形だが`:`と`todo`の間に空白が必要
2. push時に追加したい場合は、`push:`を追加
3. GIthub Actionsのdocを読み解くのが理想
4. 毎回自動でpushされるので、pull必要があるかも
5. 毎回の自動実行前に、git pull処理を入れる必要があるかも
