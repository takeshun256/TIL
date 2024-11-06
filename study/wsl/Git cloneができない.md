start：[[2023-03-02]] 23:09

## 経緯・背景

エラー
`# [Git: Could not resolve host github.com error while cloning remote repository in git](https://stackoverflow.com/questions/20370294/git-could-not-resolve-host-github-com-error-while-cloning-remote-repository-in)`

## 参考

- https://stackoverflow.com/questions/20370294/git-could-not-resolve-host-github-com-error-while-cloning-remote-repository-in

## 内容

解決
DNS サーバーがデフォルトは違ってしまっているため。
/etc/wsl.conf をいじったら、resolv.conf の方もいじる必要があるのかも
解決記事では原因不明らしい
resolv をいじることで DNS サーバーをいじる
https://blog.cosnomi.com/posts/wsl-resolv-conf/
