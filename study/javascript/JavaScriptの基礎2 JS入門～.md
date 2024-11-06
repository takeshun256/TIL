start：[[2023-07-28]] 08:33

### JS の登場(どのような特徴か)

- クライアントサイドとサーバーサイド
- ページが見たい
  - DNS 解決/
  - ->req リクエスト
  - <-res レスポンス（例:index.html)
  - ブラウザ側でレンダリング => ユーザーはページを見れる
- 再レンダリングが毎回走る
  js がなくても動く、しかし js を使ってリッチにする

- 再レンダリングされないようにする = `Ajax`
  - 毎回 req/res のサーバー更新はしているが
  - Ajax を使ったアプリ例は地図アプリ

サーバーとの通信について

- 初回は req/res=index.html
- レンダリング時は、**JSON が res で帰ってきて**、ブラウザ上の JS で操作される
-

- レンダリング時に毎回更新されてしまうと、ヘッダーやふっだーとかも更新される
  - =>JS デメインの部分だけを更新することで、**体験が良くなる**
  - ページ遷移時に最小限のレンダリング
- # =>JS でよりリッチに作成可能だよ！

### JS の仕事

1. データのやり取り
2. DOM 操作

Twitter の HTML 構造
JS の枠割

- 無限スクロール
  - **WebAPI にデータを要求**req する
  - **JSON**ガ res で返ってくる
  - パースする
    - JSON2HTML 変換
  - **DOM 操作**
    - parse されたデータを HTML に落とし込む

JS の仕事

1. データのやり取り
   1. req/res
   2. クッキー
2. DOM 操作

### オブジェクト指向型

種類(class みたいな感じか)

- オブジェクト: データと機能をまとめたもの
- プロパティ: オブジェクト内のデータに相当
  - プロパティ内の object を入れ子にできる
- メソッド：オブジェクト内の機能に相当

オブジェクトの作り方

1. オブジェクトリテラルを宣言する方法
   1. `let`で宣言
   2. プロパティやメソッドを後修正可能

```js
let takeshun = {
	name: "takeshun"; <-プロパティ
	learnPro: function(){...} <-メソッド
}
takeshun.name = "takeshun256";
```

オブジェクト(json)

- `index.js`

```js
let student = {
	list: {
		takeshun: [
			{
			name: takeshun
			learnPro: func...
			}
		]
	}
}
```

アクセス方法

```js
1 どっとアクセス
student.takeshun.name;
student.takeshun.learnPro();

2. 角かっこを用いる
student["takehsun"]["name"];
student["learnPro"](); <- methodに角かっこでアクセスできる
```

Window と Document

- ブラウザ自体もオブジェクトで定義されている => そのオブジェクトのプロパティやメソッドにアクセスして捜査している
  - ex. `window.fetch();`
  - ex. `window.document.getElementById("foo");`
  - # **window は省略できる**
  - ex. `alert`コマンドとかも`window.alert()` でメソッドの一つを呼び出している

ブラウザのオブジェクト構造

- DOM(HTML)=Document へアクセス
- DOM 操作 = Document オブジェクトを操作する

```js
window = {
	console: {
		log: function(){
			...
		}
	},
	alert: function(){
		...
	},
	document: {
		getElementById: function(){
			...
		}
	}
}
```

### JS コーディング

- index.js はオブジェクトの JSON ぽく書かれる
- 折りたたんで、カーソルを合わせると内容と種類が確認できる

- list は同じ key の要素が入る
- 青箱: property, 白箱: method, abc はファイル内の適当な文字
- 補完からオブジェクトの中身を知れる
- 他の js から読み込む

  - `export default object-name`
  - `import object-name`

- F12-＞ Console ログで JS の操作や確認が出来る
- alert 呼び出し

- 既存のページ(ex.yahoo)から Elements 内の id から property=DOM 要素を取得できた

- Console から手動でブラウザをリロードしたりとかの操作ができる

- # => 普段のブラウザ操作は、window.document のプロパティやメソッドを操作している！

### JS 操作を学ぶ

- ツール: [JS BIN](https://jsbin.com/?html,output)

  - HTML とか CSS も利用できる

- コメントアウト
  - `//`でコメントアウト
  - `/* */`で複数行コメントアウト
  - 見やすい例

```js
/**
 * ここはコメント
 */
```

- `const`と`let`の違い
  - `const`は定数, 再代入も再定義も不可 - object の中身は変更可能
  - `let`は変数, 再代入可能, 再定義不可, const の方が良い
  - `var`は再代入も再定義も可能だが、厳密でないため使わない方が良い
- 定義: `let` や `const` をつけて宣言すること
- 代入: `=` で値を代入すること

```js
let foo = 100; //変数宣言
foo = 200; //再代入
```

- 変数利用でわかりやすく書く

```js
const foo = document.getElementById("foo");
const fooWidth = foo.offsetWidth;
const fooHeight = foo.offsetHeight;
const fooArea = fooWidth * fooHeight;
```

- 変数名ケース
  - キャメルケース: `camelCase`で通常書く
  - その他

```js
const fooWidth = 100; //キャメルケース
const foo_width = 100; //スネークケース
const FooWidth = 100; //パスカルケース
```

- セミコロンは省略可能だが、書いた方が良い

- # => 変数は const で宣言することが重要

### JS 関数

- ?メソッドと関数は同じ?

  - メソッドはオブジェクト内の関数

- メソッドの短縮記法

  - `function`を省略して書く
    - `alert: function(){}` => `alert(){}`
    - 使うかはチームの方針による
    - 短縮記法でないと、vscode 上だと method が property として扱われてしまう

- 関数名は動詞で始める & キャメルケース
  - `return` の最後にもセミコロンをつける

```js
fuction cut(food){
	return food.slice(0, -1);
}

const cutFood = cut("apple");
```

- 可能かどうか: `～able`をつける

```js
function isTweetable(text) {
  return text.length <= 140;
}
function alertTweetable(text) {
  if (isTweetable(text)) {
    alert("you can tweet!");
  }
}
```

- 関数式
  - 関数を変数に代入したもの
  - 無名関数: `function(){}`のように名前がない関数

```js
const isTweetable = function (text) {
  return text.length <= 140;
};
```

- 高階関数

  - 関数を引数に取る関数 <= コールバック関数が渡される
  - 関数を返す関数
  -

- コールバック関数
  - イベントが発生したら非同期で実行される関数 <= それを登録する `addEventListener`とかがある。
  - 関数の動作を監視するために使う
  - 関数が小さくなるので、再利用性が高まり、可読性や改変がしやすくなる(変更量が小さくなる)
  - => 高階関数と組み合わせて使うことが多い(高階関数はコールバック関数を引数に取れる)

```js
function peer(food) {
    if (/*手洗いを終えたら*/) {
        //皮をむく処理
    }
}
//=> 関数内の共通の条件文などを外に出せる
function washed(fn) {
    if (/*手洗いを終えたら*/) {
        fn();
    }
}
function peer(food) {
        //皮をむく処理
}
washed(peer);
```

- コールバック関数の実践例 1
  - Tweeter とかで確認ボタンを押したときに、確認ボタンを押したらツイートするとか
  - `window.confirm`で確認ダイアログ=ポップアップを表示する

```js
function isTweetable(text) {
  return text.length <= 140;
}

function follow() {
  console.log("followed");
}
function cancelTweet() {
  console.log("canceled");
}
function confirmed(fn) {
  if (window.confirm("Are you sure?")) {
    fn();
  }
}

confirmed(follow);
confirmed(cancelTweet);
```

- 匿名関数への置き換え

```js
const cancelTweet = function () {
  console.log("canceled");
};
confirmed(cancelTweet); //=> 同じ結果, しかし関数を再利用しない場合は匿名関数を使う
confirmed(function () {
  console.log("canceled");
}); //=> 匿名関数を直に渡すこともできる
```

- コールバック関数の実践例 2
  - Github の DeleteRepository は文字入力後に削除ボタンが押せるようになる
  - => `window.prompt`で入力ダイアログを表示する

```js
const deleteRepository = function (input) {
  console.log("your input is: " + input);
  console.log("Deleting the repository...");
};
function confirmed(fn) {
  const input = window.prompt("Are you sure?(yes/no)");
  if (input === "yes") {
    fn(input);
  }
}

confirmed(deleteRepository);
```

- コールバック関数の実践例 3
  - ボタンをクリックしたら、アクションする
  - `addEventListener`でイベントを登録する => イベントが発生したら登録されたコールバック関数を非同期で行う

```js
const btn = document.getElementById("btn");

btn.addEventListener(
  "click",
  () =>
    function () {
      console.log("Button clicked");
    }
);
// => ボタンをクリックしたら、コンソールにButton clickedが表示される
```

- リストには forEach コールバックを使う
  - `foods`リストの中身を表示する

```js
const foods = ["pizza", "burger", "fingerChips", "donuts", "springRoll"];

foods.forEach(function (food) {
  console.log(food);
});
```

- # => コールバック関数はイベントが発生したら非同期で実行される関数で、条件文や共通の前後処理を外に定義できる(イベントやトリガーぽい)

### WebAPI

- 参考: [ Json PlaceHolder](https://jsonplaceholder.typicode.com/)で API を取得する

  - API 例以外に好きなダミー API を作れたりする, UI プロトタイプとかに使える

- WebAPI 自体はバックエンドが通常開発する。フロントエンドは API を使って UI を構築する
- API を JS で叩いて、よく認証つきでデータやり取りをする

- `window.fetch`で API を叩く
  - `fetch`は Promise を返す
  - `then`で成功時の処理を記述
  - `catch`で失敗時の処理を記述

```js
function callApi() {
  const res = fetch("https://jsonplaceholder.typicode.com/users");
  console.log(res);
}

callApi();
```

- 非同期処理
  - 関数の前に`async`をつける => 関数内で`await`を使える
  - `fetch` に`await`をつけると、 `Response`オブジェクトを返すようになる
  - `Response`オブジェクトは`json`メソッドを持っている
    - `res.json()`で JSON を取得し、そこから所望のデータを取得する

```js
async function callApi() {
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  console.log(res);
}
```

- `fetch` と `then` でもかける(async の方が新しめ)

```js
function callApi() {
  fetch("https://jsonplaceholder.typicode.com/users")
    .then(function (res) {
      return res.json();
    })
    .then(function (json) {
      console.log(json);
    });
}
```

- `xhr` でもかける

```js
function callApi() {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "https://jsonplaceholder.typicode.com/users");
  xhr.responseType = "json";
  xhr.send();
  xhr.onload = function () {
    console.log(xhr.response);
  };
}
```

(fetch, xhr だと Response が取れなかったあ...l)

- # => WebAPI は `window.fetch` で API を叩くことができる。非同期処理を行うためには `async` と `await` を使う

### 簡単な WebAPI 操作を作る

- 作るもの: user 情報を取得して 10 件表示する + ボタンを押すと下に 10 件追加する
- 実装時のメモ
  - ` document.createElement` で HTML 要素をなんでも作れる
  - `fetch` で API を叩いて`Response`オブジェクトを取得するために、`async`と`await`を使う
  - `const lists = document.getElementById("lists")`でリストを取得して、`lists.appendChild`でリストに追加することで、DOM 側も更新できる
    - `const list = document.createElement("li")`でリストを作成して、`list.innerText = `でテキストを追加する
    - `users.forEach(<callback func>(user){})`でリストを作成して、`lists.appendChild(list)`でリストに追加する
    - `for` + enter でひな形作成;
      - tab を推すごとに、`index` -> `array` -> `element` のようにカーソルが移動し、一括で変更できる

```js
const button = document.getElementById("addBtn");
const lists = document.getElementById("lists");

if (button) {
  button.addEventListener("click", async function () {
    const res = await fetch("https://jsonplaceholder.typicode.com/users");
    const users = await res.json();
    console.log(users);

    // DOM操作(for文)
    // for (let index = 0; index < users.length; index++) {
    //   const user = users[index];
    //   const list = document.createElement("li");
    //   list.innerText = user.address.zipcode;
    //   lists.appendChild(list);
    // }
    /// DOM操作(forEach文)
    users.forEach(function (user) {
      if (user.id <= 5) {
        return; // user.idが5以下の場合は処理をスキップ
      }
      const list = document.createElement("li");
      list.innerText = user.address.zipcode;
      lists.appendChild(list);
    });
  });
} else {
  console.log("No button");
}
```

- # => foreach で DOM 操作したり、DOM 要素を編集可能

### リファクタリング

1. 共通する関数を定義
2. 纏まった処理を関数にまとめる
   1. API を叩く処理
      1. 中で`fetch`を使って API を叩いているので, `async`と`await`を使う
3. コールバック関数: コールバック関数として匿名関数(無名関数)があるときに、それを関数に切り出す
4. 順序: 関数定義で, `function`と`async`をそれぞれまとめて順に定義する
5. `window`に関する処理を、`document`よりも上に書く
6. コメント
   1. DOM 要素の取りだし //DOM
   2. 関数定義 //Functions(Methods)
   3. イベント/コード //Events

- リファクタリングは定期的に行うことが重要, 動くとしても、可読性が悪いとコード全体の評価が下がる

```js
// DOM
const button = document.getElementById("addBtn");
const lists = document.getElementById("lists");

// Functions(Methods)
function addList(user) {
  const list = document.createElement("li");
  list.innerText = user.address.zipcode;
  lists.appendChild(list);
}

async function getUsers() {
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  const users = await res.json();
  return users;
}

async function listUsers() {
  const users = await getUsers();
  console.log(users);

  users.forEach(addList);
}

// Event
window.addEventListener("load", listUsers);

if (button) {
  button.addEventListener("click", listUsers);
} else {
  console.log("No button");
}
```

- # => リファクタリングは定期的に行うことが重要,

【メモ】

VSCode 上で JS ファイルを実行して Console ログを確認する方法

- ターミナルで `node ファイル名.js` で実行
- `document`はブラウザ上でのみ動作する=>`alert`とかは vscode 上だと動かない

以下のように実装内容を言語資するの見やすいな
![[Pasted image 20240729200409.png]]

ブラウザをロードしても、js が実行されないときは、タイポを疑う

ページに新たな js を追加するときは、`<script src="index.js"></script>`を body の最後に追加する

- - `index.html` と同じ階層に配置する
- テストはブラウザをリロードするだけ

vim: ビジュアルモードの状態で`shift + I` で複数行挿入モードになる

ol タグで番号つきリストを作成できる

- `ol>li*3`で 3 つのリストを作成できる

js で特定の要素にイベントを登録したいときは、 `js`ファイル内で`document.getElementById("id名")`で取得してそこで変数化しておく。それ以降の行でその変数に対してイベントを登録するのが可読性が高い

- `addEventListener`でイベントを登録する際は、要素が null でないか確認する

```js
const btn = document.getElementById("btn");
if (btn) {
  btn.addEventListener("click", function () {
    console.log("Button clicked");
  });
}
```

関数定義は、3 通り

1. 関数名をつけてべた書き定義(`fuction getUsers(){}`)
2. 関数式を使うか(`const getUsers = function(){}`)
3. コールバック関数の際に無名関数として使う(`btn.addEventListener("click", function(){})`)

関数の範囲を見る際は、`{}`で囲まれた範囲を見ると良い

- 終わりの`}`がどこにあるかを確認する

## 参考

[\_JavaScript 入門編 - YouTube](https://www.youtube.com/playlist?list=PLpYVzO5BZomqbLjRiHo7VvVYotX9QoQ0N)

## まとめ(類似点・相違点)

バックエンドは webapi を作る仕事

- webapi からデータベースへは直接アクセスできないようになっている
- 認証とかが走る
