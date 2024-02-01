# Python 实用小方法

# 通过ASCII码获取所有数字和字母

```Python
# 所有大写字母
print([chr(i) for i in range(65, 91)])
# 所有小写字母
print([chr(i) for i in range(97, 123)])
# 所有数字
print([chr(i) for i in range(48, 58)])
```