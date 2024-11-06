start：[[2023-03-16]] 20:11

## 経緯・背景

pytest で src ディレクトリが見つかりませんで苦労したため

## 参考

https://zenn.dev/pesuchin/articles/9573476d53d234f09433

## タスク

- [x] 理由と解決策の把握

## 内容

理由

- pytest では、`pytest`を実行すると、以下の流れで処理する
  - tests ディレクトリ内の test\_から始まるディレクトリとファイルを再起的に探索する
  - そして、それぞれのテストから、上の階層に向かって、`__init__.py`が初めてない場所を探索する
  - そのディレクトリのパスを basedir として、sys.path に登録する
    - tests ディレクトリ下全てのディレクトリに`__init__.py`を置いておくと、basedir はプロジェクトルートディレクトリ(src ディレクトリが置いてある場所)になる。
    - そのため、test ファイルに`import src...`とか書かれる import できる。

解決策

- 上記の通り、tests ディレクトリした全てのディレクりに`__init__.py`があると、ルートパスでも tests 内のどこからでも実行して src を import できる。
- でも tests 下には`__init__.py`を起きたくない場合は、ルートパスから、`python -m pytest tests/.../test_sampel.py`を実行すると、src が import される。
  - 重要なんは、`python -m pytest`をルートパスから実行すること
  - うまくいく理由としては、python が 3.7kara,`__init__.py`がなくても探索できるのが理由とのこと

【メモ】

## まとめ(類似点・相違点)

`python -m pytest`をルートパスから実行すること

## 振り返り

理由と解決策が理解できてよかった
