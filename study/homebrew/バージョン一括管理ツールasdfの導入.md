start：[[2023-12-15]] 19:00

### 導入

- [バージョン管理ツール asdf でディレクトリごとに Python のバージョンを指定する | DevelopersIO](https://dev.classmethod.jp/articles/try-asdf-settings/)
- [Getting Started | asdf](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf)
- [GitHub - asdf-vm/asdf: Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more](https://github.com/asdf-vm/asdf)

```python
brew install asdf
```

環境変数追加

```python
echo -e "\n. $(brew --prefix asdf)/asdf.sh" >> ${ZDOTDIR:-~}/.zshrc
```

### Usage

- インストール可能なプラグイン一覧(だば − ーー)

```python
asdf plugin list all
```

- 試しに python 入れる(一瞬)

```python
asdf plugin add python
```

- インストール済み確認

```python
asdf plugin list
```

- python のインストール可能なバージョンを表示
  - まさに pyenv
  - manbaforge とかもあるんけ！

```python
asdf list all python
```

- バージョンを指定して入れる

```python
asdf install python 3.12.0
```

> ない場合もあるらしい、。その場合は 3.12 という結構新しいやつではなく普通のやつをインストールしてみる

- 有効化
  - pyenv のように範囲位指定かのう

```python
# グローバル有効化
asdf global python 3.9.1

mkdir sample asdf
cd sample_asdf

# インストール済み確認
asdf list python
# そのディレクトリ下でのみ有効化
asdf local python 3.7.10
```

conda とかもある
ターミナル上には mamba は認識されているが、優先度的に conda は miniforge を撮ってきている
=>指定するオプションとか使えば良いのかも
色々 conda 環境ある - zshrc とかの conda の設定によりそう

【メモ】

- asdf のバラード
- - [GitHub - asdf-vm/asdf: Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more](https://github.com/asdf-vm/asdf#ballad-of-asdf)

- `.tool-versions`に書いたもので asdf が自動でインストールしてくれる
  - よく git のディレクトリにある
