start：[[2023-02-27]] 06:07

- Docker は Linux 上で動く

  - DockerDesktop は mac や windows 上で Docker を動かして、Docker ホストにする

- `docker logs` でログを見れる
- `docker port` でマッピング状況を確認できる
- p オプションは必ず設定する。
  - 設定しないと、コンテナにアクセスできないため

### マッピングとマウントの意味

- mapping
  - ポートを設定して、ホストとコンテナをポートを対応づけて、ホストのポートからコンテナのポートにアクセスできるようにする
  - localhost でコンテナ内のアプリにアクセスできる
  - fastapi とかで使えそう
  - `docker run -p 8000:80 my-image` で、`http://localhost:8000`でコンテナのアプリにアクセスできる
    - ホスト側のポートが 8000 でコンテナ内が 80
- mout
  - ホストとコンテナでファイルを共有する
  - ホスト側のファイルをコンテナ側にコピーする
  - また、ホスト側のファイルを変更すると、コンテナのファイルも変更される
  - `docker run -v ~/my-data:/data my-image` で、ホストマシンの `~/my-data` ディレクトリをコンテナの `/data` ディレクトリにマウントしている。
    - my-data 内のファイルがコンテナ内の data ディレクトリに自動でコピーされ、変更が反映される。

### docker-compose

- より、一括した処理をするコマンドっぽい
- compose.yml で設定を一括して設定できる

### ボリューム

- マウントして、ホストとコンテナ間でファイルを共有する仕組みのこと
- まず、マウントすることで、コンテナを削除してもデータがホスト側に残る。

- データを永続に残しておける。
- マウントを重複させることで、複数のコンテナ間でデータを共有して、スケーリングすることができる

### DockerFile

- Image 作成と設定をするものであり、Hub にアップロードされたりする

- COPY は事前に Image に含めるファイルを指定する
  - requirements.txt だったり、/src 内のファイルだったり
- VOLUME は、ホストと共有され、コンテナ内での変更はホストマシンの方で保存されている。=永続化したいものに使用する。
  - /data とかをボリュームとして指定する
    - COPY ダトデータが大きすぎる場合苦労するため
  - 実行ファイルなどは指定しない
    - 永続化したいものではないため

### コンテナからの抜け方

- exit or ctrl+d

### 基礎動画(乱取り)

- https://www.youtube.com/watch?v=0H2miBK_gAk
- https://github.com/patrickloeber/python-docker-tutorial
- https://www.youtube.com/watch?v=gAkwW2tuIqE

DockerFile を書いて、build することで、カスタマイズされた DockerImage を作成できる。

docker-compose.yml で、docker run のオプション設定だったりをまとめられる。

- 設定を書いた yml を実行すれば良い

### インストール方法

1.  Docker をダウンロードおよびインストールする Docker の公式 Web サイト([https://www.docker.com/products/docker-desktop)から、Docker](https://www.docker.com/products/docker-desktop)%E3%81%8B%E3%82%89%E3%80%81Docker) Desktop for Mac をダウンロードして、インストールしてください。Docker Desktop for Mac は、Mac 上で Docker を実行するためのオールインワンのパッケージです。
2.  Docker Desktop for Mac を起動する インストールが完了したら、Docker Desktop for Mac を起動してください。起動後、Docker アイコンが Mac のメニューバーに表示されます。
3.  Docker を使用する Docker を使用するには、Docker コマンドをターミナルで実行する必要があります。ターミナルを開いて、以下のようなコマンドを実行してみてください。

    Copy code

    `docker run hello-world`

    これは、Docker イメージ "hello-world" を実行するコマンドです。Docker が正しくインストールされていれば、"Hello from Docker!" というメッセージが表示されます。

### その他

- Docker Hub
  - 自分の push したイメージを見れる
  - https://hub.docker.com/repositories/takeshun256
