# git pick

## 1 合并单个commit

```shell
git cherry-pick <commitHash>
```

## 2 合并多个commit

```shell
git cherry-pick <HashA> <HashB>
# 合并 C 到 D 的所有提交 。提交 C 必须早于提交 D，否则命令将失败
git cherry-pick C..D
# 合并 C 到 D 的所有提交 。不包括C
git cherry-pick C^..D
```

## 3 参数

```
-e，--edit
    打开外部编辑器，编辑提交信息
-n，--no-commit 
    只更新工作区和暂存区，不产生新的提交。
-x
    提交信息的末尾追加一行(cherry picked from commit ...)，方便以后查到这个提交是如何产生的。
-s，--signoff 
    在提交信息的末尾追加一行操作者的签名，表示是谁进行了这个操作。
-m parent-number，--mainline parent-number
    如果原始提交是一个合并节点，来自于两个分支的合并，那么 Cherry pick 默认将失败，因为它不知道应该采用哪个分支的代码变动。
    -m配置项告诉 Git，应该采用哪个分支的变动。它的参数parent-number是一个从1开始的整数，代表原始提交的父分支编号。
    例：git cherry-pick -m 1 <commitHash>
```

## 4 pick 后代码冲突

```
--continue 
    解决冲突后继续pick
步骤：
    1 用户解决冲突 
    2 git add .
    3 git cherry-pick --continue

--abort
    发生代码冲突后，放弃合并，回滚到操作前的样子
    git cherry-pick --abort
    
--quit
    发生代码冲突后，退出 Cherry pick，不回到操作前的样子。
    git cherry-pick --quit
```

