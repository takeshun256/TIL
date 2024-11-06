start：2023-01-26 20:57

## 経緯・背景

Logger を使っているコードを見つけて、便利だと思ったが、ないもわからないままコピペしても上手く使えない気がしたため。
それよりは勉強して、うまく使ったほうが良いと思ったから。

## 参考

- Kaggle
  - https://www.kaggle.com/code/fujino15rin/fork-of-train-deberta-v3-base
- 使い方
  - https://zenn.dev/wtkn25/articles/python-logging
  - https://docs.python.org/ja/3/howto/logging.html
  - config
    - https://docs.python.org/ja/3/library/logging.html?highlight=funcname#:~:text=%E3%81%A6%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82-,%E5%B1%9E%E6%80%A7%E5%90%8D,-%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88
  - handler
    - https://qiita.com/shotakaha/items/0fa2db1dc8253c83e2bb
-

## 内容(GPT回答で大体OKだったので添付)

1.  ogging モジュールをインポートします。
2.  ログレベルを設定します。(debug, info, warning, error, critical)
3.  ハンドラーを設定します。(ファイルや標準出力)
4.  ロガーを取得します。
5.  ログを出力します。

```python
import logging

# ログレベルを設定
logging.basicConfig(level=logging.DEBUG)

# ハンドラーを設定
logger = logging.getLogger(__name__)

# ログを出力
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

```

これにより、ログレベルが debug 以上なら debug、info、warning、error、critical のログが出力されます。

また、ハンドラーを指定しない場合、標準出力に出力されますが、ハンドラーを指定すれば、ファイルにも出力することができます。

これらの詳細については、公式ドキュメントを参照してください。 [https://docs.python.org/ja/3/library/logging.html](https://docs.python.org/ja/3/library/logging.html)

- when, where, what の迅速な特定に助かる
  - handler の設定によって、どのレベル, 詳細なモデュール場所、メッセージ
  -

流れ

1. import
2. Config(`logging.baseConfig()`)
   1. filename
      1. run.log
   2. level
      1. debug、info、warning、error、critical
      2. logging.DEBUG とか書く
   3. encoding
   4. filemode = "w"
   5. `format='%(asctime)s %(levelname)s:%(message)s'`
   6. `datefmt='%m/%d/%Y %I:%M:%S %p'`
3. logger
   1. `logger=logging.getLogger(__name__)`
4. handler
   1. 概要：config 下でより詳細な config を設定する用/config が下に設定されテいる=baseconfig
   2. それぞれ
      1. どこで起きたかを占めす(以下はモデュール名を出力)
         1. `logger=logging.getLogger(__name__)`
      2. 送信先を決める
         1. `logger=logging.get`
      3. どのレベル以上を対象にするか ``
   3.
5. output
   1. `logging.info("Error")`
   2. `logging.warning("%s of error", value)`

2~4 まで、(config, logger, handler)までを関数にまとめている。

- LOGGER = get_logger(filename=~)
- 関数名は、setup_logger とか

baseconfig をいじるよりは、getLogger ごに handler で各種設定したほうが良い

標準出力と log にしゅつ力したい場合は、FileHandler と StreamHandler を logger に addHandler をする必要がある。

- 通常は両方は出力してくれない

### chatgpt の添削

> 改善点として、以下のような点が挙げられます。

1.  ログレベルの設定について: 現在の設定では、ログレベルが`info`以上のログが出力されます。アプリケーションによっては、`debug`レベルのログも出力したい場合もあるため、必要に応じてログレベルを変更してください。
2.  フォーマットの設定について: 現在の設定では、ログの出力フォーマットが"%(message)s"になっています。これは、ログメッセージのみを出力する設定です。ただし、ログの詳細を確認するためには、時間やログレベルなどの情報も出力する必要があるため、必要に応じてフォーマットを変更してください。
3.  ファイルハンドラーの改善点: ファイルハンドラーを使用していますが、それが正しく動作しているかどうかは不明です。必要に応じて、ファイルハンドラーが正しく出力先にログを出力しているか確認してください。
4.  ファイルパスの改善点: 現在のコードでは、出力先のファイルパスはハードコーディングされていますが、実際のアプリケーションでは、このようなハードコーディングは避けるべきです。実行時に指定するように変更した方が良いです。

これらの改善点を踏まえ、アプリケーションに合わせて調整していくことで、より適切なログ出力が実現されると思います。

## 類似点・相違点・まとめ

別の logger

- https://qiita.com/ko-he-8/items/3247e16881cf9ba45c8a
- logzero
- loguru
- pylogrus

簡単や便利だったりするが、ほとんど変わらない
