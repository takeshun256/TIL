start：[[2023-03-04]] 02:28

## 内容

### 基本コマンド

![[Pasted image 20230304023007.png]]
> gpt-3 で brew と tap の違いを調べた結果

### brew tap 関連

![[Pasted image 20230304023057.png]]

homebrew で標準で参照できないレポジトリがあり、それを tap で追加して選べるようにするもの
tap でレポジトリを追加して、その後、brew install する感じ
e.g.

```bash
brew tap joerdav/xc
brew install xc
```

## 類似点・相違点・まとめ

brew はインストールとそれの管理を手助けするもの

tap はマイナーなレポジトリを追加して、install できるようにするコマンド
