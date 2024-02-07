# Python 实用小方法

## 使用字典排序
```python
_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

# 按照key值排序
_dict = {k: v for k, v in sorted(_dict.items(), key=lambda x: x[0])}
# 按照value值排序
_dict = {k: v for k, v in sorted(_dict.items(), key=lambda x: x[0])}
```

## 通过ASCII码获取所有数字和字母

```Python
# 所有大写字母
print([chr(i) for i in range(65, 91)])
# 所有小写字母
print([chr(i) for i in range(97, 123)])
# 所有数字
print([chr(i) for i in range(48, 58)])
```