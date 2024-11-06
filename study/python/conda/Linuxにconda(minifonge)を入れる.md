start：[[2023-06-20]] 15:50

- [GitHub - conda-forge/miniforge: A conda-forge distribution.](https://github.com/conda-forge/miniforge)
- [pyenv/pyenv-virtualenv/MiniForge を使った Linux の Python 環境構築](https://zenn.dev/karaage0703/articles/5af7ce4b8b1a8a)
- [M1 Mac で機械学習や Python は Miniforge を使う - Qiita](https://qiita.com/kujirahand/items/9bf1a1e7bd34bdb87da5)

miniforge は、Conda の計量パッケージらしい

- minocnda よりは、より Python の科学計算ツールの使用やパフォーマンスに焦点を当てている
- conda-forge のみが勇逸のチャンネル
- mamba-forge は、より高速な依存関係解決をするらしい

### install

- [GitHub - conda-forge/miniforge: A conda-forge distribution.](https://github.com/conda-forge/miniforge#install)

```python
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
# conda initをyesする

source ~/.bashrc
conda config --set auto_activate_base false
# conda config --show
conda info -e # 仮想環境を表示
conda deactivate # baseから抜ける
exec $SHELL # shellを再起動
which python # condaの環境に入っていないことを確認
```

### 仮想環境を作成

```python
conda create -n NNN python=3.10
conda activate NNN
```
