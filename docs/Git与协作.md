# Git 与协作笔记

## 常用命令

| 命令 | 作用 |
| --- | --- |
| `git clone` | 克隆仓库 |
| `git add` | 暂存修改 |
| `git commit` | 提交 |
| `git push` | 推送到远程 |
| `git pull` | 拉取远程更新 |

## 分支工作流

1. `git checkout -b feature/xxx` 新建分支
2. 开发并提交
3. `git push origin feature/xxx`
4. 发起 Pull Request 合并到 main
