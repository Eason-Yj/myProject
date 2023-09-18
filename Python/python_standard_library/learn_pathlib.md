# pathlib 模块

## base

- Path():Path表示文件系统路径，但与PurePath不同，它还提供对路径对象进行系统调用方法。根据当前系统，实例化Path将返回PosixPath或WindowsPath。
- PurePath():PurePath表示文件系统路径，并提供不意味着任何实际文件系统I/O的操作。根据当前系统，实例化PurePath将返回PurePoxPath或PureWindowsPath对象。

## 创建文件(夹)

````python
from pathlib import *

# 创建目录
path = Path('exp1')
path.mkdir(exist_ok=True)
# 创建多级目录
path = Path('exp1/exp1/exp1')
path.mkdir(parents=True, exist_ok=True)

# 创建文件
path = Path('exp1')
path.touch()
````

## 获取文件(夹)

```python
from pathlib import *

# 获取文件当前所在路径
Path.cwd()
# 获取电脑用户所在目录
Path.home()
# 获取文件绝对路径
Path('exp.py').absolute()
Path('exp.py').resolve()

path = Path(Path.cwd().parent)
# iterdir 获取目录下所有文件(夹)，并返回一个生成器
print([i for i in path.iterdir()])
# glob 获取目录下所有与 pattern 匹配的文件，返回一个生成器
print([i for i in path.glob('*.md')])
# rglob 获取目录下及其子目录下所有与 pattern 匹配的文件，返回一个生成器
print([i for i in path.rglob('*.md')])

path = Path('/Users/v_wangyuji/Desktop/myLearn/myProject/README.md')
path.absolute()
path.name  # 获取文件(夹)名，README.md
path.stem  # 获取文件名（不带后缀），README
path.suffix  # 返回文件后缀（目录返回空），.md
path.suffixes  # 返回文件后缀列表，[.md]
path.root  # 返回根目录
path.parts  # 返回各级文件(夹)名,('/', 'Users', 'v_wangyuji', 'Desktop', 'myLearn', 'myProject', 'README.md')
path.anchor  # 返回根目录
path.parent  # 返回上级目录，/Users/v_wangyuji/Desktop/myLearn/myProject
path.parents  # 返回所有上级目录的列表
print([i for i in path.parents])
# [PosixPath('/Users/v_wangyuji/Desktop/myLearn/myProject'), 
#  PosixPath('/Users/v_wangyuji/Desktop/myLearn'), 
#  PosixPath('/Users/v_wangyuji/Desktop'), 
#  PosixPath('/Users/v_wangyuji'), 
#  PosixPath('/Users'), PosixPath('/')]
```

## 路径拼接

```python
from pathlib import *

# 路径拼接
res = Path.joinpath(Path.cwd(), 'exp.py')
print(type(res), res)
# <class 'pathlib.PosixPath'> /Users/v_wangyuji/Desktop/myLearn/myProject/Python/python_standard_library/exp.py

res = Path(Path.cwd(), 'exp.py')
print(type(res), res)
# <class 'pathlib.PosixPath'> /Users/v_wangyuji/Desktop/myLearn/myProject/Python/python_standard_library/exp.py
```

## 判断路径

```python
from pathlib import *

path = Path('/Users/v_wangyuji/Desktop/myLearn/myProject/README.md')
print(path.exists())  # 是否存在,True
print(path.is_dir())  # 是否为文件夹,False
print(path.is_file())  # 是否为文件,True
print(path.is_mount())  # 是否为挂载,False
print(path.is_symlink())  # 是否为链接,False
print(path.is_absolute())  # 是否为绝对路径,True
print(path.match())  # 判断路径是否与匹配字符匹配,True


```

## 删除文件夹（文件）

```python
from pathlib import *

Path('exp2/').rmdir()  # 删除文件夹，文件夹需要为空
Path('exp3').unlink()  # 删除文件或链接
```

## 移动和修改文件

```python
from pathlib import *

path = Path('exp.txt')
# 重命名文件
path.rename('exp2.txt')
# 移动文件
path.rename(str(Path(Path.cwd().parent, 'python_ThirdParty_library/exp.txt')))
# 修改文件权限
path.chmod(0o777)

```