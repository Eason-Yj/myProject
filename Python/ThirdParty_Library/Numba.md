# Numba

官方链接：https://numba.readthedocs.io/en/stable/index.html  
Numba是一个开源的即时编译器，可以将Python函数即时编译成机器代码，从而提供与原始语言(
如C、C++）性能相似。Numba支持CPU和GPU加速，可以直接将Python代码转换为高效的机器代码，无需手动编写繁琐的C扩展。

## 用法

### 1 加速循环

```python
import numba as nb


@nb.njit
def f_circulate(num):
    res_list = []
    res = 0
    for i in range(num):
        if i == 0 or i == 1:
            res_list.append(1)
        else:
            res = res_list[i - 1] + res_list[i - 2]
            res_list.append(res)
    return res_list


f_circulate(10000)
```

### 2 加速递归

```python
import numba as nb


@nb.jit
def f_recursive(n: int, l: list):
    if n == 1 or n == 2:
        val = 1
    else:
        val = f_recursive(n - 1, l) + f_recursive(n - 2, l)
    if len(l) <= n:
        l.append(val)
    return val


res_l = []
f_recursive(100, l=res_l)
print(res_l)
```

### 3 并行加速循环

```python
import numba as nb


@nb.njit(parallel=True)
def f_circulate1(num):
    res_list = []
    res = 0
    for i in nb.prange(num):
        if i == 0 or i == 1:
            res_list.append(1)
        else:
            res = res_list[i - 1] + res_list[i - 2]
            res_list.append(res)
    return res_list


f_circulate1(10000)
```