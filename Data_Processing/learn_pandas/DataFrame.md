# DataFrame

## 1 缺失值操作

### 1.1 筛选出含有缺失值的行

```python
# pandas 选出还有缺失值的行
import pandas as pd
import numpy as np

df = pd.DataFrame(dict(age=[5, 6, np.NaN, 1, 2],
                       name=['Alfred', 'Batman', '', 'asf', 'adf'],
                       toy=[None, 'Batmobile', 'Joker', 'Batmobile', 'Joker']))

# 方法一：apply
se = df.apply(lambda row: row.hasnans, axis=1)
print(df[se])

# 方法二：df.isna().any(axis=1)
print(df[df.isna().any(axis=1)])
```

## 2 特征筛选

- 根据特征列筛选 DataFrame.select_dtypes(include=None, exclude=None)[source]
    - 数值类型 np.number or 'number'，例：DataFrame.select_dtypes(include=["number"])
    - object类型, object dtype columns
    - datetimes类型, use np.datetime64, 'datetime' or 'datetime64'
    - timedeltas类型, use np.timedelta64, 'timedelta' or 'timedelta64'
    - categorical类型, use 'category'
    - datetimetz类型, use 'datetimetz' (new in 0.20.0) or 'datetime64[ns, tz]'

## 3 dataframe的拼接与分裂

### 3.1 concat (连接)

```python
import pandas as pd

df1 = pd.DataFrame(data={"a": [11, 12, 13], "b": [15, 16, 17]})
df2 = pd.DataFrame(data={"a": [21, 22, 23], "c": [25, 26, 27]})

res = pd.concat([df1, df2], ignore_index=True, axis=0, join='outer')  # 垂直拼接
print(res)

res = pd.concat([df1, df2], ignore_index=True, axis=1, join='outer')  # 水平拼接
print(res)

```

### 3.2 merge (列与列、列与索引、索引与索引合并)

```python
import pandas as pd

df1 = pd.DataFrame(data={"a": [11, 12, 13], "b": [14, 16, 17], 'd': [1, 2, 1]})
df2 = pd.DataFrame(data={"a": [11, 22, 33], "b": [11, 16, 17], "c": [25, 26, 27]})

res = pd.merge(left=df1, right=df2, how='inner', on=['b'], suffixes=['_1', '_2'])  # 通过公共列b去匹配合并
print(res)

res = pd.merge(left=df1, right=df2, how='inner', left_on='a', right_on='b')  # 通过指定列之间的相互匹配合并
print(res)

res = pd.merge(left=df1, right=df2, how='inner', left_on='a', right_index=True)  # 通过指定列和索引的匹配合并
print(res)
```

### 3.3 join (列与索引、索引与索引合并)

```python
import pandas as pd

df1 = pd.DataFrame(data={"a": [11, 12, 13], "b": [14, 16, 17], 'd': [1, 2, 3]}, index=[1, 2, 3])
df2 = pd.DataFrame(data={"a": [11, 22, 33], "b": [11, 16, 17], "c": [25, 26, 27]}, index=[0, 1, 2])

res = df1.join(df2, how='left', lsuffix='_left', rsuffix='_right')  # 通过索引合并表格
print(res)

res = df1.join(df2, how='left', on='d', lsuffix='_left', rsuffix='_right')  # 通过左表的d字段和右表的索引匹配合并表格
print(res)
```

### 3.4 append (增加一行)
```python
import pandas as pd

df1 = pd.DataFrame(data={"a": [11, 12, 13], "b": [14, 16, 17], 'd': [1, 2, 3]}, index=[1, 2, 3])

res = df1.append({"a": 11, "b": 14, 'd': 1}, ignore_index=True)
print(res)
```