# セットアップ

1. `Projects Boards` をプライベート設定で作成
   1. Your Projectsから作成して、`Link a project` で紐づける。


2. トークンを取得
   1. `https://github.com/settings/tokens` から、tokenを作成する。
      1. この時、チェック欄で、`repo` と `projects` を忘れずにチェック
      2. これは、別のレポジトリでも使えるので、どこかに記録しておく


3. ワークフローを追加
   1. https://github.com/takeshun256/TIL/pull/1/files
   2. .github/workflows/add_to_project_board.yml
      1. `Issue` や `PR` を作成すると、自動で `Project` へ追加する。
   3. .github/workflows/update_my_til.yml
      1. `repository` 内のディレクトリの情報(=`tree`)を `index.txt` に更新する。


4. `Secrets/Actions` に以下を作成
   1. `GIT_MAIL` : githubに登録したメールアドレス
   2. `GIT_USER` : githubのユーザー名(ex. `takeshun256`)
   3. `GIT_TOKEN` : `2. トークンを取得` で作成したトークン


5. IssueとPRのテンプレートを作成
   1. `.github/` 下に`ISSUE_TEMPLATE` と `PULL_REQUEST_TEMPLATE` を作成する。
      1. そうすることで、issueやpullrequest作成時に、テンプレートが書いてある状態から書き始められる。



# 運用方法

1. Issueに、Tasksや追加した機能を書く。
2. ⇒ Projectsに、自動で登録される。
3. Projectsにある、カンバン(Issue) に対して、ブランチを切って変更を加える。
4. Pushして、PRを`main ← branch` へ出して、マージする。


# どうしてこういう形式にしたのか

まず、1つの `Projects` で複数のレポジトリ・TILの運用を行いたかった。なので、ISSUEやPRを全て、1つの `Projects` へ自動で集約するようにした。

ブランチを切って作業する必要性は1人プロジェクトのため、特にないが、IssueやPRを出すことで、Projects 上でしたことを見えるように下かったため。


