# numpy

## 1 创建数组

## 2 数组的拼接与分裂

### 2.1 concatenate(连接)

```python
import numpy as np

data1 = np.random.randint(1, 10, size=(2, 2, 2))
data2 = np.random.randint(1, 10, size=(3, 3, 3))

concatenate_exp1 = np.concatenate([data1, data2[:, :2, :2]], axis=0)  # 垂直拼接
concatenate_exp2 = np.concatenate([data1, data2[:2, :, :2]], axis=1)  # 水平拼接
concatenate_exp3 = np.concatenate([data1, data2[:2, :2, :]], axis=2)  # 深度拼接

print(concatenate_exp1.shape)  # (5, 2, 2)
print(concatenate_exp2.shape)  # (2, 5, 2)
print(concatenate_exp3.shape)  # (2, 2, 5)
```

### 2.2 stack(堆叠)

注：堆叠，结果会增加一个维度

```Python
import numpy as np

data1 = np.array([[11], [21], [31]])  # shape = (3,1)
data2 = np.array([[42], [52], [62]])  # shape = (3,1) 
res = np.stack([data1, data2], axis=0)  # 按整个数据去堆叠 shape = (2, 3, 1)
print(res.tolist())  # [[[11], [21], [31]], [[42], [52], [62]]] 
res = np.stack([data1, data2], axis=1)  # 按第1维度数据堆叠 shape = (3, 2, 1)
print(res.tolist())  # [[[11], [42]], [[21], [52]], [[31], [62]]]
res = np.stack([data1, data2], axis=2)  # 按第2维度数据堆叠 shape = (3, 1, 2)
print(res.tolist())  # [[[11, 42]], [[21, 52]], [[31, 62]]] 
```

### 2.3 vstack(垂直堆叠) & hstack(水平堆叠) & dstack(深度堆叠)

注：水平（垂直、深度）堆叠，堆叠维度不存在时会增加对应维度

```Python
import numpy as np

data1 = np.array([[11], [21], [31]])  # shape = (3,1)
data2 = np.array([[42], [52], [62]])  # shape = (3,1)

res = np.vstack([data1, data2])  # 垂直堆叠
print(res.tolist())  # [[11], [21], [31], [42], [52], [62]] shape=(6, 1)

res = np.hstack([data1, data2])  # 水平堆叠
print(res.tolist())  # [[11, 42], [21, 52], [31, 62]] shape=(3, 2)

res = np.dstack([data1, data2])  # 深度堆叠
print(res.tolist())  # [[[11, 42]], [[21, 52]], [[31, 62]]] shape=(3, 1, 2)
```

### 2.4 append

注：拼接的两个数组的维度数应该相同

```Python
import numpy as np

data1 = np.array([[11], [21], [31]])  # shape = (3,1)
data2 = np.array([[42], [52], [62]])  # shape = (3,1)

res = np.append(data1, values=np.array([[41]]), axis=0)  # 垂直拼接
print(res.tolist())  # [[11], [21], [31], [41]] shape=(4,1)

res = np.append(data1, values=data2, axis=1)  # 水平拼接
print(res.tolist())  # [[11, 42], [21, 52], [31, 62]] shape=(4,2)
```

## 其他数组用法
### 1 np.diff 计算数组中相邻值的差（计算沿给定轴的第n个离散差）
```python
import numpy as np

a = np.asarray([1, 2, 3, 5, 5])

print(np.diff(a=a, n=1, axis=0)) # [1 1 2 0]
print(np.diff(a=a, n=2, axis=0)) # [0  1 -2]
print(np.diff(a=a, n=3, axis=0)) # [1    -3]

# 参数n表示计算差值次数
```