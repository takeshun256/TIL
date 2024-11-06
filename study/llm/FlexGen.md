start：[[2023-03-02]] 23:48

## 参考

- https://github.com/karaage0703/FlexGen-docker
- https://zenn.dev/karaage0703/articles/de7045e9792623
- https://github.com/FMInference/FlexGen

## 内容

参考文献見て、docker で動かした。

- https://github.com/karaage0703/FlexGen-docker

model の download で時間かかる。
小さなモデルは結構頭悪めかもしれない。もう少し大きいモデルを使ってみる。

```bash
# buildする
$ git clone https://github.com/karaage0703/FlexGen-docker
$ cd FlexGen-docker
$ docker build -t ubuntu:FlexGen .

# docker run
$ docker run -it -v $(pwd):/root --gpus all ubuntu:FlexGen

# 一番軽いモデル
python3 apps/chatbot.py --model facebook/opt-6.7b --compress-weight
```

- https://github.com/FMInference/FlexGen

opt-30b のものを入れようとしたが、wsl の容量が足りなかった
