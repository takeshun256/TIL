start：[[2023-07-27]] 04:47

- 必要なもの
  - chrome
  - vscode
- Emmet
  - コード補完
  - 前コーディング　必須技能
  - `index.html` で `!`押して Enter するとテンプレートが出てくる

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body></body>
</html>
```

- `index.html` をブラウザへドラッグアンドドロップで表示できる
- `<html lang="ja">`　でページの言語設定を決めてくれる
  - これが`en`とかだと chrome が認識して翻訳しますかとしてくれる。　だから自動翻訳してしまうぺーじがあるのね
- `indent`は見やすさのみに影響
- ブラウザで`index.html`を開いて ctrl+R で更新しながら作業するが良い
- javascript は環境構築不要でブラウザ上で動作する=> 重要
- `node.js` はサーバーサイドで動作する(バックエンド) => フロントエンドもバックエンドも流用できる
  - バックエンド側は将来どんどんコードを書かあくなる => UI/UX が重要
- js はエコシステム(他のツールやノウハウの広がり) が大きい
  - React Native: モバイルアプリ
    - ios swift, android kotlin
  - Electron: デスクトップアプリ PWA
  - Puppeteer: スクレイピング
  - TensorFlow.js: 機械学習
- 開発はじめ
  - emmet で html を書く `!`でテンプレートが出てくる
  - lang="ja"で言語設定 `en`だと翻訳が毎回出るため
- Emmet によって tag name を入力するだけで補完が表示されそこから選択することができる！
- tag を閉じられる => vscode 上で見やすい

【メモ】

### 拡張機能

- `HTML Preview`

  - style.css の内容が反映されないことがある
    - ＝＞一度 `style`タグで表示変更させたりして反映させる, もしくは保存連打

-

### css

- stlye タグ内に指定する
- タグ {～設定}
- color
- font-size
- #id で特定の id のみ指定可能
- `*` で全てのタグを指定
- `style` タグの内容を`style.css` に記載で OK、その後 style タグを削除後...
  - `link` と入力して補完で `link:css` をクリックでリンクを作る
    - `<link rel="stylesheet" href="style.css">`
-

### html tag

- 仕様書 `html reference` で都度検索する => mdn web docs
  - [MDN Doc](https://developer.mozilla.org/ja/docs/Web/HTML/Element)
  - vscode の reference が mdn web docs のため
- `div`: Just a container
  - 開発時に使えば使うほど便利！
  - html を見るときは div に注目すると良いかも
- `id="foo"` on a tag: Assign a name within the same tag, useful for separating CSS within the same tag
- `head`: meta data
  - `meta`: meta data
- `body`: main content, 一つのページに一つだけ, 表示される内容
- `head` メインルート 全てのタグは`head`の中に入る
- テキストコンテンツ
  - `h1` ~ `h6` : ヘッダー
  - `div` : コンテナ, 囲むだけ - chrome のクローラーは`div`タグは中身がわからない => `header`, `main`, `footer` などのタグを使う(SEO 対策)
  - `p` : パラグラフ
  - `a` : アンカー, リンク
    - `href` : リンク先, `#` でページ内リンクなので仮設定で使ったりする
    - `target="_blank"` : 新しいタブで開く
- `hr` : 水平線, ブラウザによって表示の差異がある例
- `input`: 入力, ブラウザによって実装されていなかったりする
  - `<input type="date" name="" id="">` : 日付入力
  - [互換性](https://developer.mozilla.org/ja/docs/Web/HTML/Element/input/date#%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%83%BC%E3%81%AE%E4%BA%92%E6%8F%9B%E6%80%A7) を見たり、[caniuse.com](https://caniuse.com/?search=input%20date)で検索する
- `img` : 画像
  - `src` : 画像のパス
  - `alt` : 画像が表示されないときの代替テキスト
  - `width` : 幅
  - `height` : 高さ
- `ul` : リスト,
  - `li` : リストアイテム
  - `ul>li*5` で ul タグの中に li タグを 5 つ作成 => よく利用する
  - `ol` : 順序付きリスト なんか表示されない
- `nav` : ナビゲーション, 文書内のリンクをまとめる, 目次など
- blog の場合は
  - header にはタイトル, nav にはリンク, main には本文, footer には著作権など
  - article には記事の内容, section にはセクション
  - article 内に header を入れたりする => 記事のヘッダの意味合い
    - h1 をもう一度入れても良い
    - article の header 内例
    - `h1` : 記事のタイトル
    - `p` : 記事の概要, 著者, 日時, `投稿日時` など
    - `time` : 記事の日時
  - article の文章は段落`p`タグで書かれたりする
    - 適当な文章: `lorem` で補完できる, ダミーテキスト
  - `section` : セクション, 記事の中でセクションを分ける
  - `footer` : 著作権など 特に `small` タグで著作権表示が推奨
- `aside` : サイドバー, 本文とは関係ない情報

- `time` : 時間, `datetime` で日時を指定
  - `<time datetime="2024-07-28">twenty eight July</time>`: twenty eight July を表示

#### 属性

- [mdn reference](https://developer.mozilla.org/ja/docs/Web/HTML/Attributes)
- emmet で属性別で入力できる
- href: リンク先 a タグで特に利用
- 種類
  - global attributes: 全てのタグでどこででも利用可能
    - class: 要素のクラスを指定, css や js で呼び出し安くする, body 内で有用
  - event handler attributes: イベントハンドラー,
    - href: リンク先 a タグなどの特定のタグで利用可能

### javascript

- `button` ボタンを作成する
  - `onclick="alert('nice click')" でボタン押したときに nice click というポップアップが出る
  - `<button id="btn" onclick="alert('nice click');alert('nice click')">Click me</button>`で二連続でポップアップできる
- `<script>` tag で js を実行できる
  - `alert('hello')` で開始時にポップアップが出る
- butten のクリックイベントをトリガーとする
  - `getElementById` で id の要素を取得して、`addEventListener` でクリックイベントを追加する

```html
<script>
  document.getElementById("btn").addEventListener("click", function () {
    alert("hello world");
  });
</script>
```

- `index.js` というファイルを作成して、`<script src="index.js"></script>` で読み込むことができる
  - この場合、`index.js` に記載された内容が実行される
  - `script` タグの内容を`index.js` に記載して、`script` タグを削除する

### vscode

ショートカット

- `emmet balance outward` : タグの内側をすべて選択
  - `ctrl+shift+a` で実行
- `emmet with abbreviation`: 選択した部分をタグで囲む
  - tag で囲みたい文字を選択して、`alt+w` で実行
- Emmet
  - `ul>li*5` で ul タグの中に li タグを 5 つ作成 => よく利用する！
  - タグ名を入力するだけで補完が表示される
  - `!` でテンプレートが出てくる
  -

## まとめ(類似点・相違点)

ドキュメントは[mdn web docs](https://developer.mozilla.org/ja/docs/Web/HTML/Element)で検索することが重要

タグ入力では Emmet を使うことで補完ができてすぐに入力できる

互換性は[caniuse.com](https://caniuse.com)で検索することが重要, 複数のブラウザでの動作保証や表示を確認することが重要

画像サイトは[unsplash](https://unsplash.com)が良い

- ランダム画像: `https://picsum.photos/800` で 800px のランダム画像が取得できる

html を見るときは div に注目すると良いかも

## 振り返り

こんな簡単にファイルを配置するだけで、html, css, js が動作するのかブラウザ上で

１画面での開発は画面を四等分にして, vscode browser youtube などを表示して作業すると良い
