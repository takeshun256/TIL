start：[[2023-06-16]] 02:46

参考

- [Site Unreachable](https://ascii.jp/elem/000/004/075/4075005/)
- [WSL ディスク領域を管理する方法 | Microsoft Learn](https://learn.microsoft.com/ja-jp/windows/wsl/disk-space)

### 現在の容量設定

![[Pasted image 20230616024758.png]]

- WSL などの容量可変の仮想ハードディスクファイルは DISKPART コマンドを使うことで最大容量を増やすことが可能
- 小さくすることはできない
- どうしても小さくしたい場合には、wsl.exe でディストリビューションをファイルにエクスポート（--export オプションを使う）して、新規に作成した同一ディストリビューションにインポート（--import オプション）するしかなさそうだ。

### 設定変更

- 設定ファイル ext4.vhdx
  - ext4.vhdx は、ユーザーフォルダー以下の「Appdata\packages」にある WSL ディストリビューションのパッケージフォルダーの LocalState フォルダーに含まれている。

```powershell
# 念のためシャットダウン
$wsl.exe --shutdown

# ext4.vhdxを探す
$Get-AppxPackage "*Ubuntu*" | select packagefullname

$Get-ChildItem C:\Users\takes\AppData\Local\packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx

# 容量変更をする
$DISKPART

$select vdisk file="C:\Users\takes\AppData\Local\packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx"

# ちゃんと選択できているか確認
$detail vdisk

# 400GB=409600にする
$expand vdisk maximum=409600

# 抜ける
exit

# 一度powershellを閉じてから、ディストリビューションを指定して起動
$wsl.exe -d Ubuntu-20.04

# 容量確認(まだ繁栄はされていない)
df -h

# パーてしょんのサイズ変更
$sudo resize2fs /dev/sdc 400G

# 再度確認
df -h
exit
wsl.exe --shutdown

```

- 400GB に増えた
