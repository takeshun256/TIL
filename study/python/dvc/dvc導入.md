start：[[2023-10-28]] 07:08

### dvc をはじめに触ってみる

[Home | Data Version Control · DVC](https://dvc.org/doc)

#### install

- mac 上

```python
arch -arm64 brew install dvc
```

- リポジトリ上

```python
git clone git@github.com:takeshun256/dvc-study.git
# pip install dvc[gdrive] dependencyを指定する必要がある gdriveないらしい
cd dvc-study
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install dvc # 指定せずにインストールできた。
```

- git リポジトリ内で、初期化

```python
# 初期化, .dvcフォルダと.dvcignoreが作成される
dvc init
git status # すでにstagingされている
git cm -m "Initialize DVC"
```

↑ 匿名で install したかを dvc 側で集計してるらしい

### data management

- [Get Started: Data Management | Data Version Control · DVC](https://dvc.org/doc/start/data-management#chapters)

#### データを管理してみる(Data Versioning)

- [Get Started: Data Versioning | Data Version Control · DVC](https://dvc.org/doc/start/data-management/data-versioning)
- git for data

```python
# dvc レポジトリで管理されているファイルをダウンロードできる。(git pullに近いな)
dvc get https://github.com/iterative/dataset-registry \
          get-started/data.xml -o data/data.xml

# dvcでtrackingする (git addd に近いな)
# data/data.xml.dvcというgit 追跡可能なメタデータファイル(プレースホルダー: 標識)を保存する
# データがあった場所に標識を置いておくかんじ + data/.gitignore更新
dvc add data/data.xml

# git で追跡する + .gitignoreに元データを管理しないようにgitignoreが更新されている
git add data/data.xml.dvc data/.gitignore
$ git commit -m "Add raw data"

# dvc addしたら 標識を git addするのを自動で行う設定
dvc config core.autostage true

# 作成されたgitignoreの中身
$cat data/.gitignore
/data.xml

# リモートストレージを設定(local remote)
mkdir /tmp/dvcstore # localのrootディレクトリ下にあるtmpフォルダ
dvc remote add -d myremote /tmp/dvcstore # remoteに設定する
dvc remote list # remoteを表示, 複数設定できるのかな

# upload data to remote storage
dvc push

# Retrieving data
dvc pull

# Retrieving data with fresh pull (データやキャッシュがない状態)
rm -rf .dvc/cache
rm -rf data/data.xml
dvc pull

=========================
# storage増やしてみる(defaultを書き換える方が良さそう, 複数あると複数ストレージに跨った際に面倒になる, やり方はurl参照)
# - [Remote Storage | Data Version Control · DVC](https://dvc.org/doc/user-guide/data-management/remote-storage)
# gdriveの追加の仕方: [Google Drive | Data Version Control · DVC](https://dvc.org/doc/user-guide/data-management/remote-storage/google-drive)
pip install dvc-gdrive

# data add
dvc get https://github.com/iterative/dataset-registry \
          get-started/data.xml -o data/data2.xml # 新しくpushするためのデータダウンロード
dvc add data/data2.xml
# dvc remote add gremote gdrive://URL <=　実際にGDrive上でフォルダを作成してパスをコピー
# [Google ドライブ: ログイン](https://drive.google.com/drive/folders/1w6YmSEVxx-zwYS8ph7MZpYQophcFyIhS?usp=drive_link)
dvc remote add gremote gdrive://1w6YmSEVxx-zwYS8ph7MZpYQophcFyIhS # -d: defaultにする [remote | Data Version Control · DVC](https://dvc.org/doc/command-reference/remote)
dvc remote list # gdriveが増えている
-----
# myremote        /tmp/dvcstore
# gremote gdrive://1w6YmSEVxx-zwYS8ph7MZpYQophcFyIhS
-----

dvc remote modify gremote gdrive_acknowledge_abuse true # 権限許可対象
dvc push -h # 設定を確認
dvc push -r gremote # 同期のために1度だけ実行, default remoteでないので、明示的に指定
dvc pull -r gremote # pullも指定必要
============================


# push meta files
git add -A
git cm -m "push data.xml data2.xml to gdrive"
git push

# リモートストレージを書き換える(これremoteのデータも削除しないとあまり意味ないかも, 別にどちらのremoteで管理されていても良いよね)
rm -f data/data.xml.dvc
dvc gc --workspace -v # 現在のプロジェクトで参照されている情報以外のcache削除, -v: --verbose, --dryでdryrun
dvc add data/data.xml
dvc push # defaultremoteにpushされる


# データのバージョンを切り替えてみる
git checkout <...>
dvc checkout

# 前のバージョンのデータに戻す
git checkout HEAD~1 data/data.xml.dvc
dvc checkout
git commit data/data.xml.dvc -m "Revert dataset updates"
```

#### data piplines

---

- [Get Started: Data Pipelines | Data Version Control · DVC](https://dvc.org/doc/start/data-management/data-pipelines)
- INtor
  - [Machine Learning Pipelines with DVC (Hands-On Tutorial!) - YouTube](https://youtu.be/71IGzyH95UY)
  - こんな可愛い人いが開発しているのか、 あと実験を yaml で管理して Makefile みたいにしているワクワクするな
- データの処理を yaml ファイルにまとめることができる

- pipline の構築
  - dvc stage add で 各ステージを登録
  - 各ステージの依存関係を登録しておくことで、ステージ処理間の順番などが定義される
    - dependency graph
    - [Defining Pipelines | Data Version Control · DVC](https://dvc.org/doc/user-guide/pipelines/defining-pipelines)
    - dvc.yaml で依存関係もろもろを記載しており、dvc.lock でその状態 hash を管理しており、もし更新がある場合は再現するかどうかを lock ファイルで判断する
  - パラメータは、params.yaml で定義できる
  - 依存関係に、必要なソースコードも定義する
    - この依存関係が変更された場合に dvc が再現が必要だと判断する
  - dvc repro で実行する
    - それぞれの出力が記録されており、データの変化も dvc.lock で捉えるため、実行時に変化がない箇所はスキップされる
    - [Get Started: Data Pipelines | Data Version Control · DVC](https://dvc.org/doc/start/data-management/data-pipelines#learn-how-to-parametrize-and-use-cached-results)

```python
# サンプルデータをダウンロード
# wget https://code.dvc.org/get-started/code.zip  # for windows
curl https://s3-us-east-2.amazonaws.com/dvc-public/code/get-started/code.zip --output code.zip
unzip code.zip && rm -f code.zip
dvc get https://github.com/iterative/dataset-registry \
          get-started/data.xml -o data/data.xml

# データ構造
tree
.
├── params.yaml
└── src
    ├── evaluate.py
    ├── featurization.py
    ├── prepare.py
    ├── requirements.txt
    └── train.py

# 仮想環境作成
python -m venv .venv: echo ".venv" >> .gitignore
source .venv/bin/activate
pip install -r src/requirements.txt
git add -A
git cm -m "code setup"

# ステージング(前処理)
# 実行コマンド + パラメータ + 依存関係 + 出力情報
# ステージにprepareステージが追加される, 各ステージがあるとのこと
# dvc.yamlが作成される
# 生成されたデータ(data/prepared)も自動でステージングされる
dvc stage add -n prepare \
                -p prepare.seed,prepare.split \ # パラメータ情報
                -d src/prepare.py -d data/data.xml \ # 依存関係
                -o data/prepared \ # 生成されるデータ
                python src/prepare.py data/data.xml # 実行コマンド：python src/prepare.py data/data.xml

# ステージング(特徴量抽出)
dvc stage add -n featurize \
                -p featurize.max_features,featurize.ngrams \
                -d src/featurization.py -d data/prepared \
                -o data/features \
                python src/featurization.py data/prepared data/features


# ステージング(学習)
dvc stage add -n train \
                -p train.seed,train.n_est,train.min_split \
                -d src/train.py -d data/features \
                -o model.pkl \
                python src/train.py data/features model.pkl

# 定義完了したので、commitに良いタイミング
git add .gitignore data/.gitignore dvc.yaml
git commit -m "pipeline defined"

==================
# パイプラインの再現
# dvc.lockが作成される, データのdvcのhashになるんだろうな -> dvc pushでデータが送られる
dvc repro
dvc push
git add dvc.lock && git commit -m "first pipeline repro"

# パイプラインの可視化
dvc dag

```

#### Metrics, Plots, and Parameters

- 評価、可視化、パラメータ変更を管理できる
  - metric: [metrics | Data Version Control · DVC](https://dvc.org/doc/command-reference/metrics)
  - metric show: [metrics show | Data Version Control · DVC](https://dvc.org/doc/command-reference/metrics/show)
  - plot: [plots | Data Version Control · DVC](https://dvc.org/doc/command-reference/plots)
  - それ反復管理するには、[Get Started: Experiment Management | Data Version Control · DVC](https://dvc.org/doc/start/experiments) が便利らしい

```python
# ステージング(評価)
dvc stage add -n evaluate \
  -d src/evaluate.py -d model.pkl -d data/features \
  -o eval \ # 出力もdvc add / git add (optional) / gitignoreにadd を自動で行われる
  python src/evaluate.py model.pkl data/features

# パイプラインの再現(metricが更新される)
dvc repro
dvc push
git add .gitignore dvc.yaml dvc.lock eval
git commit -a -m "Create evaluation stage"

# ステージング(metric)
vi dvc.yaml # 下記を追記, (最上層にコピペする stageと同じ階層)
git add -A
git commit -a -m "Create metric stage"


# metricを表示する
dvc metrics show

# metricを可視化する
dvc plots show

# パラメータを更新
vi params.yaml
---
 featurize:
-  max_features: 100
-  ngrams: 1
+  max_features: 200
+  ngrams: 2
---
dvc repro
dvc push

# 更新前後を比較する
dvc params diff
dvc metrics diff
dvc plots diff
```

- [metric のカスタム](https://dvc.org/doc/start/data-management/metrics-parameters-plots#expand-to-see-how-to-customize-metrics-and-plots)
  - トレーニング・データとテスト・データを組み合わせ、タイトルなどのカスタム属性を設定するには、dvc.yaml に以下を追加する：

```yaml
metrics:
  - eval/metrics.json
plots:
  - ROC:
      template: simple
      x: fpr
      y:
        eval/plots/sklearn/roc/train.json: tpr
        eval/plots/sklearn/roc/test.json: tpr
  - Confusion-Matrix:
      template: confusion
      x: actual
      y:
        eval/plots/sklearn/cm/train.json: predicted
        eval/plots/sklearn/cm/test.json: predicted
  - Precision-Recall:
      template: simple
      x: recall
      y:
        eval/prc/train.json: precision
        eval/prc/test.json: precision
  - eval/importance.png
```

### Experiment management

- [Get Started: Experiment Management | Data Version Control · DVC](https://dvc.org/doc/start/experiments)

exp management

1. 実験のトラッキング
   1. dvc 上で各実験結果をメタ情報にして、Git はそのメタ情報を管理するだけでよくする
2. 実験のコラボレーション
   1. Git 上で実験の数値や可視化結果を共有する感じ
3. パイプラインを使った実験
   1. パラメータとハイパラを、先にステージングで作成したパイプラインに注入する

【メモ】

dvc は、

- [Get Started with DVC | Data Version Control · DVC](https://dvc.org/doc/start#following-this-guide)

1. data management
2. exp management
   ができるらしい

dvc の remote で実際にローカルのフォルダに保存する場合は、local remote というらしい、(--local フラグとは違うらしい)

remote の設定は以下で確認

```python
dvc remote list
cat .dvc/config # core/remoteの設定がdefault remote
```

dvc add したものは、まとめて一つの hash として push される

dvc checkout は、標識情報に紐づいたデータをとってくるやつ? 現在の標識と対応した正しいバージョンに合わせる

dvc は、データのメタ情報であって、バージョン管理は dvc の meta 情報を git 管理することで完了する。そのため、管理単位は git commit 単位

remote 情報を書き換える際は、`rm -f <filename.dvc>; dvc gc` で良さそう。remote にデータは残るけど、バージョン管理だと残しておくことに意味があるからいいかんじ

- [gc | Data Version Control · DVC](https://dvc.org/doc/command-reference/gc)
- `dvc gc --cloud`を指定すると、リモートのデータも削除されるらしい。指定しないと復元可能
- オプションで、保護するキャッシュ対象を決める必要がある
  - git で毎回しっかり管理している場合は、現在のプロジェクトディレクトリで参照されているキャッシュのみを保護する `--workspace`でよさそう
- DVC LIve は stage add することで、yaml を更新してくれるもの

## 参考

- [機械学習プロジェクトのデータバージョン管理ツール『DVC』の「Get Started」のサブノート #機械学習 - Qiita](https://qiita.com/meow_noisy/items/a644547930e6f2dea12d)
- [Python API Reference | Data Version Control · DVC](https://dvc.org/doc/api-reference)
- [dvc によるデータの管理をしてみた - tkherox blog](https://takaherox.hatenablog.com/entry/2020/02/24/134850)
- [GitHub - iterative/dvc: 🦉 Data Version Control | Git for Data & Models | ML Experiments Management](https://github.com/iterative/dvc)

- [Get Started with DVC | Data Version Control · DVC](https://dvc.org/doc/start)
- [Data Version Control · DVC](https://dvc.org/)

- strage 設定
  - [Remote Storage | Data Version Control · DVC](https://dvc.org/doc/user-guide/data-management/remote-storage)

## まとめ(類似点・相違点)

dvc は Git でデータを管理できるようにするためのツール

データをメタ情報にしてリモートで管理するデータと紐づけるのが dvc
そのメタ情報を git でバージョン管理することで、データをバージョン管理している。
データ/pipline を更新したら、忘れずに、dvc add と、git commit しようね

データの保存先は安全で変えることがないような場所, リモートとかの保存先にしようね
ローカルだと無駄にデータフォルダが増えてしまう。

データのサイズやファイル数が増大しても、まとめて、dvc add して 1 つの hash にすることで、Git が管理するのはほとんど変化しない

## 振り返り

commit message は `define piplne` よりは `pipline defined` の方が完了した感があって良いな

## 次回やること

[CML · Continuous Machine Learning](https://cml.dev/)
