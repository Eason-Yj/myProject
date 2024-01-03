# vim

## 设置
- 使用vim命令，内容出现乱码
```
# 1 修改配置文件
sudo vim /etc/vim/vimrc
# 添加一下几行
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8

# 2 在vim编辑时临时修复
:set encoding=utf-8
:set fileencodings=ucs-bom,utf-8,cp936
:set fileencoding=gb2312
:set termencoding=utf-8
```
