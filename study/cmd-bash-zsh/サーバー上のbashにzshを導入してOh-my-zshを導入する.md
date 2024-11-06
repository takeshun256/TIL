start：[[2023-10-09]] 07:04

### 導入手順(Linux/sudo 使えない状態)

sudo が使える場合は、`sudo apt install zsh` で導入できるので割愛。

#### 1. zsh を導入

ここで、`sudo apt isntall zsh` が出てくるので ❌

- ユーザー下にインストールするために、ソースからビルドする
- 参考
  - [Building Zsh from Source and Configuring It on CentOS - jdhao's digital space](https://jdhao.github.io/2018/10/13/centos_zsh_install_use/)に従ってやれば良い

メモ

```python
echo $SHELL # 現在のSHELL確認, /bin/bash
cat /etc/shells # 使えるshellを確認, zshはないけどtmuxあるな
```

### 参考

- [GitHub - romkatv/powerlevel10k: A Zsh theme](https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#installation)
- [Building Zsh from Source and Configuring It on CentOS - jdhao's digital space](https://jdhao.github.io/2018/10/13/centos_zsh_install_use/)

【メモ】
