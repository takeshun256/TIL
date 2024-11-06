start：[[2023-01-28]] 01:00

## 経緯・背景

mac のローカルで Python 環境を構築する必要があり、pipenv や poetry や conda などが候補にあった。
現在入っている研究で、miniforge というものを知り、それが便利だり使用しようと思った。
conda/ miniforge / manbaforge の違いとしては以下のような理解である。

1. miniforge: デフォルトが conda-forge を使用している conda
2. manbaforge: c++で作成された miniforge であり、高速

## 参考

https://github.com/conda-forge/miniforge#unix-like-platforms

https://ja.stackoverflow.com/questions/61630/anaconda%E3%81%A7base%E3%81%8C%E8%87%AA%E5%8B%95%E7%9A%84%E3%81%ABactivate%E3%81%95%E3%82%8C%E3%82%8B%E3%81%AE%E3%82%92%E9%98%B2%E3%81%8E%E3%81%9F%E3%81%84

## 内容

流れ

1. 以下のコードで manbaforge をインストールを入れる。
   1. mac なので、https://github.com/conda-forge/miniforge#unix-like-platformsを参考にインストール
   2. ところどころ、yes と打つ場所があるので、enter/yes を適宜入力する。
   3. 最後に、conda init するかと聞かれるので yes を選択した。

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
```

2. デフォルトで、ターミナルを立ち上げると、`conda activate base`が走るので、それをオフにする。
   1. `conda config --set auto_activate_base false`
   2. vscode でもオフにするには、設定の Python Actvate Environment をオフにする。

## 類似点・相違点・まとめ

簡単な導入である、mac 便利

vscode 上の設定で pyhon 環境の設定項目があるので、それに注意

`uname -m` や`uname` はデバイスの名称などが入る。

`~/manbaforge`があったら、削除して、bash manbaforge~ をする。
