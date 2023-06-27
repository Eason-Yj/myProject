"""
希尔排序
时间复杂度：N*logN
1 初始间隔 gap=数组长度/2
2 对间隔为gap的所有分组进行插入排序
3 缩小间隔 gap=gap/2
4 重复2、3部直到gap=1
"""
import numpy as np


def shellSort(sequence: list):
    lens = len(sequence)
    gap = lens // 2
    while gap > 0:  # 迭代每个间隔
        for group in range(gap):  # 迭代每个分组
            group_idx_list = list(range(group, lens - gap, gap))
            for i in range(1, len(group_idx_list)):
                for j in range(i - 1, -1, -1):  # 迭代已排序序列
                    if sequence[group_idx_list[i]] < sequence[group_idx_list[j]]:
                        if group_idx_list[j] == 0 or sequence[group_idx_list[i]] >= sequence[group_idx_list[j - 1]]:
                            sequence.insert(group_idx_list[j], sequence.pop(group_idx_list[i]))
                            break
                    else:
                        break
        gap = gap // 2
    return sequence


def shellSort(input_list):
    # 希尔排序：三重循环，依次插入，直接插入法的优化版
    l = input_list  # 简化参数名
    gap = len(l) // 2  # 长度取半
    while gap > 0:
        for i in range(gap, len(l)):
            insert_value = l[i]  # 终止条件
            j = i
            while j >= gap and insert_value < l[j - gap]:
                l[j] = l[j - gap]
                j -= gap
            if j != i:
                l[j] = insert_value  # 循环终止，插入值
        gap //= 2
    return l





def shellSort(sequence):
    gap = len(sequence) // 2
    while gap > 0:
        for i in range(gap, len(sequence)):
            current_val = sequence[i]
            j = i
            while j >= gap and current_val < sequence[j - gap]:
                sequence[j] = sequence[j - gap]
                j -= gap
            sequence[j] = current_val
        gap = gap // 2
    return sequence

a = list(np.random.randint(1, 100, size=20))
b = list(np.random.randint(1, 100, size=30))
c = list(np.random.randint(1, 100, size=40))

sort_a = shellSort(a.copy())
a.sort()

sort_b = shellSort(b.copy())
b.sort()

sort_c = shellSort(c.copy())
c.sort()

print(a == sort_a, sort_a)
print(b == sort_b, sort_b)
print(c == sort_c, sort_c)