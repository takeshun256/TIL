start：[[2023-02-27]] 22:28

## 経緯・背景

Linux の sbin と share とかわからなかったため

## 参考

- https://www.youtube.com/watch?v=ZtqBQ68cfJc
- https://youtu.be/HbgzrKJvDRw

## 内容

ディレクトリの説明

- ユーティリティは、基礎コマンドとかが入っている
  - ls とか cat とかのファイル
  - シェルから直接実行可能 名前で呼び出せる

### usr/local と usr/share と usr/src の使い分け

- usr/local は色々なファイル
- usr/share はサイズが大きい色々なファイル
- usr/src はソースコードとかのやつ

### 基礎コマンド

- https://www.freecodecamp.org/news/the-linux-commands-handbook/
  わからないものだけ

| コマンド                                 | 意味                                     |
| ---------------------------------------- | ---------------------------------------- |
| tail -f                                  | 末尾を追跡                               |
| less -N                                  | 行番号を表示しながらページ単位で表示     |
| chmod                                    | ファイルやディレクトリのアクセス権限変更 |
| chown                                    | ファイルやディレクトリの所有者を変更     |
| ps -a                                    | 実行中のプロセスを他のユーザーも表示     |
| tar -zcvf 保存先 path/~.zip ディレクトリ | ディレクトリを zip に固める              |
