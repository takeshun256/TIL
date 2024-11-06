start：[2023-01-28](2023-01-28.md) 01:09

## 参考様

- [ ] https://qiita.com/naz_/items/84634fbd134fbcd25296
- [ ] https://hogelog.com/python/conda-command.html
- [ ] https://biotech-lab.org/articles/818
- [ ] https://miyashinblog.com/anaconda-cmd/
- [ ] https://tarovlog.com/2021/01/04/anaconda-cheat-sheet/

## 内容

流れ

```zsh
conda info -e
conda create -n <prjname> python=[version]
conda activate
conda install [package]
```

他に使うもの

- インストール
  - conda install [package]
  - `conda install [package]==[version]
  - conda install [package] -n [prjname]
  - conda-forge とかのチャンネルを使ってインストールしたい場合
    - conda install [package] --channel conda-forge
    - 普段から conda-forge チャンネルからも探すようにする
      - conda config --add channels conda-forge
      - conda config --remove channels conda-forge
      - conda config --show-sources
- アクティベート
  - conda activate [prjname]
- 仮想環境削除
  - conda remove -n [prjname] --all
- クローン
  - conda create --clone [prjname2] --name [prjname]
- 環境のエクスポート
  - conda env export --name [prjname] > test_env.yaml # 環境を指定して export
  - conda env export > test_env.yaml
- yaml を元に環境構築
  - conda env create --file test_env.yaml
- インストール済みのパッケージリストをエクスポート
  - conda list --export > package_list.txt
  - conda list --name [prjname] --export > package_list.txt
  - export を explicit に変えると、パッケージ名だけでなくダウンロード元も出力される
- パッケージリストを元に環境構築
  - conda create --name [prjname] --file package_list.yaml
- インストール済みパッケージ
  - conda list
  - conda list -n [prjname]
- アップデート
  - conda update [library]
  - conda update --all
- conda 自体をアップデート
  - conda update -n base conda
- キャッシュの削除
  - conda clean --all

requirements.txt を入出力とする。

```python
conda create -n test_env python=3.10.0
conda activate -n test_env
conda install numpy
conda list -n test_env --export > requirements.txt

conda create -n test_env2 -f requirements.txt
```

## 類似点・相違点・まとめ

仮想環境の構築部分と export/import が特殊である。

パッケージリストを出力できることから、requirements.txt と親和性はありそう
