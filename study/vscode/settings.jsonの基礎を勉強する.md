start：[[2023-07-28]] 17:13

### settings.json とは

エディタの動作や外観、拡張機能などの様々な側面をカスタマイズするために使用されます。このファイルに設定を追加・変更することで、個別のプロジェクトに対してカスタム設定を行ったり、複数の環境間で設定を共有したりできます。

- エディタの挙動のカスタマイズ
- 各プロジェクトごとに設定や共有が簡単にできる
- ユーザーレベル or ワークスペースレベル

-> vscode の設定をワークスペースレベルでカスタマイズ、上書きする感じ
-> プロジェクトで配布する感じ

設定内容としては、vscode の設定なので、パラメータを全て列挙するのはあまり意味がない(vscode の settings を理解することになる)
-> Python 環境のベストプラクティスなテンプレートを理解してちょっとだけカスタマイズするのが良さそう (使ううちは別にそれで良いし)

```settings.json
{
  // エディタ関連の設定
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.wordWrap": "on",

  // ファイル関連の設定
  "files.autoSave": "afterDelay",
  "files.exclude": {
    "**/.git": true,
    "**/.DS_Store": true
  },

  // 拡張機能の設定
  "extensions.autoUpdate": false,

  // ターミナル関連の設定
  "terminal.integrated.shell.osx": "/bin/bash",

  // その他の設定
  "workbench.colorTheme": "Default Light+",
  "workbench.iconTheme": "vscode-icons",
}
```

### テンプレートなど

#### 先輩の設定

```json
{
  "python.linting.pylintEnabled": false, # pylintの静的解析
  "python.linting.enabled": true, # pythonの静的解析を有効か flake8も
  "python.linting.flake8Enabled": true, # flake8の静的解析を有効
  "editor.formatOnSave": true, # ファイル保存時に自動でフォーマット
  "[python]": {
    "editor.codeActionsOnSave": { # ファイル保存時に~
      "source.organizeImports": true # 自動でimportを整理
    },
    "editor.defaultFormatter": "ms-python.autopep8" # ファイルのデフォルトフォーマッタをautopep8にする
  },
  "python.linting.flake8Args": [ # flake8の追加引数
    "--ignore=E226,E402,W503,E501", # これらのエラーを無視
    "--max-complexity=12" # 最大複雑度?を12とする
  ],
  "python.formatting.provider": "none", # 提供されるフォーマッタを無効化して、(上記のautopep8が使用される)
  "autopep8.args": ["--ignore=E226,E402,W503,E501"], # フォーマッタの追加引数
  "vetur.format.defaultFormatterOptions": { # vue.jsのprettterのオプションを指定
    "prettier": {
      "trailingComma": "es5"
    }
  }
}
```

#### その他

```json
{
  // ファイルについて
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 800,
  // エディタについて
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    // isort formatter
    "source.organizeImports": true
  },
  "files.eol": "\n",
  // yapf formatter
  "python.formatting.provider": "yapf",
  "python.formatting.yapfArgs": [
    "--style={column_limit: 84, indent_width: 4, SPLIT_BEFORE_NAMED_ASSIGNS=False}"
  ],
  // flake8 linter
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": ["--max-line-length=84"],
  "python.linting.flake8CategorySeverity.F": "Warning",
  "python.linting.flake8CategorySeverity.E": "Warning",
  "[python]": {
    "editor.defaultFormatter": "ms-python.python"
  }
}
```

#### Python 系で重要なもの

- プロジェクトによって結構異なっているが、構成は似ている
  - ファイル, エディタ, Linting, Format, Linting の詳細設定

```json
	# インタープリタの指定
{
  "python.pythonPath": "/path/to/your/python/interpreter"
}

	# Linting(静的解析)の設定
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.flake8Enabled": false,

	# フォーマッターの設定
{
  "python.formatting.provider": "black"
},

	# 自動補完とコードナビゲーションの有効化
{
  "editor.quickSuggestions": {
    "other": true,
    "comments": false,
    "strings": true
  },
  "editor.suggestSelection": "first",
  "editor.tabCompletion": "on"
}
```
