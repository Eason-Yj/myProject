# Python 用法

## 导出和导入Python安装库

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