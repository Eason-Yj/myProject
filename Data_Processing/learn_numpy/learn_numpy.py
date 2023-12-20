import numpy as np

# 创建带有初始化数值的数组
# np.zeros(shape=(2, 2))  # 0矩阵
# np.ones(shape=(2, 2))  # 1矩阵
# np.eye(N=3)  # 对角线为1的矩阵

# 获取数组中值的索引
# data1 = np.array([[0, 1, 2, 3], [1, 2, 3, 4]])
# data2 = np.array([[2, 3, 4, 6], [3, 4, 5, 6]])
# data3 = np.array([[10, 18, 19], [12, 13, 11], [12, 12, 17]])

# #### np.where
# np.where(data == 0) # (array([0, 1]), array([0, 0]))
# np.where(data1 == 0, data2, data3)
# 当x,y不存在时返回满足condition条件的值的索引或坐标,当x，y存在时返回x中condition坐标位置的值，其他位置的值由y中对应位置的值填充

# a = np.argmax(data1, axis=1)  # 获取最大值的索引，axis=1 获取每行最大值的索引
# b = np.argmin(data1, axis=1)  # 获取最小值的索引，axis=1 获取每行最小值的索引
# c = np.argsort(data1, axis=1) # 获取排序后数组索引，axis=1 获取每行排序后的索引
# d = np.argwhere(data1 > 1)  # 获取满足条件的值的索引或坐标

# data1 = np.random.randint(1, 10, size=(2, 2))
# data2 = np.random.randint(1, 10, size=(3, 3, 3))
# data3 = np.random.randint(1, 10, size=(1, 2, 2))

# concatenate_exp1 = np.concatenate([data1, data2[:, :2, :2]], axis=0)  # 垂直拼接
# concatenate_exp2 = np.concatenate([data1, data2[:2, :, :2]], axis=1)  # 水平拼接
# concatenate_exp3 = np.concatenate([data1, data2[:2, :2, :]], axis=2)  # 深度拼接
#
# print(concatenate_exp1.shape)
# print(concatenate_exp2.shape)
# print(concatenate_exp3.shape)

# data1 = np.array([[11], [21], [31]])  # shape = (3,1)
# data2 = np.array([[42], [52], [62]])  # shape = (3,1)
# res = np.stack([data1, data2], axis=0)  # 按整个数据去堆叠 shape = (2, 3, 1)
# print(res.tolist())  # [[[11], [21], [31]], [[42], [52], [62]]]

# res = np.stack([data1, data2], axis=1)  # 按第1维度数据堆叠 shape = (3, 2, 1)
# print(res.tolist())  # [[[11], [42]], [[21], [52]], [[31], [62]]]
# res = np.stack([data1, data2], axis=2)  # 按第2维度数据堆叠 shape = (3, 1, 2)
# print(res.tolist())  # [[[11, 42]], [[21, 52]], [[31, 62]]]

# import numpy as np
#
# data1 = np.array([[11], [21], [31]])  # shape = (3,1)
# data2 = np.array([[42], [52], [62]])  # shape = (3,1)
#
# res = np.vstack([data1, data2])  # 水平堆叠
# print(res.tolist())  # [[11], [21], [31], [42], [52], [62]] shape=(6, 1)
#
# res = np.hstack([data1, data2])  # 垂直堆叠
# print(res.tolist())  # [[11, 42], [21, 52], [31, 62]] shape=(3, 2)
#
# res = np.dstack([data1, data2])  # 深度堆叠
# print(res.tolist())  # [[[11, 42]], [[21, 52]], [[31, 62]]] shape=(3, 1, 2)

# res = np.append(data1, values=np.array([[41]]), axis=0)  # 垂直拼接
# print(res.tolist())  # [[11], [21], [31], [41]] shape=(4,1)
#
# res = np.append(data1, values=data2, axis=1)  # 水平拼接
# print(res.tolist())  # [[11, 42], [21, 52], [31, 62]] shape=(4,2)

