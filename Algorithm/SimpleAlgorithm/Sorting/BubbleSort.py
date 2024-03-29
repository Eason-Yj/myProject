"""
冒泡排序
时间复杂度：n^2
每轮迭代从左往右依次比较相邻两个数的大小，当前大后小时交换两数位置，直到没有可交换的数时，开始迭代下一轮，重复n-1轮，依次将最大的数从右开始排列。
"""
import numpy as np


def bubbleSort(sequence: list):
    lens = len(sequence)
    for i in range(lens - 1):  # 迭代n-1轮
        for j in range(lens - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence


a = list(np.random.randint(1, 100, size=15))
b = list(np.random.randint(1, 100, size=30))
c = list(np.random.randint(1, 100, size=45))

sort_a = bubbleSort(a.copy())
a.sort()

sort_b = bubbleSort(b.copy())
b.sort()

sort_c = bubbleSort(c.copy())
c.sort()

print(a == sort_a, sort_a)
print(b == sort_b, sort_b)
print(c == sort_c, sort_c)
