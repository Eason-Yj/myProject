"""
插入排序
时间复杂度：n^2
从第二个元素开始迭代，该元素依次与前面已排序的元素比较大小(从大到小比较)，将其插入到比前一个元素大比后一个元素小的位置
"""
import numpy as np


def insertSort(sequence: list):
    lens = len(sequence)
    for i in range(1, lens):
        for j in range(i - 1, -1, -1):  # 迭代已排序序列
            if sequence[i] < sequence[j]:
                if j == 0 or sequence[i] >= sequence[j - 1]:
                    sequence.insert(j, sequence.pop(i))
                    break
            else:
                break
    return sequence


def insertSort2(sequence: list):
    lens = len(sequence)
    for i in range(1, lens):
        val = sequence[i]
        j = i - 1
        while j >= 0 and val < sequence[j]:  # 将比val小的值都往右移动一位
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = val
    return sequence


def insertSort3(sequence):
    lens = len(sequence)
    for i in range(1, lens):
        current_val = sequence[i]
        j = i - 1
        while j >= 0 and current_val < sequence[j]:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = current_val
    return sequence


a = list(np.random.randint(-100, 100, size=20))
b = list(np.random.randint(-100, 100, size=40))
c = list(np.random.randint(-100, 100, size=80))

sort_a = insertSort2(a.copy())
a.sort()

sort_b = insertSort2(b.copy())
b.sort()

sort_c = insertSort2(c.copy())
c.sort()

print(a == sort_a, sort_a)
print(b == sort_b, sort_b)
print(c == sort_c, sort_c)
