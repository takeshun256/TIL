start：[[2023-08-26]] 12:33

### 基本的な使い方

```python
import argparse

# ArgumentParser オブジェクトを作成
parser = argparse.ArgumentParser(description="これはプログラムの説明です。")

# 引数を追加
parser.add_argument("positional_arg", type=int, help="これは位置引数です。")
parser.add_argument("--optional_arg", type=str, help="これはオプション引数です。")
parser.add_argument("-s", "--short_and_long", type=str, help="短い形と長い形の両方を持つオプション引数です。")

# 引数を解析
args = parser.parse_args()

# 引数を使用
print("位置引数: ", args.positional_arg) # 10
print("オプション引数: ", args.optional_arg) # オプションです
print("短い形と長い形: ", args.short_and_long) # 短い形です

```

呼び出し

```python
python script.py 10 --optional_arg "オプションです" -s "短い形です"
```

#### ファイルパスを入力にとるときにあるかどう確認したいとき

```python
parser = argparse.ArgumentParser()
parser.add_argument("--input", type=argparse.FileType("r"), required=True)
args = parser.parse_args()
img = args.input # FileType
img_str = args.input.name # str
```

そのまま取り出す、FileType になるので、.name で str を取り出せる。
Path(FileType)はエラー出る
