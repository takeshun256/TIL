start：[[2023-10-08]] 02:15

### extension.json を作成

`.vscode/extensions.json` に書くことで、vscode でワークスペースを開くと recommend してくれる機能

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-azuretools.vscode-docker",
    "ms-vscode-remote.remote-containers",
    "ms-python.black-formatter",
    "charliermarsh.ruff"
  ]
}
```

### まとめてインストールする shell スクリプトを作成

```sh
#!/bin/bash

# VS Codeの拡張機能をインストールするリスト
extensions=(
    "ms-python.python"
    "ms-azuretools.vscode-docker"
    "ms-vscode-remote.remote-containers"
    "ms-python.black-formatter"
    "charliermarsh.ruff"
)

# 各拡張機能をインストール
for extension in "${extensions[@]}"; do
    code --install-extension $extension
done

echo "All extensions have been installed."

```

実行

```python
./scripts/install_vscode_extensions.sh
```
