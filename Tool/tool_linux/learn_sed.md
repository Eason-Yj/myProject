# Linux sed 指令

## 指令格式
```
# 格式
sed [options] 'command' file(s)
sed [options] -f scriptFile file(s)

# 选项
-e <script> 或 --expression=<script>：以选项中的指定的script来处理输入的文本文件；
-f <script文件> 或 --file=<script文件>：以选项中指定的script文件来处理输入的文本文件；
-n 或 --quiet 或 --silent：仅显示script处理后的结果；
-i[SUFFIX] 或 --in-place[=SUFFIX]：直接修改原始文件而不产生副本

-v 帮助

# 参数
a\ # 在当前行下面插入文本。
i\ # 在当前行上面插入文本。
c\ # 把选定的行改为新的文本。
d # 删除，删除选择的行。
D # 删除模板块的第一行。
s # 替换指定字符
h # 拷贝模板块的内容到内存中的缓冲区。
H # 追加模板块的内容到内存中的缓冲区。
g # 获得内存缓冲区的内容，并根据条件进行行内全面替换。  
G # 获得内存缓冲区的内容，并追加到当前模板块文本的后面。
l # 列表不能打印字符的清单。
n # 读取下一个输入行，用下一个命令处理新的行而不是用第一个命令。
N # 追加下一个输入行到模板块后面并在二者间嵌入一个新行，改变当前行号码。
p # 打印模板块的行。
P # (大写) 打印模板块的第一行。
q # 退出Sed。
b lable # 分支到脚本中带有标记的地方，如果分支不存在则分支到脚本的末尾。
r file # 从file中读行。
t label # if分支，从最后一行开始，条件一旦满足或者T，t命令，将导致分支到带有标号的命令处，或者到脚本的末尾。
T label # 错误分支，从最后一行开始，一旦发生错误或者T，t命令，将导致分支到带有标号的命令处，或者到脚本的末尾。
w file # 写并追加模板块到file末尾。  
W file # 写并追加模板块的第一行到file末尾。  
! # 表示后面的命令对所有没有被选定的行发生作用。  
= # 打印当前行号码。  
# # 把注释扩展到下一个换行符以前。  
```



## 示例
- 打印出指定行
```shell
sed -n '10p' file.txt # 打印出第10行
sed -n '5,8p' file.txt # 打印出第5，8行
sed -n '5,/^test/p' file.txt # 打印出第5行到以test为起始的行之间的所有行
sed -n '/pattern1/,/pattern2/p' file.txt # 打印出符合pattern1和pattern2匹配规则的行之间的所有行
```

- 替换操作(参数s和g的使用)
```shell
# 替换指定行
sed '10c/new data' file.txt

# 替换指定字符
echo abcabcabcabcabcabc | sed 's/ab/AB/' # 将第一个ab替换成AB 
echo abcabcabcabcabcabc | sed 's/ab/AB/g' # 将所有的ab替换成AB
echo abcabcabcabcabcabc | sed 's/ab/AB/2g' # 从第二个ab开始替换成AB  

# 替换指定行的指定内容
sed '2,5s/ab/AB/' file.txt # 替换2-5行的第一个ab为AB
sed '2,5s/ab/AB/g' file.txt # 替换2-5行的所有ab为AB
sed '/pattern1/,/pattern2/s/ab/AB/g' file.txt  # 替换符合pattern1和pattern2匹配规则的行之间的所有行的ab为AB

# 从文件直接替换
sed 's|aa|AA|' file.txt # 替换file.txt文件中每行的第一个aa为AA 
sed 's|aa|AA|g' file.txt # 替换file.txt文件中每行的所有aa为AA

# 使用正则表达式替换 # &的使用
echo this is a test line | sed 's/\w\+/[&]/g' # 将每个单词的格式替换成[xxx]形式 [this] [is] [a] [test] [line]

# 使用一个匹配结果替换另一个匹配结果(s,\1,\2...的使用)
# 从左开始()内匹配的内容依次对应\1、\2...
echo aaaBBB111aaaBBB111aaaBBB111 | sed 's/aaa\([A-Z]\+\)/1/'
echo aaa BBB 111 | sed 's|\([a-z]\+\) \([A-Z]\+\) \([0-9]\+\)|\3 \1 \2|' 
```

- 删除操作(参数d的使用)
```
# 删除指定行
sed '2d' file.txt # 删除指定行
sed '$d' file.txt # 删除最后一行
sed '2,$d' file.txt # 删除第2至最后一行
sed '/^$/d' file.txt # 删除空白行
sed '/^run.*h$/d' file.txt 删除以run开头，h结尾的行
```

- 文件的读写操作
```shell
# 读
sed 'r file' file.txt # 读取文件所有内容

# 写
sed -n '/pattern1/w file1.txt' file2.txt # 将file2中符合pattern1匹配规则的行写入到file1中

# 插入(a,i)
sed 'a\insertData' file.txt # 在file.txt的每一行后插入insertData
sed '2a\insertData' file.txt # 在file.txt的第二行后插入insertData
sed '/pattern1/a\insertData' file.txt # 在file.txt符合pattern1匹配规则的行后插入insertData
sed 'i\insertData' file.txt # 在file.txt的每一行前插入insertData

```

- 多命令执行()
```shell
sed -e 's/Running/RUNNING/' -e 's/130m/1111111111/' file.txt
```

- 操作匹配行的下一行(n)
```shell
sed 'n; s/aa/bb/' file.txt 

sed -n 'n;p' file.txt # 打印偶数行
sed -n 'p;n' file.txt # 打印奇数行
```
