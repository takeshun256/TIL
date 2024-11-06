start：[[2024-08-02]] 07:23

- 以下を設定することで vscode 上でコピペ―ストしたときに、/Extra にドキュメントベース名称ではいるようになる
  `obsidian/.vscode/settings.json`

```json
{
  "markdown.copyFiles.destination": {
    "**/*": "/Extra/${documentBaseName}.${fileName/^(.+)\\.([^.]+)/$2/}"
  }
}
```

![[Pasted image 20240802072615.png]]
![[Pasted image 20240802073453.png]]

## 参考

- 公式
  - [Visual Studio Code May 2023](<https://code.visualstudio.com/updates/v1_79#_copy-external-media-files-into-workspace-on-drop-or-paste-for-markdown:~:text=%22markdown.copyFiles.destination%22%3A%20%7B%0A%20%20%22/docs/**/*%22%3A%20%22images/%24%7BdocumentBaseName/(.).*/%241/%7D/%22%0A%7D>)
- 記事
  - [Visual Studio Code で Markdown に画像を貼り付けられる markdown.copyFiles.destination 設定メモ – 1ft-seabass.jp.MEMO](https://www.1ft-seabass.jp/memo/2024/01/29/vscode-current-markdown-copyfiles-destination-setting/)　コマンド説明
  -
