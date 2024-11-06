start：[[2023-07-31]] 05:56

### install

```zsh
# armなので、初めの方に変数をつける
arch -arm64 brew install parallel
```

### 使い方

- [コマンドの並列化を行える『GNU parallel』の個人的使い方まとめ | 俺的備忘録 〜なんかいろいろ〜](https://orebibou.com/ja/home/201707/20170707_001/)

- citation してね見たいな出力がめちゃくちゃ出るので抑える引数

```sh
parallel --no-notice # citationを出力しない
```

- パイプで出力を受け取る

```sh
# コマンドの末尾に出力した値が入れられる
 | parallel 実行コマンド  

# 「--no-notice」で出力される警告文を非表示にする
 | parallel --no-notice 実行コマンド  

# {}で値を差し込む
 | parallel --no-notice 実行コマンド {}

# xargsの-Iオプションのように差込みを意味する記号を指定する事もできる
 | parallel -I@ --no-notice 実行コマンド @
```

- 例

```sh
seq -f '%03g' 1 100 | parallel --no-notice echo # 001~100まで出力
```

| 引数                          | 使い方                                                                 |
| ----------------------------- | ---------------------------------------------------------------------- |
| -j                            | 並列実行数                                                             |
| -n                            | 一度に渡すリストの要素数                                               |
| -X                            | 複数プロセス並列実行しないようにする->遅くなる                         |
| -colsep                       | デリミタを指定                                                         |
| :::                           | 手書きしたスペース区切りの文字を入力を受け取る                         |
| -a File                       | File の中身を入力に受け取る                                            |
| ::::                          | -a と同様                                                              |
| perl ポイ正規表現を使用できる |                                                                        |
| {}による置換方法              | [GNU parallel 文法メモ](https://zenn.dev/link/comments/0ad48bd93e93cc) |

### 実例

- [GNU Parallel 作者が書いた Parallel:The Command-Line Power Tool を読んだ – Siguniang's Blog](https://siguniang.wordpress.com/2012/09/09/notes-on-gnu-parallel-the-command-line-power-tool/)

  - コア数とかの話
  - リモートで実行する
    - サーバーで実行するの良い!

- [GNU parallel 文法メモ](https://zenn.dev/s10018/scraps/a53902d994e3a5)
  - わかりやすい
  - 公式ドキュメントの見方を教えてくれる
  - ファイルの置換
    - [GNU parallel 文法メモ](https://zenn.dev/link/comments/0ad48bd93e93cc)

```sh
# shellスクリプトを実行
# seq 1 <回数> | parallel -j <並列実行数> -n <引数の数> ‘<実行コマンド>’
seq 1 6 | parallel -j 1  -n 1 'sh process.sh'


# printfを使う
seq 1 10 | parallel printf "%d--" {}
# 1--2--3--4--5--6--7--8--9--10--

# コマンド引数を手書きする場合(:::の後にスペース区切りで書く)
parallel echo ::: 1 2 3 4 5
parallel echo ::: S M L ::: Green Red # 2重ループ
parallel 'echo counting {}; wc -l {}' ::: example.* # ワイルドカード使うと便利


# ファイルの中身を並列で受け取る
parallel -a abc-file -a def-file echo # 各行で2重ループになる

```
