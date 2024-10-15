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

## 获取时间

```python
from datetime import datetime
import time

# 方法一：获取当前时间
current_time = datetime.now()
print(current_time)  # 2024-06-04 11:13:56.885244

# 方法二：获取当前时间并格式化为指定字符串格式
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(current_time)  # 2024-06-04 14:25:53

# 方法三：获取当前时间并返回可读字符串形式
current_time = time.ctime()
print(current_time)  # Tue Jun  4 14:25:53 2024
```