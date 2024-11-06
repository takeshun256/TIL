start：[[2023-11-12]] 13:47

### 設定方法

#### git コマンドを略す

- git を g と略す
  - bashrc や zshrc に書けば永続化する
  - これはしない
    - gzip とかも変換されてしまう可能性があるため

```python
~~alias g='git'~~
```

or

- git 自体のコマンド設定も git config で可能
  - これは、git 作業時にのみ有効化される

```python
git config --global alias.g '!git'
```

->

```python
git config --global alias.g '!git'
g st
g log
```

#### add -A や cm -m を略す

```python
cat ~/.gitconfig

git config --global alias.addA 'add -A'
git config --global alias.cmm 'commit -m'

->
g addA
g adda # 小文字も大文字も区別しないぽい
g cmm "first commit"
```

#### 現在の設定

```python
╰─ git config --global --get-regexp alias                                                                                                              ─╯
alias.co checkout
alias.st status
alias.br branch
alias.cm commit
alias.sw switch
alias.swc switch -c
alias.stt status -uno
alias.difff diff --name-only
alias.diffc diff --cached
alias.nffmerge merge --no-ff
alias.g !git
alias.adda add -A
alias.cmm commit -m
```
