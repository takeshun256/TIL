start：[[2023-07-31]] 02:51

0. 設定の変更
   - 別にいらないかも?

```json
 "[markdown]": {
    "editor.wordWrap": "on",
    "editor.quickSuggestions": true,
    "editor.snippetSuggestions": "top"
 },
```

2. 設定/ユーザースニペットから行くか or `Ctrl + Shift + P`から `Preferences: Configure User Snippets`を選択して、markdown をクリック
3. json の snippet ファイルが出てくるので、そこにスニペットを記載して保存
   1. 生成としては chatgpt で簡単にできる
   2. [Create VSCode Snippet](https://chat.openai.com/share/de0658bc-7c9b-4e59-8077-029dca9ae274)
4. 使用方法としては、コマンドパレットから、insert snippet を選択
   1. tab 補完は、おそらく copilot と競合して出てこなかった

- 形式

```json
"スニペット名": {
  "prefix": "キーになる文字列",
  "body":[ "呼び出される文字列" ],
  "description": "このスニペットの説明文" }
```
