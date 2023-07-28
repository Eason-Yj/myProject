# Linux xargs 指令

```
# 格式 
[command1] | xargs [option] [command2]
xargs -a file [option] [command2]
```

## [option]

- -a "file" 从文件中读入作为标准输入
- -e(-E) "flag" ，flag必须是一个以空格分隔的标志，当xargs分析到含有flag这个标志的时候就停止。
- -p 当每次执行一个argument的时候询问一次用户。
- -n num 后面加次数，表示命令在执行的时候一次用的argument的个数，默认是用所有的。
- -t 表示先打印命令，然后再执行。
- -i(-I)，将xargs的每项名称，一般是一行一行赋值给 {}，可以用 {} 代替。
    - 例子：ls *.jpg | xargs -n1 -I {} cp {} /data/images (复制所有图片文件到 /data/images 目录下)
- -r no-run-if-empty 当xargs的输入为空的时候则停止xargs，不用再去执行了。
- -s num 命令行的最大字符数，指的是 xargs 后面那个命令的最大命令行字符数。
- -l(L) num 从标准输入一次读取 num 行送给 command 命令。
- -d delim 分隔符，默认的xargs分隔符是回车，argument的分隔符是空格，这里修改的是xargs的分隔符。
    - 例：echo "nameXnameXnameXname" | xargs -dX 输出为：name name name name
- -x exit的意思，主要是配合-s使用。
- -P 修改最大的进程数，默认是1，为0时候为as many as it can ，这个例子我没有想到，应该平时都用不到的吧。

## 例子

- 复制指定文件文件到指定目录: find . -type f -name "*.jpg" | xargs -I {} cp {} /data/images
- 删除指定文件: find . -type f -name "*.log"  | xargs rm -f
- 统计所有py文件行数: find . -type f -name "*.py"  | xargs wc -l
- 压缩指定文件到一个压缩包: find . -type f -name "*.py" | xargs tar -czvf images.tar.gz
- wget下载所有链接: cat url-list.txt | xargs wget -c