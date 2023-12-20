# Linux

## 常用指令

- 查看linux系统版本：
    - cat /proc/version
    - cat /etc/os-release
    - uname -a

## 指令

- [df](learn_df.md)：查看linux系统服务器文件系统的磁盘使用情况

```shell
# df [选项] [FILE]
df -h . # 查看当前文件夹所在磁盘使用情况
df -h   # 查看当前机器所有磁盘使用情况
```

- [find](learn_find.md)：它将文件系统内符合条件的文件列出来

```shell
# find [path] [expression]
find . *.txt -maxdepth 2 -type f # 查看当前目录下所有的txt文件，最大搜索两层
```

- [ln](learn_ln.md)：将一个文件或目录链接到另一个位置

```shell
# ln [OPTION]... [target] [link_name]
ln test.txt hard_text.txt # 将test.txt硬链接到hard_text.txt
ln -s test.txt soft_text.txt # 将test.txt软链接到hard_text.txt
```

- [xargs](learn_xargs.md)：给其他命令传递参数的一个过滤器(主要用于参数替换，弥补有些命令不能从管道中读取数据)

```shell
# xargs [OPTION]... [COMMAND [INITIAL-ARGS]]...
# [command1] | xargs [option] [command2]
find . -type f -name "*.log" | xargs rm -f                    # 删除当前目录下所有.log文件
find . -type f -name "*.jpg" | xargs -I {} cp {} /data/images # 复制当前目录.jpg文件到/data/images
```

