start：[[2023-04-03]] 17:55

### インストールと Config

```bash
brew install tmux
tmux -V
touch ~/.tmux.conf
vim ~/.tmux.conf
tmux source-file ~/.tmux.conf
```

- ~/.tmux.conf の中身
  - 別途、[日本語動画上の設定](https://youtu.be/wLuz3HQogW4?t=449)も拝借
  - r はリビーとモードで、長押しで継続できる

```bash
set -g default-terminal "screen-256color"

# change default tmux prefix to C-a
set -g prefix C-a
unbind C-b
bind-key C-a send-prefix

# change keybinds for splitting windows
unbind %
bind | split-window -h

unbind '"'
bind - split-window -v

# add keybind for easily refreshing tmux configuration
unbind r
bind r source-file ~/.tmux.conf

# add keybind for easily resizeing tmux panes
bind -r j resize-pane -D 5
bind -r k resize-pane -U 5
bind -r l resize-pane -R 5
bind -r h resize-pane -L 5

# add keybind for maximizing and minimizing tmux pane
bind -r m resize-pane -Z

# enable the mouse in tmux
set -g mouse on

# configure vim movements for tmux's copy mode
set-window-option -g mode-keys vi

bind-key -T copy-mode-vi 'v' send -X begin-selection # start selecting text with "v"
bind-key -T copy-mode-vi 'y' send -X copy-selection # copy text with "y"

unbind -T copy-mode-vi MouseDragEnd1Pane # don't exit copy mode after dragging with mouse
```

- Install tpm (tmux plugin manager)

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

- tmux.conf に追記

```python
# add and configure tmux plugins with tpm
# tpm plugin
set -g @plugin 'tmux-plugins/tpm'

# list of tmux plugins
set -g @plugin 'christoomey/vim-tmux-navigator' # for navigating panes and vim/nvim with Ctrl-hjkl
set -g @plugin 'jimeh/tmux-themepack' # to configure tmux theme
set -g @plugin 'tmux-plugins/tmux-resurrect' # persist tmux sessions after computer restart
set -g @plugin 'tmux-plugins/tmux-continuum' # automatically saves sessions for you every 15 minutes

set -g @themepack 'powerline/default/cyan' # use this theme for tmux

set -g @resurrect-capture-pane-contents 'on' # allow tmux-ressurect to capture pane contents
set -g @continuum-restore 'on' # enable tmux-continuum functionality

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
```

- 変更の反映と逐次確認

  - vscode で補完を活かして、conf ファイルを編集
  - iterm2 の tmux 上で、C-a + r で conf を反映

- 色設定を見る

```bash
for i in {0..255}; do printf "\x1b[38;5;${i}mcolour${i}\x1b[0m\n" done
```

### tmux の基礎知識

- セッション
  - ターミナルのウィンドウの集合
- ウィンドウ
  - ペインの集合
- ペイン
  - ここのターミナル画面
- アタッチ
  - セッションに接続する
  - tmux a -t セッション名
- デタッチ
  - セッションを破壊することなく、セッションから抜ける
  - C-a + d or C-a + : detach-client

ex. このセッションは 4 つの画面(ウィンドウ)がある。それぞれのウィンドウには 3 つのペインがある。

### tmux のコマンド

削除したいウィンドウまたはペインへ移動した後に削除する

- C-a + :kill-window: ウィンドウを削除
- C-a + :kill-pane: ペインを削除
  - `C-a x` でカレント Pane を削除

セッション操作(選択後 enter で入る)

- C-a + s: セッション一覧表示
- C-a + $: セッションの名称変更
- ct

```python
tmux a # 前回のセッションを再開, a=attach
tmux attach -t <session> # 特定のセッションにアタッチする
tmux # 適当にtmuxセッションを開始
```

tmux をターミナル起動時に自動実行

```bash_prfile, zprofile
# 初回シェル時のみ tmux実行
if [ $SHLVL = 1 ]; then
  tmux
fi
```

### 基本的な流れメモ

```bash
tmux ls # セッション一覧を表示
tmux a -t 0 # セッション0にアタッチ
----tmux
C-a + c # 新規windowを作成する
C-a + n # window間を切り替える
C-a + - # ウィンドウを複数のパネルに分割する
C-a + o # 分割されたパネル感を切り替える
C-a + d # デタッチ
----
tmux kill-session -t 0 # セッション0を削除
```

### エラー対処

【メモ】

- iterm2 で tmux のキーバインドが使えない
  - キーバインドが競合している
  - 解決-> `tmux` で tmux 環境に入りそこで、コマンドを使用できるので、その環境内だとキーバインドが有効になる。
- tmux の prefix key がなぜか、C-t になっている。

  - .tmux.conf では C-a に設定しているのに...
  - 解決: tmux の source-file に設定する必要があった、
  - `tmux source-file ~/.tmux.conf` を実行

- item2 期同時に以下のエラーメッセージ - sessions should be nested with care, unset $TMUX to force - 以下の設定を off - これは、期同時に、カスタム設定を読み込むかどうかを指定するオプション
  ![[Pasted image 20230404012501.png]]

- item2 の設定で以下の警告

  - System window restoration has been disabled, which prevents iTerm2 from respecting this setting. Disable System Preferences > General > Close windows when quitting an app to enable window restoration.
  - [iTerm2 で「Use System Window Restoration Setting」を設定しているとアラートが表示されて機能しない – Webrandum](https://webrandum.net/iterm2-window-restoration-policy-alert/)
  - 以下の画像のようにデスクトップと Dock でアプリケーションを終了するときにウィンドウを閉じるのチェックを外す

- tmux 上でマウスでコピーする場合に、権限がない場合は、access clipboard にチェックをつける

---

vscode 内で、tmux のコピーをする方法

- [macos - How to copy with the mouse from tmux in VS Code to the OSX clipboard - Super User](https://superuser.com/questions/1688563/how-to-copy-with-the-mouse-from-tmux-in-vs-code-to-the-osx-clipboard)
  item2 だと,選択して y を押すだけでコピーできるが、vscode では上記の設定を On にして、
  alt を押しながら、文字をマウスで選択する。そして、cmmand+C でコピーできる

## 参考

- video about setup
  - [How I Use Tmux With Neovim For An Awesome Dev Workflow On My Mac - YouTube](https://www.youtube.com/watch?v=U-omALWIBos)
- セットアップのコマンドの流れ
  - [How To Use and Configure Tmux Alongside Neovim](https://www.josean.com/posts/tmux-setup)
- 日本語のセットアップと基本的な使い方の流れ
  - [Tmux 超入門 Tmux の導入から使い方まで解説 iTerm2 + Vim/NeoVim + Tmux で VSCode 超え - YouTube](https://youtu.be/wLuz3HQogW4)
  - [Tmux 超入門 Tmux の導入から使い方まで解説 iTerm2 + Vim/NeoVim + Tmux で VSCode 超え | フルスタック Linux プログラミング](https://reisuta.com/tmux/)
- tmux チートシート
  - [tmux チートシート - Qiita](https://qiita.com/nmrmsys/items/03f97f5eabec18a3a18b)
- tmux conf の参考
  - [.tmux.conf の設定 - Qiita](https://qiita.com/youichiro/items/dd54c38c2f3873348c78)
- 参考
  - [エンジニアなら tmux くらい使いこなしたらどうだ | sititou70](https://sititou70.github.io/%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%81%AA%E3%82%89tmux%E3%81%8F%E3%82%89%E3%81%84%E4%BD%BF%E3%81%84%E3%81%93%E3%81%AA%E3%81%97%E3%81%9F%E3%82%89%E3%81%A9%E3%81%86%E3%81%A0/)
-

## まとめ(類似点・相違点)

- `~/.tmux.conf` に設定を書く。
- tmux で tmux に attach する。
- prefix key + key で tmux 内では操作を行う。
- tmux は、dettach することで抜けることができ、ssh 接続をしているときに、クライアントが落ちても接続が維持されるというメリットがある。
  - ssh 接続するときによく使用される。
  - 全てのセッションを削除: tmux kill-server
  - tmux がターミナルを終了せず抜ける(dettach): C-a + d

tmux のイメージ

- セッションが 1 つのバッグで、その中にキャンバスボード(ウィンドウ)が複数ある。
- それぞれのキャンバスボードにパネルを並べていく

tmux のメリット

- 複数のターミナルを管理し、複数のタスクを同時並行で実行できる。
  - 1 つのタスクは、1 セッション
  - 作業効率が上がる
- tmux で、ssh 接続する
  - セッションの状態を保存して復元できる(デタッチした場合)ので、再起動やエラーに強い

ターミナルを閉じずに保存することができる

- ずっと保存しておくとかできる=それぞれわかりやすい名称をつけるとか

## 振り返り

エラー対処の時に、ある程度、なぜエラーが出ているのかを推測することが解決につながっている気がする。

- conf ファイルの設定を読み込んでくれていない... -> source コマンドのようなものが実行されていないか、tmux の source-file に設定されていないのかもと推測する。
  - わからなかったら、インターネットで調べて、それを試して、メモる。
