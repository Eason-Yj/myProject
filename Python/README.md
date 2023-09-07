# Python 用法

## 1 Python 镜像源

* 清华：  
  https://pypi.tuna.tsinghua.edu.cn/simple
* 阿里云：  
  http://mirrors.aliyun.com/pypi/simple/
* 中国科技大学：  
  https://pypi.mirrors.ustc.edu.cn/simple/
* 华中理工大学：  
  http://pypi.hustunique.com/
* 山东理工大学：  
  http://pypi.sdutlinux.org/
* 豆瓣：  
  http://pypi.douban.com/simple/

```shell
# === 设置pip下载源 ===
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# === 设置conda下载源 ===
# 查看镜像源
conda config --show channels 
# 添加镜像源：
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --set show_channel_urls yes
# (channel中安装包时显示channel的url，这样就可以知道包的安装来源了)
```

## 2 导出和导入Python安装库

### pip

``` shell
# 导出
pip freezen > requirements.txt 
pip list --format=freeze > requirement.txt
# 导入
pip install --no-cache-dir -f requirement.txt
```

### conda

``` shell
# 导出
conda list -e > requirements.txt
# 导入
conda install --yes --file requirements.txt
```

### pipreqs

``` shell
# 安装打包库
pip install pipreqs
# 导出(当前目录下生成requirements文件)
pipreqs ./ --encoding=utf-8 --force
```