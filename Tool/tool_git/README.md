# Git

## git 流程示例

![Alt pic](images/git_process.png)

## 常用指令


| 功能               | 指令                                                          | 其他 |
| :----------------- | :------------------------------------------------------------ | :--- |
| 拉取远程分支到本地 | git checkout -b dev(本地分支名称) origin/zhaowk(远程分支名称) |      |
| 工作区提交到暂存区 | git add xxx |      |
| 暂存区提交到本地仓库 | git commit -m "xxx" |      |
| 本地仓库推送到远程仓库 | git push |      |
| 远程仓库拉取到本地仓库 | git pull |      |
| 本地仓库回退到暂存区 | git reset --soft HEAD^1 (file) | 可以指定回退多少个提交节点前(或具体文件) |
| 本地仓库回退到工作区 | git reset --mixed HEAD^1 (file) | 可以指定回退多少个提交节点前(或具体文件) |
| 本地仓库回退到原文件 | git reset --hard HEAD^1 (file) | 可以指定回退多少个提交节点前(或具体文件) |
| 暂存区回退到工作区 | git reset HEAD^1 (file) | 可以指定回退多少个提交节点前(或具体文件) |
| 暂存区回退到原文件 | git checkout | 可以指定回退具体文件 |

## 功能详解

- [git_撤销修改](git_撤销修改.md)
- [cherry-pick](cherry-pick.md)
