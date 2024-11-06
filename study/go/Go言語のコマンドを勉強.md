start：[[2023-03-17]] 19:35

## 参考

https://zenn.dev/yuki0920/articles/36a8f2957b0028

- Go 言語のモデュールの話

  - https://qiita.com/yoshinori_hisakawa/items/268ba201611401ca7935
  - mod
  - 難しめ

- go の module の使いかた
  https://qiita.com/uchiko/items/64fb3020dd64cf211d4e

## 内容

### それぞれのコマンド理解

- `go mod init github.com/takeshun256/go-typing-game`
  - 適切な go.mod ファイルを作成する
- `go get <packege>`
  - パーケージを go.mod に追記する(反映する)
  - go.mod 管理用
- `go install <package>`
  - 実行可能なバイナリの形で格納する
  - あんま使わないかも?
- go mod tidy
  - go.mod の依存関係を整理する
  - 開発ではよく使う
- go mod download
  - go.mod に書かれたモデュールをダウンロードする
  -

### 手順メモ

- go mod init 　で初期化
  - 多分初期化で指定するモジュール名はなんでも良いが
  - レポジトリで管理しているなら、そのレポジトリのパスを指定するとよさそう
- go build で依存モジュールを自動インストール(import で書かれているもの)
- go list -m all で現在の依存モジュールを確認
- go get でほしいライブラリを依存に関係なく go.mod に追加
- go mod tidy 　で使われていない依存モジュールを go.mod から削除 k
