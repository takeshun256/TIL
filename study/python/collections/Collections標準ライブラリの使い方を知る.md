start：[[2024-07-26]] 00:42

1. `Counter`: for 文使わずにリストからカウント辞書生成

```python
from collections import Counter

# リスト内の要素のカウント
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(elements)
print(counter)
# 出力: Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

2. `defaultdict`: デフォルト値のある辞書

   1. `list`=> リストや`int` => 0 初期値になる 2.　単純に追加すればよく `.get`などでエラーが出ない

3. `namedtuple`: フィールド値を持つタプル
   1. クラスで形式を定義, インスタンス作成=タプル作成
   2. フィールドによるアクセス, index アクセスではない

```python
from collections import namedtuple

# namedtupleの定義
Point = namedtuple('Point', ['x', 'y'])

# インスタンスの作成
p = Point(11, 22)
print(p)
# 出力: Point(x=11, y=22)

# フィールドアクセス
print(p.x, p.y)
# 出力: 11 22

```

- 名称表示と、フィールドアクセスするためのリストを初期化時に利用する

4. `deque`: 両端アクセスが可能なキュー

   1. `deque(list(～))`で初期化
   2. `append`, `pop` 後ろから
   3. `appnedleft` `popleft` 左から
   4. `rotate`で前後回転
   5. `deque(maxlen=n)` で最大長決められ初めのものから削除される

5. `orderdict`: 順序保持する辞書

   1. 既存の辞書と同じ
   2. `.move_to_end(key1)`メソッドである key の順序を最後尾へ

6. `ChainMap`: 複数の辞書を一つにまとめる、検索に使う

   1. `ChainMap(dict1, dict2)`　で初期化
   2. 両方の値を保持しており、単純に key アクセスすると先頭の辞書から優先して呼ばれる

7. `Userdict`: 辞書を継承してカスタム辞書クラスを作るためのクラス

   1. `class MyDict(UserDict): ` で普通の辞書をクラスとして継承できる

8. `UserString`: カスタム文字列クラス用

key が事前に決まっている辞書を扱う際

1. `Namedtuple` => 固定されたフィールド持つので辞書構造としても良い
2. `types.SimpleNamespace` => 同様

```python
from collections import namedtuple

# namedtupleの定義
Person = namedtuple('Person', ['name', 'age', 'address'])

# 辞書からnamedtupleを作成
person_dict = {'name': 'John Doe', 'age': 30, 'address': '123 Main St'}
person = Person(**person_dict)
```

```python
from types import SimpleNamespace

# 辞書からSimpleNamespaceを作成
person_dict = {'name': 'John Doe', 'age': 30, 'address': '123 Main St'}
person = SimpleNamespace(**person_dict)

print(person)
# 出力: namespace(name='John Doe', age=30, address='123 Main St')
```

【メモ】
標準ライブラリなので import そのまま可能 j

## 参考

## まとめ(類似点・相違点)

結構使われているものは少ない印象

`defaultdict` , `Counter` , `namedtuple`, `deque`くらい
