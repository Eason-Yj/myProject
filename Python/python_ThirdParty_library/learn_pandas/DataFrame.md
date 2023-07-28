# DataFrame

## 筛选出含有缺失值的行

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

## 筛选特征列

- 根据特征列筛选 DataFrame.select_dtypes(include=None, exclude=None)[source]
    - 数值类型 np.number or 'number'，例：DataFrame.select_dtypes(include=["number"])
    - object类型, object dtype columns
    - datetimes类型, use np.datetime64, 'datetime' or 'datetime64'
    - timedeltas类型, use np.timedelta64, 'timedelta' or 'timedelta64'
    - categorical类型, use 'category'
    - datetimetz类型, use 'datetimetz' (new in 0.20.0) or 'datetime64[ns, tz]'

