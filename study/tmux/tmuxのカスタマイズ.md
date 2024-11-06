start：[[2023-10-08]] 00:46

### 現在の tmux.conf

```python
## Prefix key modification
set -g prefix C-a
unbind C-b
bind-key C-a send-prefix

## Keybinding modifications
unbind %
bind '\ ' split-window -h  # Using '\ ' to ensure the backslash is interpreted correctly
unbind '"'
bind - split-window -v
unbind r
bind r source-file ~/.tmux.conf \; display "Reloaded!"
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
bind -r m resize-pane -Z
bind -n S-left previous-window
bind -n S-right next-window

## General settings
set -g base-index 1
set-option -g mouse on
set -g default-terminal "screen-256color"
set -g status-justify left

## Status line appearance
set -g status-bg "colour235"
set -g status-fg "colour250"
set -g status-position bottom
set-option -g status-left "#[fg=colour255,bg=colour4]#[dim,bold]#{?client_prefix,#[bg=colour3],} s/#S "
set-option -g status-right "#[fg=colour250,bg=colour235] %Y/%m/%d%a %H:%M:%S"
setw -g window-status-format '#[fg=colour242] #I:#W '
setw -g window-status-current-format '\
#[bg=colour2,fg=colour255] #I:#W '
set-option -g status-interval 1

## Vim keybinding settings (uncomment if necessary)
# set-window-option -g mode-keys vi
# bind-key -T copy-mode-vi 'v' send -X begin-selection
# bind-key -T copy-mode-vi 'y' send -X copy-selection
# unbind -T copy-mode-vi MouseDragEnd1Pane

## Plugins for copy-paste
# コピペをできるようにする(pluginの反映はC-a + i, コピーはドラッグでOK)
# https://wonderwall.hatenablog.com/entry/2016/06/29/230105
set -g @plugin 'tmux-plugins/tmux-copycat'
set -g @plugin 'tmux-plugins/tmux-yank'

```

### カスタマイズ調査

- [[macでtmuxのセットアップ]]
- [ターミナルをかっこよくカスタマイズしたいためだけに tmux デビューしてみた - Qiita](https://qiita.com/FrogWoman/items/f6797f2a70c44e42863d)
  - このサイトで紹介されているチートシートとか参考になりそう
- [tmux の status line の設定方法 - Qiita](https://qiita.com/nojima/items/9bc576c922da3604a72b)

### カスタマイズメモ

#### 現在 bind されているキー設定の一覧が見れる(デフォルト設定も全て)

- [tmux と仲良くなる - とよぶ](https://takasing104.hateblo.jp/entry/2014/08/05/194923)

```python
tmux list-keys
tmux list-keys | grep vi
```

#### 現在の設定を見るコマンド

```python
# ex. default-commandについてみる
tmux show-options -g | grep default-command
# window paneのオプション
tmux show-window-options -g | grep [option-name]

```

`
status-left, status-right, window-status-format

```python
# #{?client_prefix,#[bg=colour3],} でprefixが押された時に色変える
set-option -g status-left "#[fg=colour255,bg=colour4]#{?client_prefix,#[bg=colour3],} [#S] #{prefix_highlight}"
set-option -g status-right "#[fg=colour250,bg=colour235] %Y/%m/%d%a %H:%M:%S"
setw -g window-status-format '#[fg=colour242] #I:#W '
setw -g window-status-current-format '\
#[bg=colour2,fg=colour255] #I:#W '
```

### session を作るようなカスタムコマンドを作成する

- tmux new -s ... とかが忘れがちなので、カスタム func を`~/.zshrc` に作成する

```sh
# ~/.zshrc

# tmuxの新しいセッションを作成し、指定した数のウィンドウを持つ関数
ptmux() {
    if (( $# != 2 )) || ! [[ $2 =~ ^[0-9]+$ ]]; then
        echo "Usage: create_tmux_session <session_name> <number_of_windows>"
        return 1
    fi

    local session_name=$1
    local num_windows=$2

    # 新しいtmuxセッションを開始
    tmux new-session -d -s $session_name

    # 指定した数のウィンドウを作成
    for ((i = 1; i < num_windows+1; i++)); do
        tmux new-window -t $session_name:$i
    done

    # セッションにアタッチ
    tmux attach -t $session_name
}
```

使い方

```python
vi ~/.zshrc
source ~/.zshrc

ptmux hello 3
```

### 初回 tmux から始める設定

- [tmux チートシート - Qiita](https://qiita.com/nmrmsys/items/03f97f5eabec18a3a18b)
- `~/.zprofile`に以下を記載
- [[2023-10-08]] 現在はコメントアウトしている

```python
#  tmuxを初回セルのみで実行(=tmuxから始める)
if [ $SHLVL = 1 ]; then
  tmux
fi
```

【メモ】

- set コマンドはオプションの変更や設定で利用する

  - -g でグローバルオプション
    - 例：`set -g status-bg blue`
  - =set-option コマンド
  - bind はキーバインドの設定で利用する
    - 例：`bind R source-file ~/.tmux.conf
      - prefix(Ctrl-a)の後に、`R`を打つと、設定ファイルが読み込まれる設定
  - `setw` コマンドは、特定のウィンドウのオプションを設定または変更する
    - -g をつけないと現在のウィンドウにのみ適用されるらしい？

- `C-a <space>`すると pane の配置が自動で変更される
  - 3 つくらい適当に切った後に適当に変更したい時に使用する

## 参考

チートシート便利 -[tmux チートシート - Qiita](https://qiita.com/nmrmsys/items/03f97f5eabec18a3a18b)

status bar

- [tmux の status line の設定方法 - Qiita](https://qiita.com/nojima/items/9bc576c922da3604a72b)
