start：[[2024-07-20]] 00:45

## 経緯・背景・興味・目標

ホームポジションを使いたいと思った
おそらく enter や backspace で無意識のうちに数秒ロスしているため

AutoHotkey を用い得る

- PC 設定や PowerToys や RealForce はショートカット(就職キー以外の)がなかった。
- => なんか月一で壊れるらしい...
  - [Tsukino Hoshina 日記「キーボードを購入いたしました（Realforce R3）」 | FINAL FANTASY XIV, The Lodestone](https://jp.finalfantasyxiv.com/lodestone/character/35470695/blog/4890853#:~:text=%E6%9C%88%E3%81%AB1%E5%BA%A6%E3%81%8F%E3%82%89%E3%81%84%E3%81%A7%E3%81%AF%E3%81%82%E3%82%8B%E3%81%8C%E3%80%81%E3%82%AD%E3%83%BC%E3%81%8C%E6%8A%BC%E3%81%97%E3%81%A3%E3%81%B1%E3%81%AA%E3%81%97%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A6%E3%81%97%E3%81%BE%E3%82%8F%E3%82%8C%E3%82%8B%E3%81%AE%E3%81%A0%E3%80%82%0A%E4%B8%80%E5%BA%A6%E3%80%81%E7%99%BA%E7%97%87%E3%81%99%E3%82%8B%E3%81%A8%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89%E6%93%8D%E4%BD%9C%E3%82%92%E8%AB%A6%E3%82%81%E3%80%81%E3%83%9E%E3%82%A6%E3%82%B9%E3%81%AB%E9%A0%BC%E3%82%89%E3%81%96%E3%82%8B%E5%BE%97%E3%81%AA%E3%81%84%E3%80%82%E5%BE%A9%E6%97%A7%E3%81%8C%E9%9B%A3%E3%81%97%E3%81%8F%E3%80%81%E6%9C%80%E6%82%AA%E3%80%81PC%E3%81%AE%E5%86%8D%E8%B5%B7%E5%8B%95%E3%81%A8%E3%81%AA%E3%82%8B%E3%80%82%0A%0A%E8%92%BC%E5%A4%A9%E3%81%BE%E3%81%A7%E3%81%AF%E3%80%81%E3%81%BE%E3%81%A0%E3%82%88%E3%81%8B%E3%81%A3%E3%81%9F%E3%80%82%E7%99%BA%E7%97%87%E3%81%97%E3%81%9F%E3%81%A8%E3%81%A6%E3%80%81%E3%83%9E%E3%82%A6%E3%82%B9%E6%93%8D%E4%BD%9C%E3%81%A7%E3%82%82%E3%83%AA%E3%82%AB%E3%83%90%E3%83%BC%E3%81%A7%E3%81%8D%E3%81%9F%E3%80%82%0A%E3%81%97%E3%81%8B%E3%81%97%E3%80%81%E7%B4%85%E8%93%AE%E3%82%88%E3%82%8A%E9%9B%A3%E6%98%93%E5%BA%A6%E3%81%8C%E5%A2%97%E3%81%97%E3%80%81%E7%99%BA%E7%97%87%E3%81%97%E3%82%88%E3%81%86%E3%82%82%E3%81%AE%E3%81%AA%E3%82%89%E3%80%81%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%83%BC%E3%81%AE%E7%9A%86%E6%A7%98%E3%81%AB%E3%81%94%E8%BF%B7%E6%83%91%E3%82%92%E3%81%8A%E3%81%8B%E3%81%91%E3%81%97%E3%82%88%E3%81%86%E3%80%82%E3%81%A8%E3%81%84%E3%81%84%E3%81%BE%E3%81%99%E3%81%8B%E3%80%81%E3%81%99%E3%81%A7%E3%81%AB%E4%BD%95%E5%90%8D%E6%A7%98%E3%81%8B%E3%81%AF%E5%9C%B0%E7%8D%84%E9%80%81%E3%82%8A%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A6%E3%81%97%E3%81%BE%E3%82%8F%E3%82%8C%E3%81%9F%E3%80%82)

=> RealFoce の Fn でできそう

[Tsukino Hoshina 日記「キーボードを購入いたしました（Realforce R3）」 | FINAL FANTASY XIV, The Lodestone](https://jp.finalfantasyxiv.com/lodestone/character/35470695/blog/4890853)
[キーボードを最適化する教科書｜新卒 5 年目の IT コンサルタント](https://note.com/consultant1221/n/n371fb9e8ce9d)

## 内容

### 以下仕様

MuhenkanKey に、Fn を割り当てて、RealFoce の方で Fn+j とかに enter を割り当てる

1. Window の右下の文字列から、設定=> 「キーとタッチのカスタマイズ」=> キーの割り当て OFF
2. RealForce 設定側で以下のように設定する
   1. 通常バージョン
      1. Muhenkan->IMEoff
      2. Henkan -> Fn
   2. Fn バージョン
      1. Henkan -> IMEon
      2. hjkl ->方向キー
      3. o->backspace
      4. p->Enter
      5. ;->tab
         1. indent や alt+Fn+;で window 移動簡単！

->注意：Fn の設定で就職キー事態を登録はできない

## まとめ(類似点・相違点)

RealForce の設定を利用することで、すべての動作設定をまとめ、ホームポジションで、vim や方向キーや backspace, Enter の操作ができるようになった！！
