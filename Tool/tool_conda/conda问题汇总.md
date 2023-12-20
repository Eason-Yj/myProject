# conda 问题汇总

RemoveError: 'requests' is a dependency of conda and cannot be removed from conda's operating environment

```shell
# 触发情况：使用conda更新 conda 或 linux、gcc相关的库时可能会触发
# 解决办法：可在更新指令前先执行：
conda update --force conda 
conda install xxx
```

RemoveError: This operation will remove conda without replacing it with another version of conda.

```shell
# 触发情况：使用conda的base环境去更新Python版本时可能会触发
# 解决办法：重新使用miniconda安装一个新Python环境
```