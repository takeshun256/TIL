start：[[2023-02-04]] 00:22

## 経緯・背景

wadb は便利であるが、チーム開発は有料であったり、mlflow に比べて拡張性がないことがネックであるため、
学習コストは高いが、mlflow を個人でも使えるようになりたい。

## 参考

- GCI の動画
- [ ] https://qiita.com/c60evaporator/items/e0eb1a0c521d1310d95d
  - [ ] 他の実験管理のやつも載っているのでそれも調べてみる
  - [x] 基礎とテンプレートとロギングが豊富
- [x] https://kakakakakku.hatenablog.com/entry/2022/06/14/095437
- [ ] https://zenn.dev/sre_holdings/articles/9cc7d5ffd502ce
- [ ] https://github.com/mlflow/mlflow
- [ ] https://future-architect.github.io/articles/20200626/
- [ ] https://mlflow.org/
- [ ] tutorial #read/article
  - [ ] https://mlflow.org/docs/latest/tutorials-and-examples/tutorial.html

## 内容

### 4 つのコンポーネント

- **MLflow Tracking** : 実験管理 / ハイパーパラメータや評価メトリクスなどを記録したり比較できたりする
- **MLflow Projects** : パッケージング / 機械学習を実行するための設定情報などを再現可能にする
- **MLflow Models** : モデル化 / さまざまなデプロイツールをサポートする汎用的なモデル形式を提供する
- **MLflow Model Registry** : モデルレジストリ / レジストリとしてモデルを管理する

### 導入

```python
pip install mlflow
conda install mlflow
```

- UI でページを立ち上げる。

```bash
mlflow ui
```

### 実験手順

#### 1. 管理情報の洗い出し

1. 管理する情報の洗い出し
   1. Code Version
      1. コードのバージョン: Git レポジトリ上のバージョンを使用
   2. Start & End Time
      1. 時間情報: 記録の開始・終了
   3. Source
      1. Mlflow Project: 補足情報
         1. プロジェクト名
         2. エントリーポイント?
   4. Tags
      1. タグ情報
         1. モデルの種類・バージョン
   5. **Parameters**
      1. 実験条件: 性能に寄与するパラメータなどの条件
         1. ハイパーパラメータ
         2. クロスバリデーション設定
         3. 乱数シード
   6. **Metrics**
      1. 評価指標
         1. 評価スコア
         2. 処理時間
   7. Artifact
      1. 関連ファイル
         1. 上記以外の保存したいファイル情報
            1. CSV, 画像, pickle など

#### 2. トラッキングサーバーの用意

- ローカルで用意する
- できれば SQLite をバックエンドに挟む
- [ ] 勉強する/

必要なもの

1. トラッキングサーバー
2. バックエンド
3. アーティファクトストレージ

#### 3. エクスペリメントの用意

実験をグルーピングして、エクスペリメントを作成
エクスペリメントをまとまったものが、プロジェクト

- [ ] 手順はわからないが、以下のようなものを設定するらしい
  - [ ] [DB 設定](https://qiita.com/c60evaporator/items/e1fd57a0263a19b629d1#%E3%83%88%E3%83%A9%E3%83%83%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B5%E3%83%BC%E3%83%90%E3%83%90%E3%83%83%E3%82%AF%E3%82%A8%E3%83%B3%E3%83%89%E3%81%AE%E5%A0%B4%E6%89%80%E3%82%92%E6%8C%87%E5%AE%9A)

```python
import mlflow
# 各種パスを指定
DB_PATH = '[バックエンドとして作成したDBファイルのパス]'
ARTIFACT_LOCATION = '[Artifactストレージに指定したいパス]'
EXPERIMENT_NAME = '[指定したいエクスペリメント名]'
# トラッキングサーバ（バックエンド）の場所を指定
tracking_uri = f'sqlite:///{DB_PATH}'
mlflow.set_tracking_uri(tracking_uri)
# Experimentの生成
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
if experiment is None:
	# 当該Experiment存在しないとき、新たに作成
	experiment_id = mlflow.create_experiment( name=EXPERIMENT_NAME,
										artifact_location=ARTIFACT_LOCATION)
else: # 当該Experiment存在するとき、IDを取得
	experiment_id = experiment.experiment_id
```

#### 4. 実験結果のロギング

1. Run(1 実験の単位)の開始

```python
mlflow.start_run(experiment_id=experiment_id)
```

- Run の開始
  - `with` 文で囲むと、可読性がまし、実行エラーが出ると with 処理が終了するので便利。
    - wandb でも、エラーが起きたらロギング終了してくれたらありがたいな！
  - つまり、finish や end_run がいらなくなる。
  - with 文を抜けることで、run が終了する=エラーが発生すると with 文が終了するので実験も自動で終了してくれる。

```python
with mlflow.start_run(experiment_id=experiment_id) as run:
	# ロギング処理を記述
```

2. ロギング処理

- https://qiita.com/c60evaporator/items/e0eb1a0c521d1310d95d#2-%E3%83%AD%E3%82%AE%E3%83%B3%E3%82%B0%E3%81%AE%E5%AE%9F%E6%96%BD
-

3. Run の終了

- with 文を使用する場合は不要

```python
mlflow.end_run()
```

### コマンド説明

| 種類     | 意味                                                                 | コマンド                                                    |
| -------- | -------------------------------------------------------------------- | ----------------------------------------------------------- |
| 準備     | ExperimentID を取得                                                  | experiment_id = mlflow.create_experiment('test_exp')        |
|          | 存在するならそこから取得                                             | experiment_id = experiment.experiment_id                    |
|          | もし EXPERIMENT を生成                                               | experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME) |
|          | UI を立ち上げる                                                      | mlflow ui                                                   |
|          | UI 立ち上げ(SQlite を使用)                                           | mlflow ui --backend-store-uri sqlite:///mlruns.db           |
|          | トラッキングサーバーの指定                                           | mlflow.set_tracking_uri(tracking_uri)                       |
|          |                                                                      |                                                             |
|          |                                                                      |                                                             |
| 実験     | Start run                                                            | with mlflow.start_run(experiment_id=experiment_id) as run:  |
|          |                                                                      |                                                             |
|          |                                                                      |                                                             |
| ロギング | Parameters を記録                                                    | mlflow.log_param('x_1', 1)                                  |
|          | 複数記録                                                             | mlflow.log_params({'x_1': 1, 'x_2': 2})                     |
|          | Metrics を記録                                                       | mlflow.log_metric()                                         |
|          | 複数                                                                 | mlflow.log_metrics()                                        |
|          | Tag を記録                                                           | set_tag()                                                   |
|          | Tag を複数記録                                                       | set_tags()                                                  |
|          | Artifact を保存                                                      | log_artifact()                                              |
|          | 複数保存                                                             | log_artifacts()                                             |
|          | テキストファイルを Artifact ととして保存                             | log_text()                                                  |
|          | ndarray を画像として Artifac ととして保存                            | log_image()                                                 |
|          | matplotlib や plotly の Figure を画像として Artifact ととして保存    | log_figure()                                                |
|          | json, yaml を Artifact として保存                                    | log_dict()                                                  |
|          | sklearn の学習済みこ出るを MlflowModel 形式で Artifact として保存    | mlflow.sklearn.log_model()                                  |
|          | Pytorch の学習済みモデルを MlflowModel 形式で Artifact として保存    | mlflow.pytorch.log_model()                                  |
|          | Tensorflow の学習済みモデルを MlflowModel 形式で Artifact として保存 | mlflow.tensorflow.log_model()                               |
|          | sklearn のを自動で保存する                                           | mlflow.sklearn.autolog()をはじめに書く                      |

- mlflow.sklearn.autolog()
  - https://qiita.com/c60evaporator/items/e0eb1a0c521d1310d95d#mlflowsklearnautolog%E3%81%AE%E6%A6%82%E8%A6%81
- Pytorch にも自動ロギングがある
  - https://mlflow.org/docs/latest/tracking.html#automatic-logging
  -
