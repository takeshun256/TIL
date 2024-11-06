start：[[2023-03-04]] 03:50


## 参考

- https://xcfile.dev/getting-started/
- https://github.com/joerdav/xc


## 内容

xcifileは以下のようにREADME.mdを定義する。

```
------
## Tasks
### hello
Prints hello
```sh
echo hello
```
### world
Prints world
Requires: hello
```sh
echo world
```
---------
```


- Run `xc`
```
$ xc
    hello  Prints hello
    world  Prints world
           Requires:  hello

```

- run tasks
	- `xc <h3 taskname>`

```
$ xc world
echo hello
hello
echo world
world
```



### 流れ

| 実行                                 | 意味                           |
| ------------------------------------ | ------------------------------ |
| brew tap joerdav/xc; brew install xc; xc -version | レポジトリの登録とインストール               |
| README.mdを書く                      | タスクを定義する               |
| xc                                   | タスクを表示                   |
| xc "h3 taskname"                     | h3で定義されたタスクを実行する |
|                                      |                                |



## 類似点・相違点・まとめ

小さめのレポジトリなので、Readmeで付加的に使用しそう

使い所として、docとコードの開発時の内容の乖離をさせないようすることが、このレポジトリを導入するメリット
しかし、xcコマンドが使える形式のREADME.mdを作成する必要があり、面倒である。

