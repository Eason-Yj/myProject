import numpy as np

# 创建带有初始化数值的数组
# np.zeros(shape=(2, 2))  # 0矩阵
# np.ones(shape=(2, 2))  # 1矩阵
# np.eye(N=3)  # 对角线为1的矩阵

# 获取数组中值的索引
data1 = np.array([[0, 3, 5],
                  [0, 3, 1]])
data2 = np.array([[5, 3, 6],
                  [5, 5, 7],
                  [2, 1, 8]])
data3 = np.array([[10, 18, 19],
                  [12, 13, 11],
                  [12, 12, 17]])

# #### np.where
# np.where(data == 0) # (array([0, 1]), array([0, 0]))
# np.where(data1 == 0, data2, data3)
# 当x,y不存在时返回满足condition条件的值的索引或坐标,当x，y存在时返回x中condition坐标位置的值，其他位置的值由y中对应位置的值填充

# a = np.argmax(data1, axis=1)  # 获取最大值的索引，axis=1 获取每行最大值的索引
# b = np.argmin(data1, axis=1)  # 获取最小值的索引，axis=1 获取每行最小值的索引
# c = np.argsort(data1, axis=1) # 获取排序后数组索引，axis=1 获取每行排序后的索引
# d = np.argwhere(data1 > 1)  # 获取满足条件的值的索引或坐标

