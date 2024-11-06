start：[[2023-02-28]] 01:58

## 内容

Python のディレクトリ構成

- パッケージング、テスト、ドキュメント生成、および CI/CD のためのディレクトリを含む

```
mylibrary/
├── mylibrary/
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   ├── test_module2.py
│   └── ...
├── docs/
│   ├── conf.py
│   ├── index.rst
│   ├── ...
│   └── _build/
├── examples/
│   ├── example1.py
│   ├── example2.py
│   └── ...
├── setup.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── Dockerfile
└── .dockerignore

```

- `Sphinx`などのツールを使用して、HTML、PDF、EPUB などのフォーマットでドキュメントを生成することができます。

### CICD 用

```
├── .circleci/
│   ├── config.yml
└── .github/
    ├── workflows/
    │   └── test.yml
```

- `.circleci/`: CircleCI の設定ファイルを格納するためのディレクトリ。`config.yml`ファイルを含みます。
- `.github/workflows/`: GitHub Actions の設定ファイルを格納するためのディレクトリ。`test.yml`ファイルを含みます。

CI/CD は、コードの品質を維持するために非常に重要であり、GitHub Actions や CircleCI などのツールを使用して実装することができます。これらのツールを使用すると、テストや Linting、コードカバレッジの計測などを自動化することができます。また、CI/CD を導入することで、開発チーム全体でコード品質を向上させることができます。

### DockerFile

```dockerfile
# Dockerイメージのベースとなるイメージを指定
FROM python:3.8

# ライブラリの依存関係を定義したrequirements.txtをコンテナ内にコピー
COPY requirements.txt .

# ライブラリの依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# パッケージをコンテナ内にコピー
COPY . /app
WORKDIR /app

# Dockerイメージの起動時に実行するコマンドを指定
CMD [ "python", "-m", "mylibrary" ]
```

1.  Python の 3.8 をベースとした Docker イメージを取得
2.  `requirements.txt`をコンテナ内にコピー
3.  `pip`を使用して、`requirements.txt`に指定されたライブラリの依存関係をインストール
4.  `mylibrary`パッケージをコンテナ内にコピー
5.  コンテナ内での作業ディレクトリを`/app`に設定
6.  Docker イメージの起動時に、`python -m mylibrary`コマンドを実行するように設定

イメージを build する！！

## 類似点・相違点・まとめ

パッケージというかライブラリ作成はあんな感じで、機能ごとにディレクトリが分かれている。
