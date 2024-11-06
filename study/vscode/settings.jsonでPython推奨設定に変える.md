start：[[2023-08-27]] 04:09

### TL;DR

[[2024-07-20]]

- 動作確認済み
- vscode の拡張機能で flake8 と black-formmter を導入
- `.vscode/settings.json` に以下を記載 => OK

```python
{
    "flake8.args": [
      "--ignore=E203, E501, W503",
      "--max-complexity=12",  //
      "--max-line-length=88",  // max line length
    ],
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true,
      },
      // コードナビゲーションが充実するPylanceの設定
      "python.analysis.typeCheckingMode": "off",
      //Blackの設定
      "black-formatter.args": [
        "--line-length=88"
      ],
}
```

### 内容

#### vscode で Flake8 が Vscode のワーキングディレクトリの設定を読み取るようにする。

- インタープリタが想定した仮想環境に設定されているか確認する
  ![[Pasted image 20230827023200.png]]

- settings.json で非推奨になっているものを変更する
  - [[Python / linting] 最近の VSCode linting の設定方法（2023/08/04） - Qiita](https://qiita.com/siruku6/items/6a8412c41616b558df66)

dev パッケージとして必要なくなるのか!

注意点として、拡張機能は Python ファイルが開かれると自動で発動するらしいので、必要以上に入れないことと、設定は settings.json で適宜行うことにする

- グローバルに有効化がずっとされている感じ
- 無効化は、グローバル無効化か、ワークスペース無効化する

- 設定の仕方
  - ワークスペースでギアボタンで、ワークスペース内で無効化するようにする。
    - settings.json では原則設定できないらしい
    - flake8 を入れたら pylint はグローバル無効化でも良さそう
    - pylint 無効化
      - [VSCode の Python 開発環境で pylint の代わりに flake8 を導入し自動整形を設定する - Qiita](https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb)
- - 各拡張機能の設定は、マーケットプレースで見れる！！！
    - [Site Unreachable](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)

###### pylance, pylint の解決困難なエラー

![[Pasted image 20230827034626.png]]

```python
    // コードナビゲーションが充実するPylanceの設置え
    "python.analysis.typeCheckingMode": "off",
```

pylint でも同様のエラーが出て解決不可

- pylance + flake8 + black
  - flake8, pylance, black の拡張機能を有効にする
  - 以下の json をワークスペースないの.vscode/settings.json に記載

```json
{
  "flake8.args": [
    "--ignore=E203, E501, W503",
    "--max-complexity=12", //
    "--max-line-length=88" // max line length
  ],
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
  },
  // コードナビゲーションが充実するPylanceの設定
  "python.analysis.typeCheckingMode": "off"
}
```
