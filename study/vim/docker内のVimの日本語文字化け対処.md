start：[[2023-03-15]] 15:35

参考様: https://qiita.com/n_oshiumi/items/cfe91c60730f602b38eb
以上の記事を Dockerfile の上の方に書き込んで解決

- Dockerfile を作成したら、その都度、build する必要があるので注意
- 結構言語パックはインストールが長い

以下は競プロ用の Docker; 試作

```Dockerfile
# ベースイメージの選択
FROM ubuntu:20.04

# タイムゾーンの設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# ロケールの設定
RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen ja_JP.UTF-8 \
    && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    gdb \
    git \
    curl \
    wget \
    vim \
    && rm -rf /var/lib/apt/lists/*

# C++のバージョンを指定
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    g++-9 \
    && rm -rf /var/lib/apt/lists/*

# ワーキングディレクトリの設定
WORKDIR /workspace


```
