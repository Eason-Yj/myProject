# conda base

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
    - conda config --set show_channel_urls yes (channel中安装包时显示channel的url，这样就可以知道包的安装来源了)
  