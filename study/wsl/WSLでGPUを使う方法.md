start：[[2023-03-12]] 10:35

## 経緯・背景

windows で gpu をつかう docker を使うには、wsl で GPU を使えるようにする必要がある。

## 参考

- https://docs.nvidia.com/cuda/wsl-user-guide/index.html
- https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local

## 内容

### 現状確認

- wsl で`nvidia-smi`が反応しない

### 公式ドキュメントを確認/WSL 上で実行

- old gpg key(公開鍵)を削除

  - `sudo apt-key del 7fa2af80`

- wsl 用の gpu driver をインストール
  - https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda-repo-wsl-ubuntu-12-1-local_12.1.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-12-1-local_12.1.0-1_amd64.deb
sudo cp /var/cuda-repo-wsl-ubuntu-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```

なんか wsl 用のドライバーを使わないと、変に上書きされるらしい

### うまくいっているか確認

cuda toolkit が正しくインストールされているか確認

- `nvidia-smi`
  - cuda device の確認
- `nvcc --verson`
  - toolkit のバージョン確認
- ~~cuda サンプルの実行~~
  - samples フォルダなかった
  - 念のための実行なので、まあ上の 2 つで良いかも

```
$ cd /usr/local/cuda/samples
$ sudo make
$ ./bin/<サンプルプログラム名>
```

結果

1. インストールしたバージョン(12.1)とツールキットのバージョンがあっていない

- 以下でパスを変えます。

### パスを確認・変更

- 設定されているバージョンがインストールしたものと違うので、インストールしたもの(12.1)に変えてみる

```python
vi ~/.bash_profile
source ~/.bash_profile
```

- 再度確認
  - 更新されてるやった！！

## 振り返り

- 公式ドキュメントを確認して、実行する
  - 一番安全かつ、正しい内容
- chatgpt に公式ドキュメントで分からないことがあったら質問するのが良かった。

## 次回やること

- 複数の cuda version がインストールされているので、使用しているツールキット以外は削除してよいかも
