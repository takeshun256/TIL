start：[[2023-06-16]] 03:20

### 概要理解

鍵を使用しない流れ

1. Mac には、SSH クライアントがデフォルトでインストールされているため、特別な準備は必要ありません。
2. Linux PC の IP アドレスまたはホスト名を確認します。Linux PC には、SSH サーバーがインストールされ、実行中である必要があります。
3. ターミナルアプリケーションを開きます。Mac の「Launchpad」から「その他」フォルダ内の「ターミナル」を選択します。
4. ターミナルで以下のコマンドを入力します（<IP_ADDRESS>は Linux PC の IP アドレスまたはホスト名に置き換えてください）：
   1. ssh username@<IP_ADDRESS>

Mac で鍵を生成するやり方の流れ

1. Mac で ssh keygen
2. 公開鍵を LinuxPC へ連絡
3. LinuxPC で ssh/authorized-keys に登録
4. Mac の ssh/config に接続内容を書く

### LinuxPC でセットアップ

- ssh サーバーを起動

```python
sudo apt update
sudo apt install openssh-server

# sshサーバーサービスを起動
sudo systemctl start ssh

# sshサーバーが起動していることを確認
sudo systemctl status ssh
```

- 接続時には、Linux PC の IP アドレスやホスト名、SSH ポート番号（デフォルトは 22）が必要

```python
# IPアドレスを取得(inet部分を確認)
ip addr show

# hostnameを取得
hostname
```

- `ping`コマンドで接続を確認(ping コマンドは応答速度を測るのにも使用される)
  - -c 回数 (デフォルトだと送信し続けるため)
  - -i 秒数(default 1s)
  - -s サイズ(default 56b)

```python
ping IPアドレス
```

### Mac で鍵生成

```python
cd ~/.ssh
ssh-keygen -t rsa -f keyname -C ""

cat keyname.pub | pbcopy
```

linux_pc の方で配置

```python
cd ~/.ssh
vi authorized_keys
# pubkeysの中身をコピペ(複数なら1行ずつ)
chmod 600 authorized_keys
```

### Windows(WSL)でも同様にお粉う

#### Vscode 上で接続する

- [Visual Studio Code で Remote SSH する。 - Qiita](https://qiita.com/nlog2n2/items/1d1358f6913249f3e186)
  Windows で、wsl に接続した状態で、リモートエクスプローラーを開く

- 上記のやり方でやろうとしたところ、wsl 上の ssh/config を認識しなかったので、remote exploper で、ssh コマンドを入力して登録した。

### 再開する時

- 自宅で Linux-PC を動かしつつ、mac で接続したい場合とか

```python
# linux
sudo systemctl start ssh
sudo systemctl status ssh # activeであることを確認

ip a # IPアドレスを確認

```
