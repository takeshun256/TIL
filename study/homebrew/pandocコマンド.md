start：[[2023-11-29]] 08:15

## 経緯・背景・興味・目標

案件の資料を obsidian でまとめておこうと思い export する際に、docs2md が pandoc にあると知ったため。

変換は、Docs2Markdown 拡張機能があると知ったが、画像やプルダウンでエラーが出ているのが少し大変だったため、pandoc を使ってみることにした。

- [Google ドキュメントから効率的に Markdown 作成【Docs to Markdown】 #Markdown - Qiita](https://qiita.com/lilacs/items/450a4c14b978ddee4a88)
-

## 内容

- [Pandoc の比較的簡単なインストール方法 #Markdown - Qiita](https://qiita.com/sky_y/items/3c5c46ebd319490907e8)

### install

```python
brew install pandoc
pandoc -v

```

```python
pandoc 3.1.9
Features: +server +lua
Scripting engine: Lua 5.4
User data directory: /Users/takeshitashunji/.local/share/pandoc
Copyright (C) 2006-2023 John MacFarlane. Web: https://pandoc.org
This is free software; see the source for copying conditions. There is no
warranty, not even for merchantability or fitness for a particular purpose.
```

### Docs2md

- [pandoc で Word ファイル(.docx)を Markdown へ変換する | 晴耕雨読](https://tex2e.github.io/blog/windows/word-to-markdown)

```python
pandoc -s 入力.docx --wrap=none --extract-media=media -t gfm -o 出力.md
```
