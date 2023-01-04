使い方
1. .vscode/settings.json内に`"python.formatting.provider": "フォーマッター"` と設定できる
2. ファイルを保存したときにフォーマッターをインストールを進められるのでインストールする
3. フォーマッターは、問題suggestを出してくれる

フォーマッターの種類
1. yapf
	1. 参考(整形スタイルも指定できる)：https://wonderwall.hatenablog.com/entry/2017/09/03/224500
	3. `yapf -d main.py` でフォーマット前後の差分表示
	4. `yapf -i main.py` でフォーマット後で置換する
	5. `yapf --style-help` で整形スタイルを確認可能
	6. `pip install git+https://github.com/google/yapf` でインストール可能
	7. `yapf --version` や `yapf --help` を使用可能
2. autopep8
	1. 参考：https://zenn.dev/iamhacchin/articles/aac3ff2ca66959e56f34
	2. `pip3 install autopep8` と `pip3 install flake8` をしておく
	3. 基本はyapfと同じ：`-d` で差分表示, `-i` で置換
