start：[[2024-07-02]] 13:28

### [[vim 基礎]]のコマンド

- [x] **`*`**: カーソル位置の単語の位置を検索, ビジュアルモードで複数文字使える - v で選択した状態だと移動して、範囲が移動した分も含まれるようになる
      ![[Pasted image 20240702141958.png]]

- [x] **`.`**: 直前の変更操作を繰り返す
- [x] **`f{char}`**: 次の char へ移動 ex. fa =>業内の f に移動 ✅ 2024-07-02
  - [x] 現在の行内での移動、後は英数字だけの方が使いやすい ✅ 2024-07-02
- [x] `/{chars}` : 次の chars へ移動, 行関係ない ✅ 2024-07-02
- [x] **`;`**: 直前の f{char}操作を繰り返す ✅ 2024-07-02
- [x] `n`: 直前の /{chars} 操作を繰り返す ✅ 2024-07-02
- [x] **`A`**: $a 行の末尾に移動し、カーソル位置の後で挿入モードへ ✅ 2024-07-02
- [x] **`s`**: カーソル位置の 1 文字を削除して、挿入モードっ j へ ✅ 2024-07-02
- [x] `x`] カーソル位置を削除 ✅ 2024-07-02
- [x] **`u`**: 直前の 処理を元に戻す ✅ 2024-07-02
- [ ] **`,`**: 直前の f{char}操作を逆方向に繰り返す
- [ ] **`aw`**: a word カーソル位置にある単語を選択
- [ ] **`ctrl+a`**: カーソルにある数字を+1 する。カーソル下に数字がない場合、行内にある数字に飛んで+1 する。前に数字を指定して複数回処理するのが良い
- [ ] **`ctrl+x`**: カーソルにある数字を-1 する
- [ ] **`yy`**: 行をコピー
- [ ] **`p`**: 貼り付け
- [ ] **`yyp`**: 行を次の行にコピーする = ctrl+c ctrl+v
- [ ] **`cw`**: 単語を編集する=削除して挿入モードへ
- [ ] **`gu`**: 小文字にする operator
- [ ] **`gU`**: 大文字にする operator
- [ ] **`g~`**: 小文字大文字を切り替える operator
- [ ] **`>`**: インデントを深くする operator
- [ ] **`<`**: インデントを浅くする operator
- [ ] **`ap`**: a paragraph 1 つのパラグラフ
- [i] **`ctrl + u`**: 画面の上部へ移動 up
- [i] **`ctrl + d`**: 画面の下部へ移動 down
- [i] **`ctrl + b`**: 前ページへ移動 back page
- [i] **`ctrl + f`**: 次ページへ移動 forward page
- [ ] **`e`**: 単語の最後に移動
- [i] **`ctrl + h`**: 画面の一番初めに移動 何回実行しても同じ
- [i] **`ctrl + l`**: 画面の一番終わりに移動 何回実行しても同じ
- [x] `H`: 画面上部に移動
- [x] `L`; 画面下部に移動
- [x] `M`: 画面中央に移動
- [ ] `{` : 前の段落(空行)に移動
- [ ] `}`: 後の段落(空行)に移動

- [ ] nG で n 行目に飛ぶ
- [ ] `:n + enter` で n 行目に飛ぶ
- [ ] 【メモ】

- [ ] **文字単位の移動**
  - [ ] `f<char>`：現在の行で次に出現する指定した文字に移動します（forward）。
  - [ ] `F<char>`：現在の行で前に出現する指定した文字に移動します（backward）。
  - [ ] `t<char>`：現在の行で次に出現する指定した文字の 1 文字手前に移動します（till）。
  - [ ] `T<char>`：現在の行で前に出現する指定した文字の 1 文字手前に移動します（backward till）。
- [ ] **パターン検索による移動**
  - [ ] `/pattern`：指定したパターンを検索し、次に出現する場所に移動します。
  - [ ] `?pattern`：指定したパターンを検索し、前に出現する場所に移動します。
  - [ ] `n`：検索の次の一致箇所に移動します（`/`または`?`の後）。
  - [ ] `N`：検索の前の一致箇所に移動します（`/`または`?`の後）。
  - [ ]
