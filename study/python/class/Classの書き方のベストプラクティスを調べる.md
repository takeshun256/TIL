start：[[2024-07-20]] 20:29
参考

- [class - Python Classes Best Practices - Stack Overflow](https://stackoverflow.com/questions/21584812/python-classes-best-practices)
- [Python Classes: The Power of Object-Oriented Programming – Real Python](https://realpython.com/python-classes/)

1. 属性参照は直接行うのが良い 1. もし、ロジックを組み込む場合は `property` デコレータを用い、値自体は`_value` のようにアクセスできなくしておく 2. `property` の反対で、値を設定する際のロジックは、 `@value.setter` を用いる
   > OOP の思想で、変数への処理やへんしゅうロジックはそのクラスや変数自体が持っていることが望ましい。理由としてもしエラーが発生した際に探す範囲を絞れるため。

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        self._value = value

obj = MyClass(10)
obj.value = 20  # setterが呼ばれ、_valueが20に設定される
print(obj.value)  # 20
try:
    obj.value = -5  # setterが呼ばれ、ValueErrorが発生する
except ValueError as e:
    print(e)  # "Value cannot be negative"

```

2. パブリック, 非パブリックな API
   1. メッソドの前に `_method_name`とすることでアクセスををアクセスしないことが推奨する設定
      1. => メソッドの `propoerty`とかで提供されている
      2. もしくは外部からアクセスされることが想定されていない
3. マングリング：名前の前に`__` をつけることでアクセス不可になり、クラス名を前に着けつつアクセスする必要になる `_Class__method`

### <span style="background:#40a9ff">Class の目的</span>

- 複雑な世界のモデル化
- コードの再利用
  - 繰り返しを避ける
- 関連するデータと動作を単一のエンティティにカプセルか
  - 単一のエンティティ=object
- 概念とオブジェクトの実装の詳細を抽象化可能
  - クラスとしてまとまった意味を見出す　機能の集合概念みたいな？
- 共通のインターフェースによるポリモーフィズムの実現
  - クラスの継承などインターフェースに合わせて微修正や上書きや継承をすることが可能

=> Python クラスは、より整理され、構造化され、保守しやすく、再利用しやすく、柔軟性があり、ユーザーフレンドリーなコードを書くのに役立ちます。

- ただシンプル(データの実の保持=>データクラスや名前付きタプル, 単一のメソッド=>関数)では使用しない
- シンプルなものは複雑なものよりも優れています。
- その他使用しない場面特に
  - シンプルなプログラミングやスクリプト
  - パフォーマンスが重要なコード
    - 多数のオブジェクトがある場合 h オーバーヘッドを追加する？
    - レガシーコードベース: コードのスタイルと合わないため
      - 一貫性がなくなる
    - 異なるコーディングスタイル: 現在のチームのコードに合わせ r；
    - 関数型プログラミング: 同様にコーディングパラダイムが崩れる

### クラスとインスタンス

- クラスは、データと動作を 1 つのエンティティにまとめる必要がある場合に最適
  - データが属性 , メソッドが動作
  - クラス共通のクラス属性, 特定インスタンスのインスタンス属性
- 内部クラス名をハードコーディングしない方法
  - `ObjectCounter.num_instances += 1`ではなく `type(self)`を利用することで可能

```python
class ObjectCounter:
    num_instances = 0
    def __init__(self):
        type(self).num_instances += 1
```
