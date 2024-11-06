import os

# RERADME.mdのtreeを更新

tree_result = os.popen('tree').read()

# README.mdの内容を読み込み、既存のtreeを削除
with open("README.md", "r", encoding="UTF-8") as f:
    lines = f.readlines()

# 新しい内容を作成
new_lines = []
in_tree_block = False
for line in lines:
    if line.strip() == "```shell":
        in_tree_block = True
    elif line.strip() == "```" and in_tree_block:
        in_tree_block = False
    elif not in_tree_block:
        new_lines.append(line)

# 新しいtree結果を追加
new_lines.append("```shell\n" + tree_result + "\n```\n")

# README.mdを更新
with open("README.md", "w", encoding="UTF-8") as f:
    f.writelines(new_lines)
