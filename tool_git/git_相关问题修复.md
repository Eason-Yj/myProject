# 问题修复

### 1 Your branch and 'origin/main' have diverged, and have 1 and 1 different commits each, respectively.
```
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

# 1 先拉取合并本地和远程的分支
git pull --rebase 

# 2 执行上面语句后可能出现下面情况：需要手动去解决冲突

First, rewinding head to replay your work on top of it...
Applying: Huggingface1
Using index info to reconstruct a base tree...
M       python_note/README.md
Falling back to patching base and 3-way merge...
Auto-merging python_note/README.md
CONFLICT (content): Merge conflict in python_note/README.md
error: Failed to merge in the changes.
Patch failed at 0001 Huggingface1
hint: Use 'git am --show-current-patch' to see the failed patch

Resolve all conflicts manually, mark them as resolved with
"git add/rm <conflicted_files>", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".

# 3 重新add
git add python_note/README.md

# 4 继续rebase
git rebase --continue

git push
```


