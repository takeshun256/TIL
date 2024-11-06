start：[[2024-06-08]] 00:29

## 経緯・背景・興味・目標

obsidian で、ノート生成しつつ、vscode や cursor で編集をしたい
AI 補完を利用したいため

## 内容

Tempalter で js で code 実行をすることが考えられたが、js からだとシステムコマンドがうまく作動しない

### shellcommand プラグインの利用

そのため、 [Index - Shell commands documentation - Obsidian Publish](https://publish.obsidian.md/shellcommands/Index) を用いた。

1. obsidian shellcommnad プラグインを追加して有効か
2. 以下のコマンドを定義して、カレントノートブックを開く
   1. `code {{file_path:absolute}}`
3. hotkey に、 `alt+a` を設定
