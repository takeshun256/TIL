以下を参考

- [Miniconda in WSL - DEV Community](https://dev.to/sfpear/miniconda-in-wsl-3642)
- [Install Miniconda and Anaconda on WSL 2 or Linux](https://kontext.tech/article/1064/install-miniconda-and-anaconda-on-wsl-2-or-linux)
- [Anaconda の有償化に伴い miniconda+conda-forge での運用を考えてみた - Qiita](https://qiita.com/kimisyo/items/986802ea52974b92df27)

コマンド

```python
  397  sudo apt-get update
  398  sudo apt-get install wget
  399  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  400  ls
  401  sha256sum Miniconda3-latest-Linux-x86_64.sh
  402  sh ./Miniconda3-latest-Linux-x86_64.sh
  exec $_SHELL_ -l # condaを認識させるため
  conda config --remove channels defaults # defaultのcondaを入れない(古いものが勝手にインストールされるため)
  conda config --show channels

```
