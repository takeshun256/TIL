start：[[2023-03-21]] 02:54

## 経緯・背景

通常では pyenv で環境をインストール使用すると以下のエラーが出たるため

```python
╰─ pyenv install 3.9.0                                                       ─╯
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Downloading Python-3.9.0.tar.xz...
-> https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz
Installing Python-3.9.0...
patching file 'Misc/NEWS.d/next/Build/2021-10-11-16-27-38.bpo-45405.iSfdW5.rst'
patching file configure
patching file configure.ac
python-build: use tcl-tk from homebrew
python-build: use readline from homebrew
python-build: use zlib from xcode sdk

BUILD FAILED (OS X 13.2.1 using python-build 20180424)

Inspect or clean up the working tree at /var/folders/7h/kc_ssb2j1917v1fvjt5hk94r0000gn/T/python-build.20230321025336.83514
Results logged to /var/folders/7h/kc_ssb2j1917v1fvjt5hk94r0000gn/T/python-build.20230321025336.83514.log

Last 10 log lines:
checking size of _Bool... 1
checking size of off_t... 8
checking whether to enable large file support... no
checking size of time_t... 8
checking for pthread_t... yes
checking size of pthread_t... 8
checking size of pthread_key_t... 8
checking whether pthread_key_t is compatible with int... no
configure: error: Unexpected output of 'arch' on OSX
make: *** No targets specified and no makefile found.  Stop.
```

## 参考

- https://qiita.com/tomtsutom0122/items/52487730001247fdc2c5

## 内容

参考：https://qiita.com/tomtsutom0122/items/52487730001247fdc2c5

### 原因

エラー内容から、arch(M1 mac)に対応していないようである-> 指定する必要あり
homebrew が 2 つインストールされている -> env で homebrew のパスを指定する必要がある

### 解決策

- 環境をインストールするときはこれをいつも使う必要がある

```python
arch -arch x86_64 env PATH=${PATH/\/opt\/homebrew\/bin:/} pyenv install 3.8.7
```

- 使用するときは普通に呼び出して使える
  - チートシート：https://sig9.org/archives/2467

```python
pyenv versions # 保存してあるバージョンを表示
pyenv global 3.9.0
python --version # Python 3.9.0
```

### パスを記載

- 以下を zshrc に記載する
  - https://hastaluegoblog.hatenablog.com/entry/2023/02/23/210025

```zsh
# pyenv path
# settings: https://hastaluegoblog.hatenablog.com/entry/2023/02/23/210025

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

### pyenv の使い方

- https://sig9.org/archives/2467

```python
pyenv versions # 保存してあるバージョンを表示
pyenv global 3.9.0
python --version # Python 3.9.0
```

## まとめ(類似点・相違点)

エラー分の読んで色々な解決策を考えられる人すごいな

環境インストール時には以下を使う

```python
arch -arch x86_64 env PATH=${PATH/\/opt\/homebrew\/bin:/} pyenv install 3.8.7
```

## 振り返り

エラーぶんをまず初めに読む
公式ドキュメントのインストール方法は参照する

- pyenv のインストール方法とか

パスを書くことに抵抗を覚えない

- 誤った修正方法だったら大変とかは後回し
