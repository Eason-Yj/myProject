"""
选择排序
时间复杂度：n^2
每轮迭代都在未排序的序列中选出最小值并添加到排序后的序列后，直到迭代完n-1个元素(最后一个不用迭代)
"""
import numpy as np


def selectSort(sequence: list):
    lens = len(sequence)
    for i in range(lens - 1):
        min_idx = i
        for j in range(i, lens):
            if sequence[min_idx] > sequence[j]:
                min_idx = j
        sequence[i], sequence[min_idx] = sequence[min_idx], sequence[i]
    return sequence


a = list(np.random.randint(1, 100, size=20))
b = list(np.random.randint(1, 100, size=25))
c = list(np.random.randint(1, 100, size=30))

sort_a = selectSort(a.copy())
a.sort()

sort_b = selectSort(b.copy())
b.sort()

sort_c = selectSort(c.copy())
c.sort()

print(a == sort_a, sort_a)
print(b == sort_b, sort_b)
print(c == sort_c, sort_c)
