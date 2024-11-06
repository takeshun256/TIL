start：[[2023-07-31]] 12:37

### 参考となる記事

- [dotfiles を管理しよう - Qiita](https://qiita.com/massy22/items/5bdb97f8d6e93517f916)
- [GitHub で dotfiles を管理して、どこでも簡単に環境を統一しよう！【アドカレ 2020 最終日】 | デジクリ](https://core.digicre.net/blog/article/74)
- [dotfiles · GitHub Topics · GitHub](https://github.com/topics/dotfiles)
  - github の topics の dotifiles
- [VSCode Remote Containers を使うなら dotfiles repository で幸せになろう - Qiita](https://qiita.com/frozenbonito/items/aa320c4b3f84b9816daa)
  - devcontainer で、dotfiles を使う
- [ようこそ dotfiles の世界へ - Qiita](https://qiita.com/yutkat/items/c6c7584d9795799ee164)

### 導入する

- 簡単な dotfiles の仕組み

  - HOME ディレクトリ下に、dotfiles ディレクトリを clone して、そこの中の install.sh を事項することで、HOME ディレクトリ下にシンタックスリンクが作成される
    - 本体は、dotfiles ディレクトリ下に管理される
  - ssh や aws などの認証情報は絶対に入れてはいけない
    - .gitignore に登録している

- 導入結果

  - [GitHub - takeshun256/dotfiles: dotfiles](https://github.com/takeshun256/dotfiles)

- 導入した方法
  - 一番単純なものを試した
  - 安全そうな tmux.conf のみ upload してみた

1. github 上で新規レポジトリを作成(Public)
   1. [GitHub - takeshun256/dotfiles: dotfiles](https://github.com/takeshun256/dotfiles)
2. 作成

```sh
cd ~
mkdir dotfiles
echo "# dotfiles" >> README.md
vi install.sh
chmod +x install.sh
mv ~/.tmux.conf ~/dotfiles # dotfiles内へ本体を移動
./install.sh # HOME下へリンクを作成

vi .gitignore
vi README.md

git init
git add .
git cm -m "initial commit"
git remote add origin git@github.com:takeshun256/dotfiles.git
git push -u origin main
```

## まとめ(類似点・相違点)

シンタックスリンクで一括で作成しておいて、導入を簡単にする
dotfiles レポジトリで、本体をバージョン管理する

dotifles を育てていこう

- [VSCode Remote Containers を使うなら dotfiles repository で幸せになろう - Qiita](https://qiita.com/frozenbonito/items/aa320c4b3f84b9816daa)
  [Site Unreachable](https://blog.fascode.net/2023/03/10/dotfiles-manager-lico/)
