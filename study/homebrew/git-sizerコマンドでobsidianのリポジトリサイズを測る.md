start：[[2023-11-30]] 11:02

### 導入

- レポ
  - [GitHub - github/git-sizer: Compute various size metrics for a Git repository, flagging those that might cause problems](https://github.com/github/git-sizer)

```python
brew intall git-sizer
```

### Usage

リポジトリ内で以下を実行

```python
git-sizer --verbose
```

自分のを見た感じ、path length が長いぽい？
ルートディレクトリからの、パスの長さ(ファイル名称も含む)が長いみたい
-> 日本語だからかな？
