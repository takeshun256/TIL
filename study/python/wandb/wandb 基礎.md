start：[[2023-01-27]] 15:06

## 経緯・背景

コードを実験管理する際に、wandb で一括で実験設定を保存したり、ロスや精度曲線を簡単に保存できると思ったため。

## 参考

- kaggle
  - https://www.kaggle.com/code/fujino15rin/fork-of-train-deberta-v3-base
- https://wandb.ai/home
- https://www.youtube.com/watch?v=G7GH0SeNBMA&list=PLD80i8An1OEGajeVo15ohAQYF1Ttle0lk
- https://www.wandb.courses/courses/take/effective-mlops-model-development/lessons/40025747-welcome-to-the-course
- https://github.com/MLHPC/wandb_tutorial#%E3%81%BE%E3%81%9A%E3%81%AF%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B
- https://docs.wandb.ai/ref/python/init
- https://note.com/npaka/n/ne1e5112a796a

## 内容

wandb に config が保存されるため、config ファイルを保存しなくても良い

- 役割分担
  - wandb.config で一度はじめに設定した config を入力し、後から config に追加されるのは追わない。wandb.log で出力などを追う
  1.  wandb.init で初期化
  2.  wandb.config でハイパラ追加
  3.  wandb.log で出力追加

流れ

1. import
   1. pip install wandb
   2. import wandb
2. login
   1. wanb.login()
3. init
   1. ついでに config を保存
   2. `wandb.init()`
      1. `project="project_name"`：プロジェクトを作成
      2. `config =hyperparams`: ハイパーぱラムを辞書で登録
      3. `name = 実行名`: 実行ごとに名前がつく
      4. `notes=備考`
4. config
   1. config = wand.config：wandb に渡す
   2. (wandb.init(config) で入力したらこの工程はいらない)
5. log
   1. 辞書形式で保存
   2. `wandb.log({dict})`
   3.
6. finish
   1. wandb.finish()

- `wandb.watch(model)` で勾配とかを記録してくれる(任意)

実装としては

```python
!pip install wandb
wandb.login()
wandb.init({config})
config = wandb.config
wandb.log({dict})
wandb.log({dict})
wandb.finish()
```

## メモ

colab で出力させないマジックオプション
`%%capture`

h5 という大規模なメタデータなどを保存する拡張子がある。
h5py とかで読み込みする。

- 使用例
  - https://note.com/npaka/n/ne1e5112a796a
- wandb 上に保存されていないときは、反映が遅れちる可能性があるので、reload すると表示されたりする。

複数の log をまとめるときは y 軸に文字を入力するとサジェストされる
![[Pasted image 20230127173629.png]]

- fold を比べたいときは、epoch を共通で保存する
  - https://kumpei.ikuta.me/wandb-kfold/
  -
