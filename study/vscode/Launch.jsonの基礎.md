start：[[2023-07-31]] 03:48

launch.json

- Python のデバッグ設定を json で複数保持することができる

### 実際に launch.json を使用してみる

- 参考記事：[VS Code で Python コードのデバッグ構成をしてみよう：Visual Studio Code で快適 Python ライフ（1/2 ページ） - ＠IT](https://atmarkit.itmedia.co.jp/ait/articles/2107/30/news033.html)

1. 仮想環境作成 venv
2. 左サイドバーのデバッグから、launch.json を作成

3. ブレークポイントを適当に置く
4. F5 を押す。(もしくは、左サイドバーのデバッグから ▶️ をクリック)

- console
  - externalTerminal で、別のターミナルが起動し出力をそこに表示する

### launch.json の構成

- (参照：[VS Code で Python コードのデバッグ構成をしてみよう：Visual Studio Code で快適 Python ライフ（2/2 ページ） - ＠IT](https://atmarkit.itmedia.co.jp/ait/articles/2107/30/news033_2.html))
  - その他
    - [Debugging in Visual Studio Code](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes)
    - [Debugging configurations for Python apps in Visual Studio Code](https://code.visualstudio.com/docs/python/debugging#_set-configuration-options)

| 属性        | 説明                                                                                                                        | 備考                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| justMyCode  | その Python ファイルをノミを対象として、他の呼ばれた関数内では止まらない                                                    | 効率的にするため?                                        |
| stopOnEntry | プログラムの先頭行で必ず中断する                                                                                            | 前から順に見ていく想定の時に使用                         |
| console     | 出力先を、標準出力/デバッグコンソール/別ウィンドウのターミナルへ出力先を選択する                                            | 出力を見ながらやる場合は、internalConsole とか良さそう   |
| name        | デバッグ構成名, 左サイドバーの選択で出てくる表示名                                                                          | 目的別で設定を作りたいな                                 |
| request     | launch(ファイル実行) or attach(実行中のプロセスにアタッチするか)                                                            | 基本 launch で良さそう                                   |
| program     | 起動するファイルのパスの指定                                                                                                | 基本現在 active の{file}で良いかな                       |
| args        | プログラム起動時に渡す引数を指定                                                                                            | これらの設定を複数保持したいから複数設定を作ると良さそう |
| cwd         | 作業ディレクトリの場所を指定、相対パスの基準、[定義済み変数](https://code.visualstudio.com/docs/editor/variables-reference) | {fileDirname}だとそのファイルのあるディレクトリになる    |
|             |                                                                                                                             |                                                          |

### 設定の追加/複数持ち

- 参考：[Debugging configurations for Python apps in Visual Studio Code](https://code.visualstudio.com/docs/python/debugging)

  - debugpy 使っている

- 設定の追加方法
  ![[Pasted image 20230731210525.png]]

- debug 方法
  - F5
  - 左サイドバー
  - 右上の ▶️ ボタン

## その他参考

- [Visual Studio Code Variables Reference](https://code.visualstudio.com/docs/editor/variables-reference)

## まとめ(類似点・相違点)

debug 設定を複数保持して、それを選択することで簡単に debug できる
