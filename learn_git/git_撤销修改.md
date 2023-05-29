# 撤销和恢复修改

## 1 工作区代码修改了，但还未add
```
git checkout -- Huggingface/p3/exp.py # 用暂存区的代码替换工作区的代码
```

## 2 add了，但还没commit
```
git reset HEAD Huggingface/p3/exp.py # 回退到未add状态
git reset --mixed HEAD Huggingface/p3/exp.py
```

## 3 commit了，但还没push
```
git reset HEAD^1 # 回退到未add状态
git reset --soft HEAD^1 # 回退到未commit状态
git reset --hard HEAD^1 # 回退到未修改状态
```