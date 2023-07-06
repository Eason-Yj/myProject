# pandas 基础

## 下载

```shell
# conda
conda install pandas
# pip
pip install pandas
```

## 设置

### 设置展示的 dataframe

- 获取参数值：[pd.get_option(optional, value)](
  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_option.html)
- 设置参数值：[pd.set_option(optional, value)](
  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html)
- 恢复默认值：[pd.reset_option(optional, value)](
  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.reset_option.html)

```python
import pandas as pd

pd.get_option('display.max_rows')  # 获取设置展示的最大行数
pd.get_option('display.max_columns')  # 获取设置展示的最大列数

pd.set_option('display.max_rows', 999)  # 设置展示的最大行数
pd.set_option('display.max_columns', 999)  # 设置展示的最大列数
pd.set_option('display.max_colwidth', 999)  # 设置展示的最大宽度
pd.set_option('display.precision', 6)  # 设置展示的小数精度
```
