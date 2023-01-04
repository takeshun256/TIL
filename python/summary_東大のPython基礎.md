参考：[Open in Colab](https://colab.research.google.com/github/utokyo-ipp/utokyo-ipp.github.io/blob/master/colab/index.ipynb)

知らなかったことや覚えておきたいことをメモする

## 2.変数
1. 予約語：defやreturnなどpythonないで設定されている文字

### 関数
1. returnを設定しないと、return Noneとして定義される
2. 関数内だけで定義され利用可能な変数：ローカル変数
3. 関数外で定義される変数：グローバル変数
	1. 関数内で参照することもできる

## 3.論理・比較演算と条件分岐の基礎
1. 真理値(TrueまたはFalse)：組み込み定数
2. オブジェクトとは、値や変数の値もすべてobject
3. 再帰：定義するもの自身を定義の中で参照すること

## 4.デバッグ

### エラーの種類
参考：https://docs.python.org/ja/3/tutorial/errors.html
(logging, pytestとか使用してデバッグしてみたい)
(エラーを記録するときにこの性質をまず添付するとかかな)
1. 文法エラー：Syntax Errors
	1. Python文法に違反しているエラー
	2. 対処
		1.  まず、エラーメッセージを確認
		2.  エラーメッセージの最終行を見て、それが `SyntaxError` であることを確認
		3.  エラーとなっているコードの行数を確認
		4.  そして、当該行付近のコードを注意深く確認
2. 実行エラー：Runtime Errors
	1. コードの実行時に検出されるエラー
	2. 対処
		1.  まず、エラーメッセージの確認
		2.  エラーメッセージの最終行を見て、そのエラーのタイプを確認
		3.  エラーとなっているコードの行数を確認
		4.  そして、当該行付近のコードについて、どの部分が実行エラーのタイプに関係しているか確認
		5. もし複数の原因がありそうであれば、行を分割、改行して再度実行し、エラーを確認
		6.  原因がわからない場合は、 `print` を挿入して処理の入出力の内容を確認
3. 論理エラー：Logical Errors
	1. 自分の中でのエラーの場合分けに当たる(Pythonで出力されるわけではない)
	2. プログラムを実行できるが、プログラムが意図したように動作しないエラー
		1. 入力に対する期待される出力と実際の出力を確認
		2. コードを読み、期待する処理と異なるところを見つける
		3. print分で入出力を確認

### コーディングスタイル=コードの書き方
バグによるエラーを出さないことが大切
可読性も大事
PEP8というスタイルガイドがある
- http://pep8-ja.readthedocs.io/ja/latest/
- https://www.python.org/dev/peps/pep-0008/
例
-   インデントは半角スペースを4つで1レベル
-   `=` `+=` `==` などの演算子の前後に半角スペースを1つ入れる
-   `*` と `+` の複合式では `+` の前後に半角スペースを1つ入れる（例：`2*x + y`）
-   関数の開き括弧の前にスペースを入れない
-   `l` `I` `O` を変数名として使わない
-   真理値の比較に `==` や `is` を使わない

PEP8自動検査機：pycodestyle
https://pypi.org/project/pycodestyle/
オンラインサービス：PEP8 online
http://pep8online.com/

可読性
読みやすく、勘違いしないコードを書く
- 自己説明的でない“マジックナンバー”ではなく記号的に意味がわかる変数を使う
- 不要なコードは削除する
- 1つの関数では1つのタスクだけを処理する
- docstringとかをかく

### ASSERT文によるデバッグ
1. 論理エラーをみつけるためによく使用される
2. assert "条件文"として、条件文がFalseなら、AssetionErrorを発生させる
	1. エラー文出力指定は書かない方がよいかも(論理エラーだからエラー原因がわからないため)
	2. 場所はエラー文で何行目かわかるため

## 2.1.文字列
空文字=""
スライスは[1:4]とか最後の数字は+1する
[-1]で最後のindexを指定できる

### 文字列検索
"mozi" in "moziretuA"：bool値

### エスケープシーケンス
1. 'moziretu'内に'を含めたい場合に使用する
	例：'文字列\'mozi\''
2. 'シングルクォーツ'内に""は使用できる(逆もしかり)
3. その他
	1. \" ("を入れたい時)
	2. \\ (\を入れたい時) 
	3. \n (改行)
	4. """ """で複数行や上記のエスケープシーケンスを回避できる
4. \と￥はフォントによって見え方が異なり、￥はPythonでは使用できない(Unicode `U+005C`)

### メゾット
1. 連結："moziretuA"+"moziretuB"
2. 置換：文字列.replace(部分文字列A, 文字列B)
	```
	word1 = 'hello'
	word1.replace('l', '123')
	```
3. 分割：文字列A.split(区切り文字列B)
	```
	fruits1 = 'apple,banana,cherry'
	fruits1.split(',')
	```
4. 検索：文字列A.index(部分文字列B)
	1. 見つからない場合はエラー
	2. 初めに出現するindexを返す
	3. .find()の場合は、見つからない場合エラーではなく-1を返す
	```
	word1 = 'hello'
	word1.index('lo')
	```
5. 数え上げ：文字列A.count(部分文字列B)
6. 大文字・小文字
	1. 小文字化：文字列.lower()
	2. 大文字化：文字列.upper()
	3. 先頭文字を大文字化：文字列.capitalize()
7. 大小比較は、辞書での順番(早いと小さい)

## 2.2.リスト
1. +でリスト結合
2. \*でリストの繰り返し
3. もし、y=x*3とかしたら、xの変更でyも複数個所変更される
4. in で要素として含まれるかboolを返す
5. リスト.index(要素)：要素のindexを返す
6. リスト.sort()：元のリストを昇順にソートする
7.  リスト.sorted()：昇順にソートしたものを返す
8. リスト.count(要素)：要素の数え上げ
9. リスト.insert(index, 新しい要素)：indexに新しい要素を追加
10. リスト.remove(要素)：要素を削除(複数の場合は初出現のみ, ない場合はエラー)
11. リスト.pop(index)：元のリストのindexの要素を削除し、その要素を返す
12. del リスト(要素)：要素を削除、要素のスライスで削除も可能, 破壊的
13. リスト.reverse()：順序を逆にする

sort()のようにもとのリストを変更するような操作を破壊的あるいはインプレース(inplace)と呼ぶ⇔非破壊的(sorted()などの元のリストを破壊しない者)

### タプルについて
文字列やTupleはimmutable(変更不可能)、listはmutable(変更可能)
	1. 変更しない場合はタプルを使用するべき
	2. 関数の return はtupleをしようしたり
	3. 空Tuple = ()
	4. 代入は不可だが、参照はできる(Tuple)[x]やスライスも可能)
	5. tuple(list)やlist(tuple)で相互変更可能
	6. for i in (tuple)も可能

### オブジェクトの等価性と同一性
1. 演算子== でオブジェクトの等価性を判定
2. 演算子is でオブジェクトの同一性を判定

二つの違い
並んでいる10円玉2つを思い浮かべる
その2つは、等価だが、同一ではない
1. 等価は、等しい存在かどうか
2. 同一は、同じ存在かどうか

## 2.3.条件分岐
長い処理を`\`で複数行にできる
andやorは条件が左から順に評価され、不要な評価は省かれる
	1. `True or ~` は左のTrueで評価終了
	2. `False and ~` は左のFalseで評価終了

3項演算子
`a = x if 条件文 else y`
これは、if else文で複数行書くのと同義

## 3.1.辞書
キーが辞書に登録されているかは`in` で把握

登録は代入で行う
	1. 辞書[key] = value

削除
	1. del 辞書[key]
	2. 辞書.pop(key)：削除して、そのkeyに対応するvalueを返す
	3. 辞書.clear()：全削除して空辞書にする

一覧を見る
	1. 辞書.keys()：キーの一覧
	2. 辞書.values()：valueの一覧
	3. 辞書.items()：(key, value)の一覧
	4. これらは元の辞書に紐づいて動的に変化する

Valueを取り出す
	1. 辞書[key]の場合は、存在しない場合エラーが出る
	2. 辞書.get(key)で存在する場合はValueを、存在しない場合はNoneを返す
	3. 辞書.get(key, Object)で存在しない場合はObjectを返す

キーがない場合に登録を行う
	1. 辞書.setdefault(key, v)を使用する
	2. 指定したキーが辞書に含まれる場合は、対応するvalueを返す
	3. キーが含まれない場合、2番目の引数の値を返し、キーに対応するvalueとして登録する

## 3.2.繰り返し
`ord` は与えられた文字の文字コードを整数として返す
`chr` は逆に与えられた整数を文字コードとする文字を返す

文字列の文字ごとの頻度を比較するコード
```
word = 'supercalifragilisticexpialidocious'
height = [0] * 26
# aを0として、zまで1ずつ文字コードが大きくなってくことを利用
for c in word:
	height[ord(c) - ord('a')] += 1
import matplotlib.pyplot as plt
left = list(range(26))
labels = [chr(i + ord('a')) for i in range(26)]
plt.bar(left,height,tick_label=labels)
```

辞書の繰り返し
`for key, value in dic.items():`

二項分布を作るコード
```
C = [[1]]
for i in range(100):
	C.append([1]+[0]*i+[1])
	for j in range(i):
		C[i+1][j+1] = C[i][j] + C[i][j+1]
C[:10]
#############
[[1], 
[1, 1], 
[1, 2, 1], 
[1, 3, 3, 1], 
[1, 4, 6, 4, 1], 
[1, 5, 10, 10, 5, 1], 
[1, 6, 15, 20, 15, 6, 1], 
[1, 7, 21, 35, 35, 21, 7, 1], 
[1, 8, 28, 56, 70, 56, 28, 8, 1], 
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
###########
plt.plot(C[100]) # 正規分布みたいな二項分布ができる
```

break：forやwhileを中断し、最も内側のループも終了させる目的で使用
continue：forやwhileを中断し、次の最も内側のループを開始する目的で使用

forやwhileにelse文があり、ループが終了した際にelseが実行される。
	1. ただし、breakで終了した際は実行されない

`from time import sleep` して、`sleep(n)`でn秒停止

## 3.3.関数
関数とは、処理をまとめた再利用可能なコード
	1. 名前を持つ
	2. 手続きの流れを含む
	3. 返値を返す(明示的、非明示的)

グローバル変数と同じ名を持つローカル変数を使用しない/定義しない
関数名と変数名が重なると参照が最新のものを参照するので大変
- 関数も変数である!!
関数内でグローバル変数を更新する際は`global` 宣言を使用する
```
def greeting():
	global greeting_global
	greeting_global = "Hello!"
	return greeting_global
```

関数定義
順番は位置引数が最初に指定される必要がある
順番：def 関数名(位置引数, キーワード引数, 可変長引数, 辞書型可変長引数)
1. **位置引数**：変数のみ
2. **キーワード引数**：変数=キーワード
	1. キーワードが初期値となる
3. **可変長引数**
	1. `*args` のように`*` が引数の前にあると、複数の位置引数のタプルを受け取れる
	2. `**kwargs` のように`**` が引数の前にあると、複数のキーワード引数を辞書形式で受け取れる
	3. 関数へ渡す際は
		1. リストやタプルの形の場合、`greeting(*greeting_list, **greeting_dic)` のようにする
		2. 普通に渡す場合は、(位置引数1, 位置引数2, キーワード引数1, キーワード引数2)のように何個でも渡せる


## 4.1.ファイルの入出力 
参考：https://docs.python.org/ja/3/tutorial/inputoutput.html#reading-and-writing-files
### ファイル操作
ファイルオープン
```f = open('sample.txt', 'r')``` 
変数f：ファイルオブジェクトといい、ファイルを読み書きするためのデータが入る
モード
	1. r：読み込み
	2. w：書き込み
	3. a：追記
	4. +：読み書き両方を指定したい場合
ファイルクローズ
ファイルオブジェクトは使用し終わったら、閉じておく必要がある(いつまでも消えない)
`f.close()`
### ファイルオブジェクトへの操作
行の読み込み
1. `readline()`：新たに1行読んで文字列を返す(ファイル終わりor 改行迄)
	1. 読み込むものがないときは、""を返す
	2. ファイルオブジェクトを更新するため、改めて読みだす場合は、再度openする
ファイル全体の読み込み
1. `read()` ：ファイル全体を一括で読み込んで、1つの文字列を取得する
	1. ファイルの終端に到達する(再度行うと空文字列""を返す)
with文
処理後に自動で、ファイルのクローズを行ってくれる(`close()` 不要)
```
with ファイルオブジェクト as 変数:
	....
例
with open("sample.txt", "r") as f:
	print(f.read())
```
ファイルへの書き込み
	書き込みモードは`w` で指定
	`print` 関数で行う
	`file` 引数に書き込み先のファイルオブジェクトを指定する
		1. `\n`：改行文字(エスケープシーケンスの1種)
		2. `\r`：復帰文字, `\t` ：タブ
```
with open('print-test.txt', 'w') as f:
	print('hello\nworld', file=f)
```
print関数は、デフォルトで、与えられた文字列の末尾に`\n` を加えて書き込む
	1. `end` 引数で末尾に加える文字を指定可能
	2. `print('hello', 'world\n', end='', file=f)` 
複数の印字対象(printの引数)を渡すと、デフォルトで空白文字で区切って印字する
	1. 区切り文字は`sep` 引数で指定可能
	2. `print('hello', 'world', sep=', ', file=f)` ：'hello, world\n'が印字
それ以外の書き込み
`write()` を使用した原始的な方法
	1. 与えらえた1つの文字列を単に書き込む
	2. `read()` と対でよく使用される
	3. 以下はsample.txtをsample.txt.bakへコピーする
```
with open('sample.txt') as src, open('sample.txt.bak', 'w') as dst:
	dst.write(src.read())
```
### 文字コードの指定
`open()` でファイルを開く際に、そのファイルをテキストモードで開く(他：バイナリモード)
	1. その際に特定の文字コードでファイルを開く
	2. 指定しない場合はデフォルト(WindowsはShift_JIS、macOSやLinuxはUTF-8)
	3. お互いに文字コードが違う場合に文字化けやエラーが起こる
	4. 半角英数字は共通のルールでエンコードされている
	5. エラー例：```'utf-8' codec can't decode byte 0x82 in position 0: invalid start byte``` 
対処方法
	1. 特に半角英数以外の文字を記録する際は文字コードを指定する
	2. またそのようなファイルを開くときは、記録するときに指定した文字コードでファイルを開く
	3. `open(encoding='utf-8')` のように引数に指定する
	4. Pythonでの日本語の文字コードの推奨は、UTF-8(他はshift-jisやeuc-jpがある)
### 改行文字を削除するコード例
```
with open('text/novel.txt', 'r', encoding='utf-8') as f:
	while True:
		line = f.readline()
		if line == '':
			break
		print(line.rstrip('\n'))
```
with内に複数の`open`を置ける
```with open(infile, 'r') as f, open(outfile, 'w') as g:```
## 4.2.イテレータ
参考：https://docs.python.org/ja/3/tutorial/classes.html#iterators
ファイルオブジェクトは、イテレータというオブジェクトの一種
イテレータ(繰り返すの意)は、要素をひとつずつ取り出す処理が可能
### next
1つずつ取り出す処理を1回分行う
例
```
f = open('sample.txt', 'r')
next(f)
next(f)
# StopIteration:

f.close()
```
ファイルの終わりが来た時の挙動が`f.readline()` と違う
	1. `f.readline()` は空文字''を返す
	2. `next(f)` は`StopIteration:` というエラーを返す
### for文にイテレータを指定可能
1. イテレータは、for文の`in` に指定できる。
2. 繰り返しごとに`next(f)` されたものが、変数に入る。
3. for文でイテレータを使用すると、イテレータは最後まで達しているので、再度for文は回せない
```
with open('sample.txt', 'r') as f:
	for line in f:
	print(line)
```
### iter
`iter(list)` でリストからイテレータを作成
1. for文では、内部で、リストに組み込み関数`iter` を適用するような処理がされている
2. iter(イテレータ)は、元のイテレータが返る(同一性がある：`is` で確認可能)
### イテラブル
関数`iter` が適用できるオブジェクトをイテラブルと呼ぶ
	1. イテラブルは、forの`in` 後に指定できる
		1. イテレータは、イテラブルである
		2. リストは、イテラブルだが、イテレータではない
		3. 関数`range` が返すオブジェクトはイテラブルだが、イテレータではない
	2. enumerate(イテラブル)
## 4.3.ディレクトリ構造
逆さツリーのようなデータ形式を木構造という
1. 一番根っこに当たるデータをルート(根)：ディスクなどの記憶媒体自体
2. 先端に当たるデータをリーフ(葉)：ファイル
3. その間にあるデータをノード(節)：フォルダ
カレントディレクトリ
1. プログラムを実行する際の今のディレクトリのこと
2. 実行時にファイルを見つける際は、カレントディレクトリからのファイルのパス(経路)を指定する
### 相対パスと絶対パス
相対パス：カレントディレクトリとファイル間のパスの関係
絶対パス：カレントディレクトリの場所にかかわらず、ルートからのパス(常に同じファイルを指定できる)、`/`から始まる
一つ上：`../`
## 5.1.モジュールの使い方
参考
	1. https://docs.python.org/ja/3/reference/import.html
	2. https://docs.python.org/ja/3/tutorial/modules.html
モジュール
1. 特別な関数や値をまとめたもの
2. `import モジュール名`
3. モジュール内の関数の使用方法： `モジュール名.モジュール内の関数名`
### fromによるimport
モジュール内の特定の関数だけ読み込みたい場合
```from モジュール名 import モジュール内の関数名```
1. 使用は、`モジュール内の関数名` で利用できる
関数だけでなく、グローバル変数やクラスもimportするにはワイルドカード`*` を使用
```from モジュール名 import *```
1. これは非推奨である
	1. 読み込んだモジュール内の未知の名前とプログラム内の名前が衝突する恐れがある
### asによる命名
モジュール名を訳したい時に利用
```import numpy as np``` 
```from math import factorial as fact```
## 5.2.モジュールの作り方
参考
	1. https://docs.python.org/ja/3/tutorial/modules.html
	2. https://docs.python.org/ja/3/reference/import.html
プログラムをモジュールという単位で、複数のファイルに分割する
	1. 便利な関数などの再利用したい部分をモジュールとして切り出す
	2. プログラムが大きくなると、複数のファイルに分割した方が、開発や保守が簡単になる
モジュールファイルの形式
1. pyファイル
2. エンコード(読み書き)時の文字コードはUTF-8が推奨
colabへファイルアップロードのコード例
```
import sys
if 'google.colab' in sys.modules:
	from google.colab import files
	uploaded = files.upload() # Upload to the current directory
```
### 自作モジュールの使い方
カレントディレクトリからの当該ファイルのパスをimportすればよい
ただし、ディレクトリごとimportする場合はinit.pyが必要
1. モジュールファイルがカレントディレクトリにある場合(モジュール名=~.pyの~部分)
	1. import モジュール名
	2. ワイルドカードは非推奨(オブジェクト名の衝突の恐れ)
	3. fromやasの利用
## 5.3.Numpy
配列とは、特定の型の値の並び：`np.array()` で構築
### 要素型
主に４つ
1. `np.int32`：整数(32-bit)
2. `np.float64`：実数(64-bit)
3. `np.comlex128`：複素数(64-bit実数の組)
4. `np.bool_`：真理値
確認方法
`type(array)`
指定方法
`np.array(list, dtype=np.int32)`
1. np.int32とかじゃなくても、int32, float64, bool, complex128などでも同様に指定可能
32bitは、2の32乗を半分ずつ-2^16~+2^16の範囲まで表現できるようなデータ型
### 多次元配列の処理
これらは、元の配列と内部データを共有している
`array.reshape(shape)` ：配列の形を更新、(-1, 1)で列ベクトル、(1, -1)で行ベクトル化
`array.ravel()`：多次元配列を1次元配列へ変換
`array.flatten()`：要素をコピーして、多次元配列を1次元配列へ変換
	1. コピーしない`ravel()` の方が何かと効率的
### 配列のデータ属性
配列は、オブジェクトであり、様々な情報を属性として保持している
代表的なデータ属性(メソッド=組み関数?以外)
1. `a.dtype`：配列の要素型
2. `a.shape`：配列の形(各次元の長さのタプル)
3. `a.ndim`：配列の次元数(=`len(a.shape)`)
4. `a.size`：配列の要素数(=`a.shape`の総乗)
5. `a.flat`：配列の1次元表現(`a.ravel()`と等しい)
6. `a.T`：配列の転置配列(元配列と要素を共有)
### 構築関数
`np.arange`：range関数を実数に拡張したもの(start=0, stop,刻み幅=1)
`np.linspace()`：範囲を等分割した配列(start, stop, 分割数)
`np.zeros()`, `np.ones()`：0, 1からなる配列((shape))：dtypeはfloat
`np.identity(shape)`：単位行列
`np.random.rand()`：0以上1未満の乱数からなる配列(shape)：dtypeはfloatのみ
	1. `np.random.randn()`：正規分布の乱数
	2. `np.random.binomial()`：　二項分布の乱数
	3. `np.random.poisson()`：ポアソン分布の乱数
### for文
`for idx, enum in np.edenumerate(array)`
	1. 多次元配列版のenumerate()
	2. 多次元のidxと要素enumの組をすべて列挙する
### 配列演算
1. スカラー演算や行列間演算はユニバーサル演算
2. 比較演算は、要素毎に演算され、真理値の配列を返す
	1. `array[(array>2) & (array%2==0)]`のようにインデックスで抽出できる
	2. `array[array>8]=2`のように要素を上書きもできる
	3. `and or not`は真理値を返すが、`& | ~` は要素毎の計算を行うためこちらを使用する
ユニバーサル関数
	1. 配列の各要素に所定の演算を与えた結果を返す関数：例 `np.sqrt()`
	2. 一覧：https://docs.scipy.org/doc/numpy-1.14.0/reference/ufuncs.html#available-ufuncs
2. 配列演算
	1. `np.dot(array1, array2)`：2配列のドット積、両者ベクトルの場合は内積
		1. `np.matmul(array1, array2)`は行列積専用(内積はない)
	2. `np.sort()`：sorted()の配列版、非破壊的
	3. `sum`, `max`, `min`, `mean`：全要素を集計、axis=0で各列、axis=1で各行にメソッドを適用
	4. `np.linalg.norm(array)`：ノルムを返す(デフォルトはユークリッドノルムL^2 )
		1. 線形代数関連：https://docs.scipy.org/doc/numpy/reference/routines.linalg.html
### 配列の保存
`np.savetxt("ファイル名.txt", array)`
	1. テキスト形式で配列を保存、行は改行、列は空白区切り
	2. 列の区切り文字の指定：`delimiter=""`
	3. 大規模な配列を保存する際
		1. 拡張子を`.gz` として、GZip形式で圧縮保存(ロードでは自動で解凍してくれる)
`np.loadtxt("ファイル名.txt")`
	1. ファイルから配列を復元する
## 内包表記
参考
	1. https://docs.python.org/ja/3/tutorial/datastructures.html#list-comprehensions
	2. https://docs.python.org/ja/3/tutorial/datastructures.html#nested-list-comprehensions
例
```
[x**2 for x in range(6)]
```
は以下と等しい
```
squares1 = []
for x in range(6):
	squares1.append(x**2)
```
コード例
a~zの文字列を割り当てたい時のリスト：`[chr(i + ord('a')) for i in range(26)]`
### 入れ子(ネスト)
例
多重リスト
```[[x*y for y in range(x+1)] for x in range(4)]```
要素数が掛け算
`[x*y for x in range(4) for y in range(x+1)]`
コード例
与えられた文字列の全てのから空でない部分文字列からなるリスト
```
def allsubstrings(s):
	return [s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]

allsubstrings('abc')
```
### 条件付内包表記
例
`length = [len(w) for w in words if w != None]`
その他の例
set型(`set([])`, `{}`)
	`length_set = {len(w) for w in words}`
辞書型(`{:}`)
	`length_dic = {w:len(w) for w in words}`
### ジェネレータ式
リスト内包表記の`[]`を`()`にした場合、イテレータが構築される
	1. 例：`it = (x * 3 for x in 'abc')`
	2. 引数にする場合は外側の`()`は省略でき、`list(x * 3 for x in 'abc')`や`tuple(x * 3 for x in 'abc')`でリストやタプルを生成できる
	3. リストやタプルに適用できる組み込み関数は、イテレータも渡せる：`sum(iter)`
## 6.2.高階関数
参考：https://docs.python.org/ja/3/howto/functional.html
関数を引数として受け取ったり、返値として返す関数のこと
1. 関数とはオブジェクトの一種
	1. 例
		1. ラムダ式：`<function __main__.<lambda>>`
		2. abs：　`<function abs>`
`max(list, key=abs)`のようにキーワード引数を与えられる
	1. 書く要素にkeyで指定された`abs`が適用されて、その結果でmaxであった元の要素を返す
	2. そのほかにも、`sorted(list, key=abs)`とか
### ラムダ式(無名関数)
1. `key=lambda~` のように使用できる
辞書の呼び出しのラムダ式：`lambda k: d[k]`
### イテラブルについて
イテラブルは、iterが適用できるもののこと
また、さっきまで、リストやタプルに適用できた関数は、一般にイテラブルを引数にとれる
1. 例：ファイルオブジェクト(=イテラブル)
```
with open('jugemu.txt', 'r', encoding='utf-8') as f:
	print(max(f, key=len))
```
2. 例：辞書(=イテラブル)
```
# キーの最大値9を返す
max({3:10, 5:2, 9:1})
```
### map
mapは高階関数
イテラブルなオブジェクトに関数を適用したイテレータを返す
`map(fuction, iterable)`
		1. `map(abs, [3,-8,1,0,7,-5])`とするとマップオブジェクト`<map at 0x7f39c9aa2590>`が返る(イテレータ)
		2. `for x in map_object:`のようにして読み出し 
		3. `list(map_object)` でイテレータからリストに変換できる
		4. `next(map_object)`も可能
		5. map_objectはイテレータだから、mapを再度適用すること可能
			1. `map(lambda x: x+1, map(abs, list))`
		6. イテラブルをとれる関数なら、わざわざリストに戻さなくてもよい
			1. `sum(map_object)`
### filter
関数filterも、イテラブルをもらって、イテレータを返す
真理値を返す関数bool_funcを第一引数に指定
`filter(bool_func, イテラブル)`
例
```
lam = lambda x: True if x>0 else False
list(filter(lam, [3,-8,1,0,7,-5]))
```
条件内包に近い(以下と等しい結果)
```
def pos(x):
	if x>0:
		return True
	else:
		return False

[x for x in [3,-8,1,0,7,-5] if pos(x)]
```
**mapに併用することも可能**
1. ファイル名 `file` と整数 `n` を受け取って、そのファイルをオープンし、改行文字も含めて、長さが `n` より長い行の数を返す関数
```
def number_of_long_lines(file, n):
	with open(file, 'r', encoding='utf-8') as f:
		return sum(map(lambda x: 1, filter(lambda x: len(x)>n, f)))
```
## 6.3.クラス
参考
	1. https://docs.python.org/ja/3/tutorial/classes.html
	2. https://docs.python.org/ja/3/reference/datamodel.html
クラス定義されたオブジェクトは、オブジェクト指向プログラミングにおける典型的なオブジェクトです。
クラスとはオブジェクトの種類の一つであり、クラスに属するオブジェクトの型はそのクラスになる。
クラス定義の形
	1. self：メソッドが呼び出されたオブジェクト自身が渡される(classのインスタンスのこと?)
```
class クラス名:
	def メソッド名(self, 引数, ...):
		実行文
	def メソッド名(self, 引数, ...):
		実行文
	...
```
例：Helloを必ず出力するクラス
```
class HelloForEver:
	def readline(self):
		return 'Hello.\n'
```
### クラスの生成
コンストラクタ`クラス名(式, ...)`によってオブジェクトを生成する
オブジェクト生成
	1. `f = HelloForEver()`
	2. クラスのインスタンスが生成される
型をチェック
	1.  `type(f) # __main__.HelloForEver`
	2. `__main__`はノートブックの式が評価されているモジュールを指す
呼び出し
	1. `f.readline()`
	2. オブジェクト`f` が`self`引数として渡されて、関数実行
### 初期化と属性
初期化
	1. メソッドは、`__init__`という名を持ち、オブジェクト生成時に自動的に呼び出される
	2. `__init__`の引数は、インスタンス生成の引数の式
属性
	1. クラスを型とするオブジェクトは属性(クラス内の変数)を保持できる
	2. `self.属性名`で参照、代入可能
	3. メソッドも属性の一種
### 継承
既存のクラス(親クラス)をもとにして、変更部分だけを与えることで、新たなクラス(子クラス)を定義する機能
例：
	1. `__init__`とreadlineを新たに定義、更新している
	2. `super()`は、子クラスのオブジェクトに対して、親クラスのメソッドを呼び出すための構文
```
class HelloFile(HelloForEver):
	def __init__(self, n):
		self.n = n
	def readline(self):
		if self.n == 0:
			return ''
		self.n = self.n - 1
		return super().readline()
```
### 特殊メソッド
前後に`__`が付くメソッドのことで、多数ある。
`__iter__`：オブジェクトに関数`iter`が適用されたときに呼び出される。
	1. `iter(f)`で、`f.__iter__()`として呼び出され、返値が`iter(f)`となる。
`__next__`：オブジェクトに関数`next`が適用されたときに呼び出される
	1. `__next__`メソッドの値が`next`の返値となる
1. `raise StopIteration`はfor文が捕まえて繰り返しを止める働きがある
	1. `raise`によって強制的にエラーを発生させる
	2. for文が`raise`によるエラーを捕まえて、そこでfor文を打ち切る
```
class HelloFileIterator(HelloFile):
	def __iter__(self):
		return self
	def __next__(self):
		line = self.readline()
		if line == '':
			raise StopIteration
		return line

f = HelloFileIterator(3)

print(f is iter(f)) # True

for line in f: # 内部でnextが発動して、変数lineへnextの返値が入る
	print(line)
# Hello.
# Hello.
# Hello. 三回でraiseのエラーによって打ち切り
```
### 継承による振る舞いの改変
- 親クラスを継承するにかかわらず、`self`は子クラスの中のオブジェクト(メソッド等)を先に探索する
	- 親クラスのメソッドが呼ばれ、その中で`self`  が出てきたら、子クラスのオブジェクトを先に探索してしまう
	- つまり、子クラスで、親クラスのメソッド名を使用して定義したら、間接的に改変することができる(子クラスの定義を優先する)
	- 親クラス、子クラス両方で同名のメソッド定義をするなら、親クラス呼び出しの際に`super().メソッド名`で指定する
`list(イテレータf)`すると`[x for x in f]`にみたいに、`next`されてる判定になるかな
### with文によるイテレータ呼び出し可能に
特殊メソッド：`__enter__`と`__exit__`を定義することで、with文も可能に
```
class HelloFileIterator(HelloFile):
	def __enter__(self):
		return self
	def __exit__(self,exception_type,exception_value,traceback):
		pass
	def __next__(self):
		line = self.readline()
		if line == '':
			raise StopIteration
		return line
	def __iter__(self):
		return self

with HelloFileIterator(3) as f:
	for line in f:
		print(line)
# Hello.
# Hello.
# Hello.
```
## 7.1.pandasライブラリ
参考
	1. http://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
	2. http://pandas.pydata.org/pandas-docs/stable/
リスト、配列や辞書型から作成でき、インデックスで管理される
### 生成
1. リスト、配列、辞書から生成できる
	1. `pd.Series(入力)`, `pd.DataFrame(入力, index=, columns=)`
2. 参考：https://note.nkmk.me/python-pandas-dataframe-values-columns-index/
CSVから生成
1. 参考：https://note.nkmk.me/python-pandas-read-csv-tsv/
2. `pd.read_csv(url)`, `pd.read_txt(url)`
### データ参照の仕方
1. 行のスライス：`df[3:]`
2. 列名の添え字指定：`df["列名"]`, `df.列名`
3. ilocとlocによる任意の行と列を指定：`df.iloc[行index, 列index]`, `df.loc[行名or index, 列名 or index]`
	1. スライスやリストでの指定も可能
		1. `iris_d.loc[1:5, ['sepal_length','species']]`
### 条件取り出し mask
1. `df.mask`というものがあるらしい
2. 真理配列によるインデックスアクセス( `&`, `|`, `~`)
	1. `iris_d[(iris_d['sepal_length'] > 7.0) & (iris_d['sepal_width'] < 3.0)]`
### 列の追加と削除
1. 追加
	1. 代入：`df["列名"]=~`
	2. `df1 =　df.assign(my_columns=リスト等)`
2. 削除
	1. `del df["列名]"`
	2. `df.drop([列名, 列名], axis=1)`
	3. 残しておく列名で新たにdfを作成：`df1 = df[ほかの列名]`
### 行の追加と削除
1. 追加：`df.append(row, ignore_index=True)`
	1. `ignore_index=True`で追加した行に新たなインデックス番号が振られる
2. 削除：`df.drop(行index or 行label)`
### 統計量計算など
参考：https://pandas.pydata.org/pandas-docs/stable/reference/frame.html#computations-descriptive-stats
1. `describe()`
2. `info()`
3. `pandas.profiling`
欠損値：https://pandas.pydata.org/pandas-docs/stable/missing_data.html#missing-data
時系列データの処理：https://pandas.pydata.org/pandas-docs/stable/timeseries.html
### 連結と結合
1. concat：連結, `pd.concat([df1, df2], axis=)`
2. merge：結合, `pd.merge(df1, df2, on=key_columns)`
### グループ化
1. `df.groupby([列名]).mean()`
2. aggsとかあった気がする
## 7.2.scikit-learnライブラリ
参考
- https://scikit-learn.org/stable/tutorial/index.html
- https://scikit-learn.org/stable/getting_started.html
機械学習の各手法の詳細については以下を参考にしてください
- https://elf-c.he.u-tokyo.ac.jp/courses/364 （線形回帰）
- https://elf-c.he.u-tokyo.ac.jp/courses/365 （ロジスティック回帰)
- https://elf-c.he.u-tokyo.ac.jp/courses/360 （クラスタリング）
- https://elf-c.he.u-tokyo.ac.jp/courses/363 （次元削減（主成分分析））
教師あり
	1. 観測されたデータの特徴量に対して、そのデータに関するラベルが存在する
	2. ラベルを教師として、データからそのラベルを予測するモデルを学習すること
	3. ラベルが連続値なら回帰、ラベルが離散値なら分類
教師なし学習
	1. ラベルが存在せず、観測されたデータの特徴量のみからそのデータセットの構造やパターンをよく表すようなモデルを学習することを教師なし学習と呼ぶ
	2. クラスタリング(データをクラスタへ)や次元削減(簡潔に低い次元で表現)は教師なし学習
irisデータの入力
```
from sklearn.datasets import load_iris
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```
### モデル学習の基礎
scikit-learnでは、以下の手順でデータからモデルの学習を行います。
1. 使用するモデルのクラスの選択
2. モデルのハイパーパラメータの選択とインスタンス化
3. データの準備
	 - 教師あり学習では、特徴量データとラベルデータを準備
	 - 教師あり学習では、特徴量・ラベルデータをモデル学習用の訓練データとモデル評価用のテストデータに分ける
	 - 教師なし学習では、特徴量データを準備
4. モデルをデータに適合（`fit()` メソッド）
5. モデルの評価
	 - 教師あり学習では、`predict()` メソッドを用いてテストデータの特徴量データからラベルデータを予測しその精度の評価を行う
	 - 教師なし学習では、`transform()` または `predict()` メソッドを用いて特徴量データのクラスタリングや次元削減などを行う
### ロジスティック回帰(LigisticRegression)
[LogisticRegressionクラス](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
```
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
  
iris = load_iris()
X_iris = iris.data # 特徴量データ
y_iris = iris.target # ラベルデータ

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X_iris, y_iris, test_size=0.3, random_state=1, stratify=y_iris)

# ロジスティック回帰モデル：solver引数には最適化手法、multi_classには多クラス分類の方法を指定
# ここではそれぞれのデフォルト値、lbfgsとautoを指定
model=LogisticRegression(solver='lbfgs',  multi_class='auto')

model.fit(X_train, y_train) # モデルを訓練データに適合
y_predicted=model.predict(X_test) # テストデータでラベルを予測
accuracy_score(y_test, y_predicted) # 予測精度（accuracy）の評価
# 0.9777777777777777
```
1. 決定境界の可視化(分類問題)
```
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

w2 = model.coef_[0,1]
w1 = model.coef_[0,0]
w0 = model.intercept_[0]

  
line=np.linspace(3,7)
plt.plot(line, -(w1*line+w0)/w2)
y_c = (y_iris=='versicolor').astype(int)
plt.scatter(iris2['petal_length'],iris2['petal_width'],c=y_c);
```
2. 回帰の評価方法
	1. 分類では、予測精度accuracyだったが
	2. 回帰では、平均2乗誤差：`mean_squared_error(y_test,y_predicted)`
### クラスタリング(教師なし学習の1つ)
Kmeansクラス：https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
元のノートブックの画像見た方が早い
https://colab.research.google.com/github/utokyo-ipp/utokyo-ipp.github.io/blob/master/colab/7/7-2.ipynb#scrollTo=N2zKpcXeFt6X
```
from sklearn.cluster import KMeans

iris = pd.read_csv('iris.csv')
X_iris=iris[['petal_length', 'petal_width']].values

model = KMeans(n_clusters=3) # k-meansモデル
model.fit(X_iris) # モデルをデータに適合
y_km=model.predict(X_iris) # クラスタを予測

iris['cluster']=y_km
iris.plot.scatter(x='petal_length', y='petal_width', c='cluster', colormap='viridis');
```
### PCA(教師なし学習の1つ)
次元削減
https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
```
from sklearn.decomposition import PCA

iris = pd.read_csv('iris.csv')
X_iris=iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values

model = PCA(n_components=2) # PCAモデル
model.fit(X_iris) # モデルをデータに適合
X_2d=model.transform(X_iris) # 次元削減
```
可視化
```
import seaborn as sns

iris['pca1']=X_2d[:,0]
iris['pca2']=X_2d[:,1]
sns.lmplot(x='pca1',y='pca2',hue='species',data=iris,fit_reg=False);
```
## 8. jupyterノートブック知識(claboも)
参考：https://jupyter.readthedocs.io/en/latest/
* a: 上にセルを挿入 (above)
* b: 下にセルを挿入 (below)
* x: セルを削除（そのセルが削除されてしまいますので注意！）
* l: セルの行に番号を振るか振らないかをスイッチ
* s または Ctrl+s: ノートブックをセーブ (checkpoint)
* Enter: 編集モードに移行
* Shift+Enter: セルを実行して次のセルに
## 9.set(集合)
1. 定義方法
	1. `set1 = {1, 2, 3}`
	2. `set2 = set([1, 2, 3])`
2. 空set：`set()`
	1. `set3 = {}`としたら辞書になるので注意
3. 重複削除される
4. 文字列は分解されてsetになる
	1. `set("abahjgha")`
		1. `{a, b, g, j, h}`が返る
5. 辞書はキーだけのsetになる
	1. `set({'apple' : 3, 'pen' : 5}) # {'apple', 'pen'}`
### 組み込み関数
indexで指定して取り出しはできない：`set1[0]`はダメ
1. `len`
2. 多重代入：`x,y,z = set1`
3. 含有判定：`2 in set1`
### 集合演算
1. 和集合：`set1 | set2`
	1. `set1.union(set2)`
2. 積集合：`set1 & set2`
	1. `set1.intersection(set2)`
3. 差集合：`set1 - set2`
	1. `set1.difference(set2)`
4. 対象差(XOR)：`set1 ^ set2`
	1. `set1.symmetric_difference(set2)`
比較演算は包含関係を判定する
### メゾット
すべて破壊的
1. `set1.add(4)`：要素追加
2. `set1.remove(1)`：要素削除(ない場合はエラー)
3. `set1.discard(1)`：要素削除(なくてもエラーにならない)
4. `set1.clear()`：すべての要素を削除して、空setにする
5. `set1.pop()`：ランダムに取り出す(破壊的)
## 10.再帰関数
1. 関数の**再帰呼び出し**とは、定義しようとしている関数を、その定義の中で呼び出すこと
2. 再帰関数は、**分割統治**アルゴリズムの記述に適している
	1. 分割統治とは、問題を容易に解ける粒度まで分割し、合成することで全体を解く手法
3. テンプレ
```
def recursive_function(...):
	if 問題粒度の判定:
		再帰呼び出しを含まない基本処理
	else:        
		再帰呼び出しを含む処理（問題の分割や部分解の合成を行う）
```
4. 繰り返し処理のほうが効率的にできるが、複雑な処理には再帰定義が読みやすい(
	1. 包含や2回以上の再起になると繰り返し処理では対処できない)
5. 例：マージソート(分割と比較ソートを順に繰り返す)
```
# リストに対してマージソートを行い、比較回数 n を返す(破壊的)

def merge_sort_rec(data, l, r, work):
	```[l:r]までを再帰的にソートする```
	n = 0 # 比較数
	if r - l <= 1: # サイズ1なら何もしない
		return n
	m = l + (r - l) // 2
	n1 = merge_sort_rec(data, l, m, work)
	n2 = merge_sort_rec(data, m, r, work)
	i1 = l # 代入詞&比較詞
	i2 = m
	for i in range(l, r):
		from1 = False # workに代入する際のflag
		if i2 >= r:
			from1 = True
		elif i1 < m:
			n = n + 1 # 比較数+1
			if data[i1] <= data[i2]: # 2値の比較
				from1 = True	
		if from1:
			work[i] = data[i1]
			i1 = i1 + 1
		else:
			work[i] = data[i2]
			i2 = i2 + 1
		print(work)
	for i in range(l, r): # copyでいい
		data[i] = work[i]
	return n1 + n2 + n # 比較数を返す
  
def merge_sort(data):
	return merge_sort_rec(data, 0, len(data), [0]*len(data))
	
###########
import random
a = [random.randint(1,100) for i in range(10)]
merge_sort(a)
print(a)
```


## 11.matplotlib基本
参考：https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

1. ノートブック上で表示
	1. `%matplotlib inline`を一回だけ実行
	2. `%`で始まる分をマジックコマンドという
2. `import matplotlib.pyplot as plt`

### 基本
点描画：`plt.plot(リストx, リストy)`
	1. 指定できるもの
		1. `linestyle='--', ':'`：線のスタイル
		2. `color='blue'`：色
		3. `marker='o', '*'`：マーカの形
		4. `label='Hello'`：plt.legend()が次に必要

その他
```Python
plt.title('My First Graph') # グラフのタイトル
plt.xlabel('x') #x軸のラベル
plt.ylabel('y') #y軸のラベル
plt.grid(True); #グリッドの表示
```

散布図：`plt.scatter(リストx, リストy)`
	1. 指定できるもの
		1. `s=100`：サイズ
		2. `alpha=0.5`：透明度
		3. `color='blue'`：色
		4. `marker=*`：マーカーの形

棒グラフ：`plt.bar(リストx, リストy)`
	1. `plt.bar(xs, ys, tick_label=labels)`：tick_labelを使うらしい

ヒストグラム：`plt.hist(リストd, bins=n)`

ヒートマップ
imshowで可視化
colorbar()で値と色の濃淡を対応
```Python
im=plt.imshow(ary2)
plt.colorbar(im);
```

保存：`savefig('~.png')`


## 12.CSV
参考：https://docs.python.org/ja/3/library/csv.html

### 読み込み
csvリーダー
```
import csv
f = open('small.csv', 'r')
dataReader = csv.reader(f) # 行列
f.close()
```
イテレータであるため、`next`やfor文で呼び出せる
`next(dataReader)`
```
for row in dataReader:
	print(row)
```
文字化け防止：`encoding='utf-8'
with文
```
with open('small.csv', 'r') as f:
	dataReader = csv.reader(f)
	for row in dataReader: # 1行ずつ読み込み
		print(row)
```
### 書き込み
csvライター
```
import csv
f = open('out.csv', 'w', encoding='utf-8', newline='')
dataWriter = csv.writer(f)
dataWriter.writerow([21,22,23])
f.close() # with文でOK!
```
書き込みする際は
`encoding='utf-8', newline=''`で文字化けを防止する必要がある
1. `dir(~)`で使用できるattrが見れる
	1. `dataWriter.writerow([21,22,23])`とかが効率的に利用できる
線形回帰ぽい図は
`fitp = numpy.poly1d(numpy.polyfit(x1, y1 1))` # 線形回帰fit
`plt.plot(x1, y2, '.', x2, fitp(x2), '-')`
## 13.Bokehによるグラフ描画(使いづらい)
参考：https://bokeh.pydata.org/
引数詳細：https://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure.Figure.line
データを可視化するためのライブラリ
グラフ描画：`import bokeh.plotting
図形生成：`bokeh.plotting.figure()`
図形表示：`bokeh.plotting.show()`
出力先をノートブック上に設定する：`bokeh.plotting.output_notebook()`
まず
```
from bokeh.plotting import figure, output_notebook, show
output_notebook()
```
Figureクラスのlineメソッドを使用
データ店を増やせば、曲線も可能：`x, np.cos(x)`とか
```
d = [0, 1, 4, 9, 16]
p = figure()
p.line(x=range(len(d)), y=d) # 第1引数がx軸、第2引数がy軸
show(p)
```
複数データまとめて表示
線の色、種類、凡例など指定可能
```
p.line(x, x, line_color='blue', legend_label='linear!', line_dash='dashed')
p.line(x, data, line_color='green', legend_label='quad!!', line_dash='dotted')
```
`figure()`関数の引数
軸ラベル、タイトル
```
p = figure(x_axis_label='x', y_axis_label='y', title='Hello')
```
プロット点
グラフに重ねる場合は、追加するように書く
```
p.circle(x, x, color='blue', line_width=5)
p.cross(x, data, color='green', size=16)
```
パレット
参考：https://bokeh.pydata.org/en/latest/docs/reference/palettes.html
d3のcategory10の2色パレット
```
from bokeh.palettes import d3
c = d3['Category10'][3]
...
p.cross(x, data, color=c[1], size=16)
```
散布図
```
p = figure()
p.scatter(x, y, marker='circle', size=16, alpha=0.5)
show(p)

# これでも可
p.circle(x, y, size=16, alpha=0.5)
```
棒グラフ
```
p = figure()
p.vbar(x, 0.5, y) # 第2引数は幅
show(p)
```
ヒスとブラム
`p.quad()`を用いる
np.histgramでbin_edges出して、leftとrightは1つずらした配列を入力
棒ぬり色： `fill_color='red'`
棒ふち色：`line_color='white'` 
例：正規分布
```
# 正規分布に基づく1000個の数値の要素からなる配列 
d = np.random.randn(1000)
# numpy.histogramで20のビンに分割
hist, bin_edges = np.histogram(d, 20)
p = figure()
p.quad(top=hist, bottom=0, left=bin_edges[:-1], right=bin_edges[1:], line_color='white', alpha=0.5)
show(p)
```
ヒートマップ：難しいのでいらないかも
x, y ,Tの三つの値が必要なので、`bokeh.models.ColumnDataSource`
Tに応じた階調のある色選択：`bokeh.models.LinearColorMapper`がたの`mapper`
表データの属性を参照して描画：`p.rect()`
```
from bokeh.models import LinearColorMapper, BasicTicker, PrintfTickFormatter, ColorBar, ColumnDataSource
from bokeh.transform import transform

# 10行10列のランダム要素からなる行列
n = 10
data = np.random.rand(n*n)
src = ColumnDataSource({'x': [yx % n for yx in range(n*n)], 'y': [yx // n for yx in range(n*n)], 'T' : data})

colors = ['#75968f', '#a5bab7', '#c9d9d3', '#e2e2e2', '#dfccce', '#ddb7b1', '#cc7878', '#933b41', '#550b1d']
mapper = LinearColorMapper(palette=colors, low=data.min(), high=data.max())
p = figure()
p.rect('x', 'y', 1, 1, source=src, line_color=None, fill_color=transform('T', mapper))
color_bar = ColorBar(color_mapper=mapper, location=(0, 0),
				ticker=BasicTicker(desired_num_ticks=len(colors)),
				formatter=PrintfTickFormatter(format='%2.1f'))
p.add_layout(color_bar, 'right')
show(p)

```
### グラフのファイル出力
画像保存ボタンを押すとPNG形式で保存される
`bokeh.plotting.output_file()`で、グラフ単独のHTMLファイルを保存できる
ただし、既に `output_notebook()` を読んでいる場合、**`bokeh.plotting.reset_output()`** で状態をリセットする必要がある
```
from bokeh.plotting import save, output_file, reset_output
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
p = figure(title='sin Curves', x_axis_label='x', y_axis_label='y')
p.line(x, np.sin(x))

reset_output() # output_notebook()の効果を消す
output_file('sin.html') # 出力先の設定
save(p) # グラフを保存するだけ
show(p) # 保存した上でブラウザを開く
```
`output_notebook()` を呼んだ状態と `output_file()` を呼んだ状態が重なると、`show()` でエラーが起きます
## 14.Pythonスクリプトとコマンドライン実行
参考：
	1. https://docs.python.org/ja/3/tutorial/interpreter.html
	2. https://docs.python.org/ja/3/tutorial/modules.html
	3. https://docs.python.org/ja/3/tutorial/appendix.html
	4. https://docs.python.org/ja/3/library/sys.html
	5. https://docs.python.org/ja/3/reference/import.html
- モジュールファイル(=`.py`)は、それ単独で直接実行可能な自己完結したプログラム
- 直接実行されるコードファイルを特に**Pythonスクリプト**と呼ぶ
- モジュール(関数)かスクリプト(pyファイル)かを区別しないときには、Pythonソースファイルや `.py` ファイル等と呼ぶ
### コマンドライン引数
実行スクリプト名の後に、文字列を追加することで、実行スクリプトへ引数(=コマンドライン引数)を与えることができる
$ python3 sample.py v1 v2 v3..
### モジュールのコマンドライン実行
Pythonソースファイルの実行のされ方
	1. モジュールとしてインポート= ライブラリ
	2. スクリプトとしてコマンドライン実行 = アプリケーション
この二つの違いは、`__name__`を参照することで区別可能
	1. モジュール`mod.py`がコマンドライン実行されたときに、`__name__`の値は`__main__`になる.
	2. 一方、`import mod` されたとき、`__name__`の値は`mod`になる
これを利用することで、インポートとコマンドライン実行された場合で、モジュールのふるまいを変えることができる
例：
factorial.py:
```Python
import sys
# 階乗n!を返す
def fact(n):
	prod = 1
	for i in range(1, n + 1):
		prod *= i
	return prod
if __name__ == '__main__':
	n = int(sys.argv[1]) # 整数nが1番目のコマンドライン引数で与えられる
	print(fact(n))       # n!を印字 
```
1. `import factorial`で`facotorial.fact()`が利用可能になる
2. `python factorial.py 6`とコマンド実行すると、`720`が返る
とても簡単にライブラリやスクリプトとして利用できる。

`if __name__ == '__main__'`の分岐の中は、自己完結したスクリプトが望ましい
	1. 条件分岐がなかったら、モジュールがインポート先の変数などを参照してしまったり、printなど影響を受けてしまう恐れがある
	2. コマンドライン実行で完結している必要がある


テストコードを記述
1つのPythonソースファイルの中で、ライブラリ実装とテストをひとまとめにできて、保守しやすくなる
```Python
import sys
# 階乗n!を返す
def fact(n):
	prod = 1
	for i in range(1, n + 1):
		prod *= i 
	return prod
if __name__ == '__main__':  
	print('test n = 6:', fact(6) == 720)  
	print('test n = 0:', fact(0) == 1) 
```


### ソースファイル先頭の宣言
文字コード宣言
1. Pythonソースコードでは、UTF-8での記述が推奨
	1. Windows環境では、時々shift_jisが使用されることがある
		1. `# -*- coding: shift_jis -*-`が宣言される必要がある
		2. こうしないとPythonインタプリタがエラーを起こす
	2. UTF-8記述の場合は、文字コードを宣言しないことが推奨

shebang
Unix環境では、スクリプトファイルの先頭行に、そのスクリプトを実行するコマンドを指定できるようになっている、その先頭行を**shebang**という。

Unix環境のPythonスクリプトに用いられる標準的なshebang
`# !/usr/bin/env python3`
	1. `#!`の続く部分は、絶対パスで指定
	2. `env`コマンドは、その引数(ここでは`python3`)の名前のコマンドを環境から探して実行する
	3. Pythonインタプリタがインストールされている場所を気にせずに、Unix環境におけるPython3系列の標準コマンド名である `python3` を使って実行できる

shebangと文字コード宣言の両方を含む
```
# !/usr/bin/env python3
# -*- coding: shift_jis -*-
```


`sys.argv`はコマンドライン引数を保持するが、`sys.argv[0]`は`~.py`が入っているので、引数は`[1]`から保存されている

(arrayは`ary`と訳すとかっこいい)



## 15.正規表現(regular expression)
参考：https://docs.python.jp/3/library/re.html
ノートブック：https://colab.research.google.com/github/utokyo-ipp/utokyo-ipp.github.io/blob/master/colab/appendix/5-re.ipynb#scrollTo=OSZH5wQgmGVI

正規表現：文字のパターンを表す式
	1. 正規表現にマッチする

```Python
import re
```

### 基本
**match**
正規表現が文字列の先頭部分にマッチするかを区別, 判別に使用できる
	1. 大文字・小文字区別する
		1. `re.match(~, ~, re.IGNORECASE)`で区別しないマッチングを行う
		2. `re.I`でも可
```
re.match(正規表現A, 文字列B)
```
- 判定
```Python
# マッチする
re.match('abc', 'abcde') # <re.Match object; span=(0, 3), match='abc'>
# マッチしない
re.match('abc', 'ababc') # None
```
1. マッチ成立で、マッチオブジェクトを返す
2. マッチ不成立で、Noneを返す
このことは、bool(None)=Falseより、`if re.match(正規表現, 文字列):`として判別に使用できる


マッチオブジェクトについて
`<_sre.SRE_Match object; span=(0, 3), match='abc'>`
match=マッチした文字列
span=マッチした文字列と適合するインデックス


**search**
指定した正規表現が文字列にマッチするかどうか調べる(文字列内をすべて探査)
	1. re.matchは先頭だけ
	2. re.IGNORECASEを第3引数に指定できる
	3. if文利用が可能
		1. あう部分文字列があったら、`<re.Match object; span=(3, 6), match='def'>`を返す
		2. なかったら、`None`を返す
	4. matchみたいに先頭や末尾とのマッチを調べたい
		1. キャレット`^`で先頭マッチング：`re.search('^abc', 文字列)`
		2. ドル記号`$`で末尾マッチング：`re.search('abc$', 文字列)`
```Python
re.search(正規表現A, 文字列B)
```


### 正規表現記法
- 特に正規表現の欄の拡張に関して
- 正規表現は、ただの文字列`abc`のようなものも正規表現の1つとしてマッチングとして利用できる

 `正規表現A|正規表現B`：和もしくは選択
	 1. どちらかがマッチングしていたらマッチオブジェクトを返す
	 2. 文字列の先頭から先に出てきた正規表現のマッチオブジェクトを返す
	 3. `A|B|C`のような複数の**和**も可能

 1. 正規表現`abc`は厳密には3つの正規表現の連結であり、このように正規表現をつなげて新しい正規表現を作ることを**連接**という。
 2. `A*`は正規表現Aを0回以上繰り返した文字列にマッチする(**閉包**)
	 1. 閉包だけのマッチングは、先頭の`span=(0,0), match=''`の空文字列にマッチングしてしまう
	 2. `abb*`は`ab`+`b*`

演算(連接, 閉包, 和)の優先度
1. 和<連接<閉包：和<積<冪
	1. `ab|ac`のように、優先度は連接>和
	2. `a(b|a)c`は、`abc|aac`となる

正規表現は、変数に代入可能
```Python
reg1 = 'a(bc|b)*'
re.match(reg1, 'abcde')
# <re.Match object; span=(0, 3), match='abc'>
```


### 文字クラス
角かっこがついた正規表現(**文字列なので''で囲むこと**)のこと
`[abc]`は、`a|b|c`と同じ意味の正規表現
	1. 使用例：`6[789]*`
	2. カッコ内の要素のどれかなので、要素数は1になる
		1. `ab | cd`を一つの文字クラスでは表せない
	3. 注意点
		1. `[a|b]`や`[a*]`には、連接や閉包は適用されず、和の一部と考える
			1. `[a|b]`=`a|||b`
			2. `[a*]`=`a|*`
	4. 連続する和演算`-`
		1. すべてのアルファベットと数字：`[a-zA-Z0-9]`
		2. 1から7：`[1-7]`
	5. 否定クラス`^`
		1. `^`以降の文字以外のマッチング
			1. `[^abc]`は,a, b, c以外の文字とマッチング
			2. `[^1-7]`は、1~7以外の文字とマッチング
		2. ただし、キャレット`^`を戦闘以外でつけると文字クラスの要素の1つになる


### 正規表現の基本関数
1. `re.sub(正規表現R, 置換する文字列B, 元になる文字列A)
	1. RにマッチするA内の文字列すべてをBへ置換(非破壊的)
	2. 例
		1. 句読点削除：`re.sub('[.,:;!?]', '',文字列)`
		2. HTMLやXMLのタグ消し：`re.sub(r'<[^>]*>', '', 文字列)`
		3. 空白やタブや改行の繰り返しを空白へ置換：`re.sub(r'[ \t\n][ \t\n]*', ' ', 文字列)`
`
2 .`re.split(正規表現R, 元になる文字列A)
	1. Rにマッチする正規表現の個所でAを文字列のリストへ分割
	2. 英文字以外の文字の1回以上の繰り返し：`[^a-zA-Z][^a-zA-Z]*`


### 先頭にrをつける理由
エスケープすべき文字がエスケープシーケンスになってくれる
本来は使わなくてもOK!
```Python
r'[ \t\n]+'
# [ \\t\\n]+
```

`\`自体を含めたい場合
`\\`を含める、もしくは、`r'\'`でOK!
	1. `\\`はバックスラッシュを表すエスケープシーケンス
```
r'\\t t/'
# \\\\t t/
```

### 反復文字
`*`：0回以上
`+`：1回以上
`?`：高々1回(=0, 1)
`a{x,y}`：正規表現aをx回以上かつy以下繰り返す

### メタ文字
`.`：すべての文字とマッチ
`\t`：タブ
`\s`：空白文字(=スペース, タブ, 改行など)
`\S`：空白文字`\s`以外のすべての文字：`[^\s]`
`\w`：`[a-zA-Z0-9_]`と同じ：英数字と`_`
`\W`：`[a-zA-Z0-9_]`以外のすべての文字：`^[a-zA-Z0-9_]`のこと
`\d`：`[0-9]`：1桁の数字
	1. 電話番号　`re.search('\d*-\d*-\d*', '03-5454-6828')`
`\D`：`\d`以外のすべての文字：`[^0-9]`
