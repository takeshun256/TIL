start：[[2023-10-09]] 15:16

### 例

土曜 0 時：`'0 0 * * 6'`
日曜 0 時：`'0 0 * * 0'`

```python
*     *     *   *    *        <command to be executed>
-     -     -   -    -
|     |     |   |    |
|     |     |   |    +----- day of week (0 - 6) (Sunday=0)
|     |     |   +------- month (1 - 12)
|     |     +--------- day of month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)

```

### 作成したもの(参考)

- Actions が repository を書き換える設定が必要

```python
name: Weekly Tag

on:
  schedule:
    - cron: '0 0 * * 5'  # Run every Friday at 00:00
  workflow_dispatch:

jobs:
  create-tag:
    runs-on: ubuntu-latest

    steps:
    - name: Check out code
      uses: actions/checkout@v2

    - name: Set tag name
      id: getdate
      run: echo "date=$(date +'%Y%m%d')" >> "$GITHUB_OUTPUT"

    - name: Set committer information
      run: |
        git config user.email ""
        git config user.name ""

    - name: Create or update tag
      run: |
        git tag -fa ${{ steps.getdate.outputs.date }} -m "Weekly tag"
        git push origin :refs/tags/${{ steps.getdate.outputs.date }}
        git push origin ${{ steps.getdate.outputs.date }}

```
