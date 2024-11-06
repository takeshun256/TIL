start：2023-01-27 00:25

```python
# 方法4: 多重ループ
from itertools import product
for i, j in tqdm(product(range(3), range(3))):
	# 何かの処理
```

## 類似点・相違点・まとめ

product で、多重を 1 つにまとめる。
tqdm を適用する。

これの問題点として、2 つのループの間に何か処理を挟む場合は、場合分けが必要になり面倒である。
そのため、i や j のみを使い分ける場合に使用する。
