start：[[2023-07-29]] 16:17

### gitとの違い

- github cliは、gitよりもgithubとの連携が強いコマンドのこと。
	- issueやpull requestをより直感的に操作できる。

強み
- インターフェースとの連携：githubの操作が簡単に
- コマンドが簡単

問題
- gitよりもgithubに特化しているので操作としては、特化している。
- gitとは別にインストールする必要がある。
- 複雑な操作はできなそう


### インストール

- [Installation instructions | GitHub CLI](https://cli.github.com/manual/installation)

```bash
brew install gh
gh --version
	# gh version 2.32.1 (2023-07-24)
	# https://github.com/cli/cli/releases/tag/v2.32.1
```

- CLIの認証
	- [MacでGitHub CLIをセットアップする](https://zenn.dev/krabben16/articles/setup-github-cli-for-mac)
 -> gihtubに sshで認証した。
```bash
gh auth login
```

### カスタマイズ

- vimに設定
```bash
gh config set editor vim
```

- config一覧
![[Pasted image 20230729164405.png]]

- カレントレポジトリをブラウザで開くエイリアス
```bash
gh alias set rvw "repo view --web"

cd /path/to/repo
gh rvw
```

- その他設定
	- [GitHub CLIのすヽめ&オレオレ関数で効率化していく](https://zenn.dev/torahack/articles/d6b760fd11bf3a#github-cli%E3%81%A7%E3%82%AA%E3%83%AC%E3%82%AA%E3%83%AC%E9%96%A2%E6%95%B0%E3%82%92%E4%BD%9C%E3%82%8B)


### 動作確認
- 自身のレポジトリから条件に合うものを取り出す。
	- pythonが使用されているもの
	- json形式で色々出力
```bash
gh repo list --language python --json name,primaryLanguage,languages,owner,createdAt,updatedAt
gh repo list --language python --json name
```

private repoの情報も取得できている


### 操作

- [MacでGitHub CLIをセットアップする](https://zenn.dev/krabben16/articles/setup-github-cli-for-mac)
- [GitHub CLIのすヽめ&オレオレ関数で効率化していく](https://zenn.dev/torahack/articles/d6b760fd11bf3a)

-> 色々、レポジトリや github actionsの操作が可能
-> 検索も可能


その他の便利なコマンド
- [GitHub CLIのすヽめ&オレオレ関数で効率化していく](https://zenn.dev/torahack/articles/d6b760fd11bf3a#github-cli%E3%81%A7%E3%82%AA%E3%83%AC%E3%82%AA%E3%83%AC%E9%96%A2%E6%95%B0%E3%82%92%E4%BD%9C%E3%82%8B)

- これすご
[GitHub CLIのすヽめ&オレオレ関数で効率化していく](https://zenn.dev/torahack/articles/d6b760fd11bf3a#git-init%E3%81%8B%E3%82%89%E3%81%AEfirst-commit%E3%81%8B%E3%82%89%E3%81%AE%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E4%BD%9C%E6%88%90%E3%81%8B%E3%82%89%E3%81%AE%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E3%83%96%E3%83%A9%E3%83%B3%E3%83%81%E3%81%AE%E5%88%87%E3%82%8A%E6%9B%BF%E3%81%88%E3%81%BE%E3%81%A7%E4%B8%80%E6%B0%97%E3%81%AB%E7%B5%82%E3%81%88%E3%82%8B%E9%96%A2%E6%95%B0)
```
mkdir gh_test
cd gh_test
gcre
```
-> このエラーで無理そう
- [【git】error: failed to push some refs to "URL"のエラー対処法 - Qiita](https://qiita.com/cccccccccc/items/118a5b3237c78d720582)
