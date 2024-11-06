start：[[2023-03-30]] 12:02

- Dataview は quiery とかのコードブロックを作って、いろいろな表を作成できる、
  - Vault 内の様々な情報をぬきだして整理することができるみたい
- ノートをデータベースのように扱えるプログイン

- その日作成したノートをリスト化する

```python
LIST FROM !"Daily" WHERE file.day = date(2023-03-30)
```

- できること e.g.
  - 今週新しく作ったノート
  - 1 年間更新されていないファイルの表示
- -> 今日更新したノートのリストも表示できるのか!!

- <font color="#2DC26B">tag</font>を持ちいて、データを取得したり整理することができるので、タグを活用するのが良いかも

- 直近１日を対象に、作成日と修正日のリストを表示する

```python
TABLE file.cday AS "作成日",
      file.mday AS "修正日"
FROM ""
WHERE date(today) - file.mday <= dur(7days)
SORT file.mday desc
```

```dataview
TABLE file.cday AS "作成日",
      file.mday AS "修正日"
FROM ""
WHERE date(today) - file.mday <= dur(1days)
SORT file.mday desc
```

- Inbox で今日更新したノートの一覧

```python
list
from "Inbox"
where file.mday = date(today)
sort file.mtime desc
```

```dataview
list
from "Inbox"
where file.mday = date(today)
sort file.mtime desc
```

【メモ】

## 参考

- [GitHub - blacksmithgu/obsidian-dataview: A high-performance data index and query language over Markdown files, for https://obsidian.md/.](https://github.com/blacksmithgu/obsidian-dataview)
- [Dataview](https://blacksmithgu.github.io/obsidian-dataview/)
- [Obsidian Dataview を使って同じタグの前後の記事へのリンクを作る - by goryugo](https://knowledgestuck.substack.com/p/obsidian-dataview)
- [obsidian で dataview に入門してみる - Jazz と読書の日々](https://wineroses.hatenablog.com/entry/2023/02/12/114842)
- [Obsidian でタスクの一括管理をしてみる - Jazz と読書の日々](https://wineroses.hatenablog.com/entry/2023/02/19/074212)

## まとめ(類似点・相違点)

ノートの取得や整理はとても便利

- 条件付けが簡単で便利

URL のまとめとかは別にできなそう

- 見た目を綺麗にするようなものではない
