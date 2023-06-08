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

### 2 fatal: unable to access 'https://github.com//xxx/xxx.git/': Failed to connect to github.com port 443: Timed out
```
可能是因为网络连接失败
解决1：科学上网

解决2：设置域名解析
1 查询github可访问ip
http://ping.chinaz.com/github.com
http://ping.chinaz.com/github.global.ssl.fastly.net
http://ping.chinaz.com/assets-cdn.github.com

2 修改hosts文件
文件位置：C:\Windows\System32\drivers\etc\hosts
host文件中增加：
20.205.243.166 github.com

157.240.6.35 github.global.ssl.fastly.net
157.240.18.18 github.global.ssl.fastly.net
199.59.148.229 github.global.ssl.fastly.net
199.96.58.157 github.global.ssl.fastly.net

185.199.111.153 assets-cdn.github.com
185.199.110.153 assets-cdn.github.com
185.199.109.153 assets-cdn.github.com
185.199.108.153 assets-cdn.github.com

3 刷新DNS
ipconfig /flushdns

4 若修改后开始可以使用后来又出现该问题了，需要重新查看IP是否能访问
```