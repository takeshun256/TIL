start：[[2023-07-31]] 01:02

## 経緯・背景・興味・目標

これまでは、markdawn image という拡張機能を使用して、画像添付を、コピペでできるようにしていたが、デフォルト設定になった。

[VS Code で拡張機能なしで Markdown に画像を貼り付けられるようになった](https://zenn.dev/roboin/articles/1fa72705ff2e03)

## 内容・手順

settings.json に、以下の設定をすれば良い

- [VSCode の markdown.copyFiles.destination が zenn CLI と相性悪くて画像アップできん！](https://zenn.dev/temasaguru/scraps/1c234724218d4e)
- [VSCode でクリップボードの画像をそのまま Markdown に貼り付ける - Qiita](https://qiita.com/ugai/items/d0d3b9fffab39dcd8424)

そして、settings.json のパス変数

- [VS Code の設定をキレイに変数置換【VS Code 使い方 ①】 - Qiita](https://qiita.com/ShortArrow/items/dc0c8cacd696154510f1)

最終的には、ワーキングディレクトリごとに、設定をするようにするのが良さそう

どうしても相対パスになり、settings.json のパスがうまくいかないので、md ファイルと同じフォルダ内の images フォルダ内に保存されるようにした。

- images フォルダがない場合は、作成される。
