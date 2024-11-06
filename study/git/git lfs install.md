start：[[2023-07-16]] 07:04

### install

windowsでインストールする場合と、wslでインストールする場合は、両方別々でインストールが必要

- windows
	- [Git Large File Storage | Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.](https://git-lfs.com/)でダウンロードして起動してfinish
	- `git lfs install`をターミナルで実行
- wsl
	- [Installation · git-lfs/git-lfs Wiki · GitHub](https://github.com/git-lfs/git-lfs/wiki/Installation)

- mac
	- `arch -arm64 brew install git-lfs`
	- [[GitHub] Git LFSで巨大なファイルを扱う](https://blog.katsubemakito.net/git/github-gitlfs)
```bash
 1077  curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
 1078  sudo apt-get install git-lfs
 1079  ls
 1080  git lfs install
 1081  git lfs version
```

### usage

- 大きな画像ファイルとかを扱う際に、使用する

- 使い方参考
	- [Git LFS をちょっと詳しく - Qiita](https://qiita.com/ikmski/items/5cc8b8832336b8d85429)

- lfsを使用したいレポジトリ内で、`git lfs install`をすれば良い
- github proだと、1レポジトリ2GBなので簡単に使い切る可能性
