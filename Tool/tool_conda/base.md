# conda base

## 安装conda

### 1 下载sh(exe)文件

下载地址：

- 官网：https://docs.conda.io/projects/miniconda/en/latest/
- 镜像源：https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/

### 2 安装

Linux：

```shell
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

macOS：

```shell
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

Linux：

```shell
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe
```

## 环境相关指令

- 创建环境：conda create --name (env_name) python=(python_version)
- 激活环境(for Windows)：activate (env_name)
- 激活环境(for Linux/Mac)：source activate (env_name)
- 删除环境：conda env remove --name (env_name)

## Python库相关指令

- 安转库：conda install (package)
- 删除库：conda remove (package)
- 升级库：conda update (package)
- 搜索库：conda search (package)
- 比对库：
    - conda compare environment.yml(比对当前环境和yml文件中的库版本)
    - conda compare -n envName environment.yml(比对envName环境和yml文件中的库版本)

## 环境导出/导入

- txt 文件 (python库的导出导入)
    - 导入：conda install --yes --file requirement.txt
    - 导出：conda list -e > requirement.txt
- yml 文件 (python环境的备份)
    - 导入：conda env create -f environment.yml
    - 导出：conda env export > environment.yml

## 环境回滚

- 查看历史安装：conda list --revisions
- 回滚到指定版本：conda install --revision=n

## 镜像源设置

- 查看镜像源：conda config --show channels
- 添加镜像源：
    - conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
    - conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    - conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle
    - conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
    - conda config --set show_channel_urls yes (channel中安装包时显示channel的url，这样就可以知道包的安装来源了)
  