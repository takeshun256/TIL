start：[[2023-10-09]] 07:41

### Oh-my-bash 入れる

#### 導入

- [GitHub - ohmybash/oh-my-bash: A delightful community-driven framework for managing your bash configuration, and an auto-update tool so that makes it easy to keep up with the latest updates from the community.](https://github.com/ohmybash/oh-my-bash/)

```python
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
```

インストール直後のターミナルの状態

- [Oh My Bash 導入メモ - Qiita](https://qiita.com/tomoten/items/9fab3dbac1295a82caa4#32-%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E5%BE%8C%E3%81%AE%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E3%81%AE%E8%A6%8B%E3%81%9F%E7%9B%AE)

#### **カスタマイズ**

<u>theme</u>

- [GitHub - ohmybash/oh-my-bash: A delightful community-driven framework for managing your bash configuration, and an auto-update tool so that makes it easy to keep up with the latest updates from the community.](https://github.com/ohmybash/oh-my-bash/#themes)
- [Themes · ohmybash/oh-my-bash Wiki · GitHub](https://github.com/ohmybash/oh-my-bash/wiki/Themes)
  - 画像で見れる

```python
vi ~/.bashrc
######## 上記の画像から入れたいthemeへ変更
# OSH_THEME="font"
OSH_THEME="powerline"
# OSH_THEME="powerline-light"
# OSH_THEME="agnoster"
########

source ~/.bashrc
```

色々あったけど、Git の差分が数字で表示される+色で `powerline` を選択した。

<u>その他の設定</u>

- 参考：[GitHub - ohmybash/oh-my-bash: A delightful community-driven framework for managing your bash configuration, and an auto-update tool so that makes it easy to keep up with the latest updates from the community.](https://github.com/ohmybash/oh-my-bash/#configuration)
- sudo の禁止
- python venv の表示
  - 下記の conda の初期化設定を移行する必要がある
- completions
  - `ls ~/.oh-my-bash/completions/`
  - conda は、`conda install argcomplete`する必要あり
    - `Please install argcomplete to use conda completion`
    - 常に conda に入る必要があるので削除する
- plugins
  - `ls ~/.oh-my-bash/plugins/`

【メモ】

設定ファイル

```python
.bashrc # シェル実行ごとに読み込まれる
.bash_profile # ログイン時のみ読み込まれる設定
```

## 参考

[GitHub - ohmybash/oh-my-bash: A delightful community-driven framework for managing your bash configuration, and an auto-update tool so that makes it easy to keep up with the latest updates from the community.](https://github.com/ohmybash/oh-my-bash/)
