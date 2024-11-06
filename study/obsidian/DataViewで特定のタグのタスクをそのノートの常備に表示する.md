start：[[2024-07-23]] 19:28

参考：

- [Metadata on Tasks and Lists - Dataview](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-tasks/) メタデータで取得できるものがのっている
- [【Obsidian】dataview の使い方｜六](https://note.com/6kuga0/n/n228824aec14e) dataview の基本的な使い方
- [[Dataviewの使い方を軽く見てみる]] 入門　現在のテンプレートはここがもと

以下は、TASK の`WHERE` で指定するもの

- `completed`: 完了もの
- `fullyCompleted`: サブタスクもすべて完了もの
- `!completed`: 未完了もの
- `visual`:表示文字　`contains` と合わせたらいけそうではある
- `text` : 文字　＝＞　[How to create task lists with DATAVIEW based on tags associated with individual tasks - Help - Obsidian Forum](https://forum.obsidian.md/t/how-to-create-task-lists-with-dataview-based-on-tags-associated-with-individual-tasks/29384/2)　をしようしてタグ検索できるぽい
- `tags`: タスクテキスト内のタグ list 形式　＝＞まさにこれか！

書き方

- `WHERE any(file.tasks, (t) => !t.fullyCompleted)` <= `!fully.Completed`でも OK、`file.tasks` や `file.list` が暗黙的にフィールドアクセスできるため

日付とかの短縮構文を利用するとその完了日やスケジュール日も取得可能らしい

- [Metadata on Tasks and Lists - Dataview](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-tasks/#:~:text=%E7%9F%AD%E7%B8%AE%E6%A7%8B%E6%96%87%E3%82%92,%E3%81%A6%E3%81%84%E3%82%8B%E6%97%A5%E4%BB%98%E3%80%82)

### 作ってみた

```dataview
TASK
FROM "Inbox"
WHERE file.name = this.file.name
	AND any(file.tasks, (t) => !t.fullyCompleted)
	AND contains(text, "#hello")
```

```
TASK
FROM "Inbox"
WHERE file.name = this.file.name
	AND !fullyCompleted
	AND contains(text, "#hello")
```

【メモ】

```dataviewsample
TASK from "100-daily notes"
where file.day >= date("2022-02-14")
　AND file.day <= date("2022-02-20")
　AND contains(string(section), "⭕ Things")
```

- [Metadata on Tasks and Lists - Dataview](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-tasks/)

- 現在のページの実から取り出す場合は以下を利用する

  - `WHERE file.name = this.file.name`

- [ ] => 以下をテンプレートに追加する #todo
  - [ ] おはようみってる！

```
TASK
FROM "Inbox"
WHERE file.name = this.file.name
	AND !fullyCompleted
	AND contains(text, "#todo")
```

## 振り返り

メタ情報の公式ページを見ることでより深い使い方ができるようになった
疑問点と仮説を立てて検証することが重要
適当に調べているだけだと載っていない
今回の場合は `file.tasks`の取れる値が関係していそうだと辺りをつけて調べた
