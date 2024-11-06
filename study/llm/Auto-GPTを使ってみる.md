start：[[2023-05-08]] 10:51

### AutoGPT とは

コーディングやモデルの構築を自動化する

- [AutoGPT とは何か？ ChatGPT を「さらに自動化」するツールの基本と具体的な使用方法 ｜ビジネス+IT](https://www.sbbit.jp/article/cont1/114615)

- [GitHub - Significant-Gravitas/Auto-GPT: An experimental open-source attempt to make GPT-4 fully autonomous.](https://github.com/Significant-Gravitas/Auto-GPT)

### 導入

参考：

- [AutoGPT とは何か？ ChatGPT を「さらに自動化」するツールの基本と具体的な使用方法 ｜ビジネス+IT](https://www.sbbit.jp/article/cont1/114615)
- [Setup - Auto-GPT](https://docs.agpt.co/setup/)

- APIkey 取得

  - [[ChatGPT API]]
  - [OpenAI Platform](https://platform.openai.com/account/api-keys)

- 最新の安定リリースを取得する
  - [Release Auto-GPT v0.4.4 · Significant-Gravitas/Auto-GPT · GitHub](https://github.com/Significant-Gravitas/Auto-GPT/releases/tag/v0.4.4)

```python
wget https://github.com/Significant-Gravitas/Auto-GPT/releases/tag/v0.4.4
unzip v0.4.4.zip
cd Auto-GPT-0.4.4
```

- git と docker でインストールする
  - [Setup - Auto-GPT](https://docs.agpt.co/setup/)の Set up without Git/Docker をする

```python
cp .env.template .env
vi .env
# OPENAI_API_KEY=<my-key>に編集する
```

- Docker で動かす
  - [Setup - Auto-GPT](https://docs.agpt.co/setup/) の Running Auto-GPT

```python
docker compose version
docker compose build auto-gpt
docker compose run --rm auto-gpt

# 任意の引数
# docker compose run --rm auto-gpt --gpt3only --continuous
```

↑ 多分、コンテナを run した段階で、run.sh が走るんだろうな

---

- Vsocde の remote で開く
  - 上記のコンテナにサイドバーからアタッチする
  - (コマンドパレットから Dev Containers: Open Folder in Container)
  - もしくは、サイドパネルの remote explorer から、開発コンテナで、開く
  - run `./run.sh`

プロジェクトディレクトリを vscode で開くと、自動的に dev container で開かれて、コンテナ内で作業することになった

---

受け答えメモ(英語なので重要なことのみ)

> 「y」を入力してコマンドを認証する場合は「y」を、N 回連続でコマンドを実行する場合は「y -N」と入力してください。プログラムを終了する場合は「n」と入力してください。または、QAGPT へのフィードバックを入力してください。

1. 起動時に、やってもらいたいことを入力
2. 継続する際は、質問をする
3. 終了する際は、n を入力

- 日本語入力も OK だが、精度は悪く、日本語ではなく英語で返ってくる
  - おそらく、OpenAI ではなく日本語特化にすればよいのかな
  - それか言語のパラメータがあるかどうか

---

#### プラグインのインストール

結局開発中のものだから、使わない方が良いかもしれない

- 無効化して普通に実行する

```sh
cd plugins
mv Auto-GPT-Plugins.zip Auto-GPT-Plugins.zip-notuse
cd ..
docker compose run --rm auto-gpt
```

プラグインは、plugins_config.yaml で管理される。

- 経緯
- plugin の installation を参考にインストール
  - [GitHub - Significant-Gravitas/Auto-GPT-Plugins: Plugins for Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT-Plugins)

```python
pwd # /home/takes/Programming/Python/Auto-GPT-0.4.4
curl -L -o ./plugins/Auto-GPT-Plugins.zip https://github.com/Significant-Gravitas/Auto-GPT-Plugins/archive/refs/heads/master.zip

# python >= 3.10以上が必要なので、condaを使用する
conda create -n auto-gpt-plugin-install python=3.10
conda activate auto-gpt-plugin-install

# install(dev container内で仕様：外だとPythonのバージョンではじかれる)
sudo ./run.sh --install-plugin-deps

# pluginを設定(ファイルを新規作成)
vi plugins_config.yaml
# 以下例
AutoGPTSpacePlugin:
    config: {}
    enabled: true

# 再度buildして vscodeで開く
ocker compose down && docker compose build auto-gpt
```

permission denied 対策

- 以下をコメントアウト
- [logger.py](https://github.com/Significant-Gravitas/Auto-GPT/blob/a758acef2cf12b206d7172b47880dd876f8ad4bc/autogpt/logs/logger.py#L28-L29C46)
- 参考：[PermissionError: [Errno 13] Permission denied: '../logs' · Issue #1328 · Significant-Gravitas/Auto-GPT · GitHub](https://github.com/Significant-Gravitas/Auto-GPT/issues/1328)

```
vi autogpt/logs.py
```

-
- プラグインの種類はたくさんある

  - [GitHub - Significant-Gravitas/Auto-GPT-Plugins: Plugins for Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT-Plugins#first-party-plugins)

- プラグインの書き方
  - [Plugins - Auto-GPT](https://docs.agpt.co/plugins/)
- 例

```python
plugin_a:
  config:
    api_key: my-api-key
  enabled: false
plugin_b:
  config: {}
  enabled: true
```

## 参考

- [AutoGPT Official](https://autogpt.net/)
- [AutoGPT とは何か？ ChatGPT を「さらに自動化」するツールの基本と具体的な使用方法 ｜ビジネス+IT](https://www.sbbit.jp/article/cont1/114615)
- [GitHub - Significant-Gravitas/Auto-GPT-Plugins: Plugins for Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT-Plugins)
- [GitHub - Significant-Gravitas/Auto-GPT: An experimental open-source attempt to make GPT-4 fully autonomous.](https://github.com/Significant-Gravitas/Auto-GPT)
- [AutoGPT プラグインを解放する：包括的なガイド – Kanaries](https://docs.kanaries.net/ja/tutorials/ChatGPT/autogpt-plugins)
