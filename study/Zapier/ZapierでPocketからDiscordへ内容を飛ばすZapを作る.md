start：[[2024-07-17]] 19:35

## 経緯・背景・興味・目標

記事とかをワンクリックで obsidian か discord に飛ばせたらよいなと思い、IFTTT と Zapier のなかで zapier で作ってみる

## 内容

[[Account/<username>/Zapier|Zapier]]: アカウント内容

作成した

- それぞれの Connection するアプリケーションにログイン
- フローを 2Zap までで作成 - Pocket/archive => URL を Discord の pocket channel へ投稿
  [zapier.com/app/login?next=%2Fapp%2Fzap%2F249148661&type=login&referer=](https://zapier.com/app/zap/249148661)
  テスト Run では飛ばしてくるが、Archive してもすぐ飛ばさない => なんか設定があるのかな？
  また、無料版は 1000Tack(Trigger)リミットがあるらしい

=> なんか別の方法ないかな

- 単純に pocket api を使って、discord api に飛ばす
