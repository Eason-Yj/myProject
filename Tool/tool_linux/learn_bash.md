# Linux 常用方法和指令

## 1 重定向符( >  >>  <  << )
```
## 格式 
# 输出重定向
command > file # 覆盖写入
command >> file # 追加写入

# 输入重定向
command < file
command << file

## 常用方式
# 输出重定向
command >/dev/null # 标准输出重定向到空
command > stdout.log # 标准输出重定向到指定文件
command 2 > stderr.log # 标准错误输出重定向到指定文件
command > stdout.log 2>&1 # 标准输出和标准错误输出都重定向到 stdout.log 文件

# 输入重定向
cat < file # 将file中的内容输入给cat

```
- /dev/null 表示空设备文件
- 0 表示stdin标准输入
- 1 表示stdout标准输出
- 2 表示stderr标准错误
- \> 默认为标准输出重定向，与 1> 相同
- 2>&1 标准错误输出 重定向到 标准输出
- 1>&2 把标准输出 重定向到 标准错误输出
- \&>file 标准输出 和 标准错误输出 都重定向到文件file中
- \>&file 标准输出 和 标准错误输出 都重定向到文件file中
- 注意:默认都输出到屏幕