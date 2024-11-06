start：[[2024-07-09]] 14:15

1. ssh 接続
   1. `ssh vps-server`
   2. [[桜VPS初見]]でセットアップ済み
2. ポートの確認
   1. `cat /etc/ssh/sshd_config`から、`#Port 22` だったので、22
3. Uncomplicated Firewall をインストール
   1. `sudo apt update && sudo apt install ufw`
4. ssh 接続を許可
   1. `sudo ufw allow ssh`
5. 必要なポートを適宜許可
   - ウェブサーバー運用の場合
     - `sudo ufw allow http && sudo ufw allow https`
6. FireWall の有効化
   1. `sudo ufw enable`
7. 状態の確認 1. `sudo ufw status
8. 接続できるか確認
   1. `Ctrl+D` => `ssh vps-server`

メモ: 詳細な設定の場合は、iptable というものを利用するらしい
