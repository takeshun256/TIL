start：[[2023-12-07]] 10:38

### install

ブラウザ上でログインして、ワークスペース全体のログを取得できる、 slackdump を使用する

- [Slack データをエクスポート #Slack - Qiita](https://qiita.com/nanbuwks/items/f400db5f5974c4958f55)：手順

1. リリースから mac 用を取得
   1. [Releases · rusq/slackdump](https://github.com/rusq/slackdump/releases)
2. 解凍する
3. export を指定して実行

```python
./slackdump -export yyyy.zip -export-type standard -download
```

1. ブラウザ上でメールでログイン
   1. Google ログインはできないかもしれない
2. ログイン後、ブラウザ上で続行をクリック
   1. -> ダウンロードがコマンドライン上で再開される

### usage

- 上記で任意のワークスペースにログインしてログを全て取得する
- 別のワークスペースへログインするには、キャッシュを削除する必要あり

```python
rm -rf ~/.cache/slackdump
```

### viewer

#### slack-export-viewer

- 手順
  - [2022 年 8 月版：slack のバックアップ方法｜荒川 豊 (Yutaka Arakawa)](https://note.com/wildriver/n/ne0f7969a9c3b)
- 使用するもの
  - [GitHub - hfaran/slack-export-viewer: A Slack Export archive viewer that allows you to easily view and share your Slack team's export](https://github.com/hfaran/slack-export-viewer)

```python
# 上記のslackdumpを以下のディレクトリへ回答している状態
cd /Users/takeshitashunji/Programming/Python/py_study/slackdump_macOS_arm64

# zipを指定
python -m venv .venv
source .venv/bin/activate
pip install slack-export-viewer
slack-export-viewer -z /path/to/export/zip
```

#### slack-log-viewer

- prebuilt のものをダウンロード

  - [Releases · thayakawa-gh/SlackLogViewer](https://github.com/thayakawa-gh/SlackLogViewer/releases)
  - [GitHub - thayakawa-gh/SlackLogViewer: A viewer for json files exported from Slack workspaces.](https://github.com/thayakawa-gh/SlackLogViewer)

- ダウンロード後、app を実行して、左上のメニューから zipfile を開く
  - 画像が表示されないので、slackdump を使用するときに以下の指定すると良いらしい
  - README 参考
    - [usage-export.rst](https://github.com/rusq/slackdump/blob/master/doc/usage-export.rst)

```python
-export-type mattermost ...
->
slackdump -export slack_2mattermost.zip -export-type mattermost -download
```

### エラー対処

- 以下実行時に文字コードのエラー？

```python
slack-export-viewer -z /path/to/export/zip
```

- encode で utf-8 を指定する必要がりそう

  - [python - UnicodeEncodeError: 'charmap' codec can't encode characters - Stack Overflow](https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters)
  - [Encoding issue · Issue #26 · hfaran/slack-export-viewer · GitHub](https://github.com/hfaran/slack-export-viewer/issues/26)
  - -> fork して編集する感じか？

- 上記の例外処理をする(パスの/の問題ぽい)
  - [Python で zip 展開（日本語ファイル名対応） #Python - Qiita](https://qiita.com/tohka383/items/b72970b295cbc4baf5ab)
  - [Python で UnicodeDecodeError が発生した時の対応 #Python - Qiita](https://qiita.com/ijufumi/items/3609a983cd0673383f69)
- => 解決
  - [BugFix: UnicodeEncodeError: 'charmap' codec can't encode characters · hfaran/slack-export-viewer@aae7120 · GitHub](https://github.com/hfaran/slack-export-viewer/commit/aae71207e1b4ce00bdbbb4d51fa51463cf8e679a)

```python
BugFix: UnicodeEncodeError: 'charmap' codec can't encode characters

エラー原因としては、日本語名のファイルをcp437でエンコードしようとしていたため。
変更として、cp437でエラーが出る場合は、utf8でエンコードする場合分けを追加。

memo
- ビルド手順
pip install wheel
python setup.py sdist bdist_wheel

- インストール手順
pip uninstall slack-export-viewer
pip install slack-export-viewer/dist/.....whl

- 実行
slack-export-viewer -z /path/to/*.zip
```

## 参考

- [2022 年 8 月版：slack のバックアップ方法｜荒川 豊 (Yutaka Arakawa)](https://note.com/wildriver/n/ne0f7969a9c3b)
- [Releases · thayakawa-gh/SlackLogViewer](https://github.com/thayakawa-gh/SlackLogViewer/releases)
