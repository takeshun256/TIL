start：[[2023-11-12]] 12:36

## 経緯・背景・興味・目標

[[ConnectX]] を強化学習イベントで勉強する中で実験管理をしてみたくなったため。

[Getting started | Hydra](https://hydra.cc/docs/intro/)

[GitHub - facebookresearch/hydra: Hydra is a framework for elegantly configuring complex applications](https://github.com/facebookresearch/hydra)

[勉強用レポ](https://github.com/takeshun256/hydra-study)

### installation

```python
pip install hydra-core --upgrade
```

### Basic Tutorial

- [A simple command-line application | Hydra](https://hydra.cc/docs/tutorials/basic/your_first_app/simple_cli/)

#### 基本

**構造**

```python
├── conf
│   ├── config.yaml
│   ├── db
│   │   ├── mysql.yaml
│   │   └── postgresql.yaml
│   └── __init__.py
└── my_app.py
```

**書き方**

- hydra はからの cfg オブジェクトを作成し、デコレータで annotated された関数に渡す

```python
from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None)
def my_app(cfg: DictConfig) -> None:
print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
my_app()
```

**config.yaml 例**
して、それのディレクトリとファイル名をデコレータで渡す

- config.yaml

```python
db:
  driver: mysql
  user: omry
  password: secret
```

**my_app.py 例**

```python
from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None, config_path=".", config_name="config")
def my_app(cfg):
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()
```

-> my_app を実行すると自動で指定した config が読み込まれる

**設定の上書きも可能**

- ++で config が設定されていない場合でも設定可能
- ++という prefix なしの場合は、設定されていない場合に設定可能

```python
# Override an existing item
$ python my_app.py ++db.password=1234

# Add a new item
$ python my_app.py ++db.timeout=5
```

**config グループ**

- config は階層表記が可能で、その時のディレクトリを config パッケージと呼び、設定方法は以下の通り
- `+GROUP=OPTION`
- 設定方法は、config,yaml の defaults/db/...で設定するのかな
- primary 設定とかで上書きができるようになるので、全てグルーピングした方が良いらしい-> primary だけ conf 下に置く

```python
├─ conf
│  └─ db
│      ├─ mysql.yaml
│      └─ postgresql.yaml
└── my_app.py
------

$ python my_app.py +db=postgresql db.timeout=20
db:
  driver: postgresql
  pass: drowssap
  timeout: 20
  user: postgres_user
```

**デフォルトを設定**

- `defaults..`で設定する
  - なにも cmd で設定しない場合は、defaults の conf が選択される

```python
defaults:
  - db: mysql

# cmdで+オプションなしでoverride可能
$ python my_app.py db=postgresql db.timeout=20
db:
driver: postgresql
pass: drowssap
timeout: 20
user: postgres_user

# ~でデフォルトの削除も可能 ({}で上書きしている感じ?)
$ python my_app.py ~db
{}
```

**プライマリーコンフィグと、デフォルトコンフィグの話**

- primary = confg.yaml
- not primary = db/mysql.yaml 等
- 最後の設定された設定が優先される

```python
# primaryが優先-> db.user = root
defaults:
  - db: mysql
  - _self_

db:
  user: root

# not primaryが優先 -> db = mysql
defaults:
  - _self_
  - db: mysql

db:
  user: root
```

**MultiRun して、実験を sweep する**

- config に書かれているすべての組み合わせ or cmd で設定したもの全てを実行する(sweep)
- 性能評価する時などで使用される
- cmd から`hydra.mode=MULTIRUN`で設定する

- multirun を cmd で設定

```python
$ python my_app.py hydra.mode=MULTIRUN db=mysql,postgresql schema=warehouse,support,school
# -> 2x3 = 6通り実行

# もしくは引数で設定も可能 (--multirun, -m)
$ python my_app.py --multirun db=mysql,postgresql schema=warehouse,support,school
```

- sweeper.params を config ファイル上で override することでも設定可能

```python
hydra:
  sweeper:
    params:
      db: mysql,postgresql
      schema: warehouse,support,school

# -mでmutirunにすると、sweeperで設定されたものを全て実行, cmdで上書きは可能
$ python my_app.py -m db=mysql
# 1x3 -> 3通り


# sweeperで設定可能なやり方
x=range(1,10) # 1-9
schema=glob(*) # warehouse,support,school
schema=glob(*,exclude=w*) # support,school
```

-> sweeper は plugin とかでも詳しく設定可能

- [Ax Sweeper plugin | Hydra](https://hydra.cc/docs/plugins/ax_sweeper/)

**出力ディレクトリ設定**

- カレントディレクトリに outputs フォルダが作成されてそこに log が保存される
- 日付順
- 保存先
  - .hydra に保存されるもの
    - config.yaml
      - ユーザーが指定したものの dump
    - hydra.yaml
      - hydra の設定の dump
    - overrides.yaml
      - 使用されたコマンドラインオーバーライド
  - メインディレクトリに
    - my_app.log

![[Pasted image 20231112142412.png]]

- 設定で、`hydra.job.chdir=True` と設定すると、ワーキングディレクトリが実行時に、outputs/.../... の場所に移動するのでもし、実行時に相対パスを指定している場合は、直接保存できたりする
  - [Output/Working directory | Hydra](https://hydra.cc/docs/tutorials/basic/running_your_app/working_directory/#automatically-change-current-working-dir-to-jobs-output-dir)

**logging**

- [Logging | Hydra](https://hydra.cc/docs/tutorials/basic/running_your_app/logging/)
  設定は実行ファイルに書けば良い、INFO レベルを出力する

```python
import logging
from omegaconf import DictConfig
import hydra

# A logger for this file
log = logging.getLogger(__name__)

@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(_cfg: DictConfig) -> None:
    log.info("Info level message")
    log.debug("Debug level message")

if __name__ == "__main__":
    my_app()
```

logger の詳細を指定するのは cmd から

```python
$ python my_app.py
# [2023-11-12 14:36:24,136][__main__][INFO] - Info level message

# DEBUGも出力する
$ python my_app.py hydra.verbose=true

# [2023-11-12 14:40:02,397][HYDRA] Hydra 1.3.2
# [2023-11-12 14:40:02,398][HYDRA] ===========
# [2023-11-12 14:40:02,398][HYDRA] Installed Hydra Plugins
# [2023-11-12 14:40:02,398][HYDRA] ***********************
# [2023-11-12 14:40:02,398][HYDRA]        ConfigSource:
# [2023-11-12 14:40:02,398][HYDRA]        -------------
# [2023-11-12 14:40:02,398][HYDRA]                FileConfigSource
# [2023-11-12 14:40:02,398][HYDRA]                ImportlibResourcesConfigSource
# [2023-11-12 14:40:02,398][HYDRA]                StructuredConfigSource
# [2023-11-12 14:40:02,398][HYDRA]        CompletionPlugin:
# [2023-11-12 14:40:02,398][HYDRA]        -----------------
# [2023-11-12 14:40:02,398][HYDRA]                BashCompletion
# [2023-11-12 14:40:02,398][HYDRA]                FishCompletion
# [2023-11-12 14:40:02,398][HYDRA]                ZshCompletion
# [2023-11-12 14:40:02,398][HYDRA]        Launcher:
# [2023-11-12 14:40:02,398][HYDRA]        ---------
# [2023-11-12 14:40:02,398][HYDRA]                BasicLauncher
# [2023-11-12 14:40:02,398][HYDRA]        Sweeper:
# [2023-11-12 14:40:02,398][HYDRA]        --------
# [2023-11-12 14:40:02,398][HYDRA]                BasicSweeper
# [2023-11-12 14:40:02,398][HYDRA]
# [2023-11-12 14:40:02,398][HYDRA] Config search path
# [2023-11-12 14:40:02,398][HYDRA] ******************
# [2023-11-12 14:40:02,450][HYDRA] | Provider | Search path
# ....

# loggerで何も出力しない
$ python my_app.py hydra/job_logging=disabled
$
```

**debugging**

- config.yaml とか hydra.yaml とかに書かれている内容を出力するぽい

```python
# 実行せずに、config.yamlで設定したcfgだけ出力
$ python my_app.py --cfg job

# hydraの設定だけ
python my_app.py --cfg hydra

# どちらも
python my_app.py --cfg all

# 表示するsubsetを指定(hydra設定は結構長いため)
python my_app.py --cfg hydra --package hydra.job

# ディレクトリ構造とか色々(便利)
# [Debugging | Hydra](https://hydra.cc/docs/tutorials/basic/running_your_app/debugging/#info)
python my_app.py --info
```

![[Pasted image 20231112144827.png]]

**tab 補完**

- [Tab completion | Hydra](https://hydra.cc/docs/tutorials/basic/running_your_app/tab_completion/)
- 今入らなそう, config で色々実験したいだけだし...

```python
# autoload -U compinit && compinit # これでも良さそうだけど...下の方が良さそう
autoload -Uz bashcompinit && bashcompinit
```

#### まっさらな例

- [Using the config object | Hydra](https://hydra.cc/docs/tutorials/basic/your_first_app/using_config/)

```python
# conf/config.yaml
node:                         # Config is hierarchical
  loompa: 10                  # Simple value
  zippity: ${node.loompa}     # Value interpolation
  do: "oompa ${node.loompa}"  # String interpolation
  waldo: ???                  # Missing value, must be populated prior to access

---------------------
# my_app.py
from omegaconf import DictConfig, OmegaConf
import hydra

@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg: DictConfig):
    assert cfg.node.loompa == 10          # attribute style access
    assert cfg["node"]["loompa"] == 10    # dictionary style access

    assert cfg.node.zippity == 10         # Value interpolation
    assert isinstance(cfg.node.zippity, int)  # Value interpolation type
    assert cfg.node.do == "oompa 10"      # string interpolation

    cfg.node.waldo                        # raises an exception

if __name__ == "__main__":
    my_app()

----------------------
# 実行結果, 設定のおかしい waldo呼び出しでエラー
╰─ python my_app.py                                                                                                                                    ─╯
Error executing job with overrides: []
Traceback (most recent call last):
  File "/Users/takeshitashunji/Programming/Python/py_study/hydra-study/tutorial/my_app.py", line 13, in my_app
    cfg.node.waldo                        # raises an exception
omegaconf.errors.MissingMandatoryValue: Missing mandatory value: node.waldo
    full_key: node.waldo
    object_type=dict

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.

----------
# outputができるらしい
.
├── conf
│   └── config.yaml
├── my_app.py
└── outputs
    └── 2023-11-12
        └── 13-18-27
            └── my_app.log
```

#### 構造の書き方

- [Introduction to Structured Configs | Hydra](https://hydra.cc/docs/tutorials/structured_config/intro/)

- Pyhton の DataClass や Omegaconf を使用することで、config ファイルに書かずにそのまま入力できる
  - テストとか、設定ファイルを書く前に実験で書くときに使用するかも

```python
# データクラスをConfigStoreで、nodeをconfigグループとして設定する
from dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from omegaconf import DictConfig, OmegaConf
import hydra


@dataclass
class PostgresSQLConfig:
    driver: str = "postgresql"
    user: str = "jieru"
    password: str = "secret"

cs = ConfigStore.instance()
# Registering the Config class with the name `postgresql` with the config group `db`
cs.store(name="postgresql", group="db", node=PostgresSQLConfig)

@hydra.main(version_base=None, config_path="conf")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()

```

![[Pasted image 20231112150822.png]]

- config が複数階層になる時は、クラスを階層にすることで対応
  - [A hierarchical static configuration | Hydra](https://hydra.cc/docs/tutorials/structured_config/hierarchical_static_config/)
  - あと色々なグループとかをベタ書きする場合の書き方
    - [Config Groups | Hydra](https://hydra.cc/docs/tutorials/structured_config/config_groups/)
    - yaml ファイルで管理するしいらないかも
- db グループとかではなく、config をそのまま設定したい場合は、name=config にする

#### 実戦での使用を考える

![[Pasted image 20231112153558.png]]

- cnn や rnn を使った方法
  - [Hydra ディレクトリ構造](https://chat.openai.com/share/77819538-2adb-4b4d-9613-eaa19d7703f0)
  - 各実験ようにパラメータを別々に指定して、
  - train ファイルを 1 つ持ち学習すれば良い

【メモ】

- [Getting started | Hydra](https://hydra.cc/docs/intro/)

  - hydra は、conf ファイルを main 関数で conf 引数で読み込んで、hydra でコレー他をつけることで、自動でその conf から読み出しできる。
  - hydra 自体は、conf を別途置けるようにして、デコレー多自動読み出しをできるようにしたものか
  - conf は cmd で override できる
  - 複数の yaml 設定を読みだせて(db や port 設定)、multi job で複数回回せる

- placeholder は、仮の関数 - my_app みたいな example の例で挿入されるやつ - あとで置き換えられるよ

  > . The my_app function is a placeholder for your code.

- config ファイルのような composition 用のファイルがなければ、12 個の実験を実施する場合に 12 個の設定ファイルが必要であるが、hydra は、パラメータを 12 個列挙すれば良い、しかもパラメータによって、組み合わせをそれぞれ設定すれば良い

- 基本 primary で設定を 1 つに管理して、デフォルトでデフォルトの設定を記載する。そして、任意の組み合わせについてターミナルで指定すれば任意の設定で実験可能

  - -> 設定一覧を作れて、ターミナルで簡単に指定できるようになる。あとのループ処理とかは shell スクリプトに任せれば良い, log ファイルが出てくるのもいいね

- hydra は基本 Siri アライズして並列実行するらしい Launcher で検索?

- python の logging はセットアップに時間がかかるので、hydra の logging を使う良さそう

  - だから、実験管理だと logging が設定されているのか...
  - python の logging 使いづらすぎて触っていなかったから重要性理解できていなかったわ

- `version_base=None`が良いらしい

  - 互換性の警告をなくすため

- hydra は、型チェックや、attriberror の出力してくれる

  - [Minimal example | Hydra](https://hydra.cc/docs/tutorials/structured_config/minimal_example/)
  - config 周りの設定は描きやすそう

- 設定ファイルを共通にしたり継承上書きするやつ

  - @マークとかを試乗する
  - [Configuring Experiments | Hydra](https://hydra.cc/docs/patterns/configuring_experiments/)

- config プラグイン
  - [Configuring Plugins | Hydra](https://hydra.cc/docs/patterns/configuring_plugins/)
  - primary config を上書きしたら、別々にかけたりする

## 参考

[5 分でできる Hydra によるパラメーター管理 #Python - Qiita](https://qiita.com/Isaka-code/items/3a0671306629756895a6)

Overview

- [Overview | Hydra](https://hydra.cc/docs/configure_hydra/intro/)

## まとめ(類似点・相違点)

hydra は、設定を別ファイルにまとめて、複数実行や簡単な指定で実験の実行とログを残すことができる。

用意するのは、パラメータを指定できる関数と、config ファイル, db とか使用する場合は、グルーピングして、グループごとに階層したファイルを作成する

デメリット

- パラメータごとの結果の比較とかは対応していない。可視化も
- logger も log ファイルに出力するだけ

メリット

- 実験設定を yaml ファイルで管理するのが仕事

## 振り返り

結構学ぶことは少なめだし、設定する yaml とデコレー他を設定する関数を用意すれば全て OK
あとは、モデルとかそれぞれのパラメータを指定できるようのスクリプト形式にして管理すれば OK
