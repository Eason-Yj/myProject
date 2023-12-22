# pandas 基础

## 1 下载

```shell
# conda
conda install pandas
# pip
pip install pandas
```

## 2 设置

### 设置展示的 dataframe

- 获取参数值：[pd.get_option(optional, value)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_option.html)
- 设置参数值：[pd.set_option(optional, value)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html)
- 恢复默认值：[pd.reset_option(optional, value)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.reset_option.html)

```python
import pandas as pd

pd.get_option('display.max_rows')  # 获取设置展示的最大行数
pd.get_option('display.max_columns')  # 获取设置展示的最大列数

pd.set_option('display.max_rows', 999)  # 设置展示的最大行数
pd.set_option('display.max_columns', 999)  # 设置展示的最大列数
pd.set_option('display.max_colwidth', 999)  # 设置展示的最大宽度
pd.set_option('display.precision', 6)  # 设置展示的小数精度
```

## 3 基础用法

### 索引用法

```Python
import pandas as pd

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [1, 2, 3]}, index=[2, 3, 4])

# reset_index：重置索引
df.reset_index(drop=True)  # 重置索引，并删除索引列
df.reset_index(names=["index"])  # 重置索引，并保存索引为新列index

# reindex：通过设置新索引去增加和减少行列，并自定义新增行列的填充值
df.reindex([2, 3, 4, 5, 6], fill_value=0)  # 设置新的行索引，并将不存的索引行用0填充
df.reindex(columns=['col1', 'col2', 'col3'], fill_value=0)  # 设置新的列索引，并将不存的列用0填充

# set_index: 使用存在的列作为新的索引
df.set_index('col1')
```

## 4 小技巧

### 交集、并集和差集

1 交集

```python
import pandas as pd

df1 = pd.DataFrame({"col1": [1, 2, 3], "col2": [1, 2, 3]})
df2 = pd.DataFrame({"col1": [3, 4, 5], "col2": [2, 3, 4]})

# 使用isin
df = df1[df1["col1"].isin(df2["col1"])] # 找到df1中存在于df2中的元素，及交集
# 使用merge
df = pd.merge(left=df1, right=df2, how="inner", on=["col1"])
```

2 差集

```python
import pandas as pd

df1 = pd.DataFrame({"col1": [1, 2, 3], "col2": [1, 2, 3]})
df2 = pd.DataFrame({"col1": [3, 4, 5], "col2": [2, 3, 4]})

# 使用isin
df1[~df1["col1"].isin(df2["col1"])] # 找到df1中不存在于df2中的元素，及df1对df2的差集
# 使用merge
df = pd.merge(left=df1, right=df2, how="left", on='col1') # 找到df1中不存在于df2中的元素，及df1对df2的差集
df = df[df['col2_y'].isna()]
```

3 并集

```python
import pandas as pd

df1 = pd.DataFrame({"col1": [1, 2, 3], "col2": [1, 2, 3]})
df2 = pd.DataFrame({"col1": [3, 4, 5], "col2": [2, 3, 4]})

# 使用isin
df = df2[~df2["col1"].isin(df1["col1"])]
df = pd.concat([df1, df], axis=0, ignore_index=True)
print(df)

# 使用merge
df = pd.merge(left=df1, right=df2, how="right", on='col1', suffixes=['_1', '_2'])
df_diff = df[df['col2_1'].isna()][['col1', 'col2_2']].rename(columns={'col1': 'col1', 'col2_2': 'col2'})
df = pd.concat([df1, df_diff], axis=0, ignore_index=True)

```

#### 其他


| 功能 | 语法                                | 其他 |
| :--- | :---------------------------------- | :--- |
| 去重 | df.drop_duplicates(subset=["col1"]) |      |
