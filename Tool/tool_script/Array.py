from typing import Union
import numpy as np

TypeArray = Union[list, np.ndarray]


class arrayOperate():
    pass


def equalInterval(array: TypeArray, gap_num: int = 1, return_tuple: bool = True):
    """
    将数组等间隔切分为n个数组
    numpy.linspace | pd.cut 效果类似

    :param array:
    :param gap_num:
    :param return_tuple:
    :return:
    """
    if isinstance(array, np.ndarray):
        array = array.tolist()

    lens = len(array)
    if lens < gap_num:  # 当切分个数大于数组长度时，设置切分个数为数组长度
        gap_num = lens

    min_val = min(array)
    max_val = max(array)

    gap_val = round((max_val - min_val) / gap_num, 4)
    bins = [min_val + gap_val * i for i in range(gap_num)]
    bins.append(max_val)
    bins[0] = bins[0] - 1
    print(bins)

    res_list = []
    for i in range(1, len(bins)):
        start, end = bins[i - 1], bins[i]
        bin_list = []
        for v in array:
            if start < v <= end:
                bin_list.append(v)
        res_list.append(bin_list)
    print(res_list)


equalInterval(array=[1, 2, 3, 4, 5, 6], gap_num=3)


def specifyLength(array: TypeArray, gap_val: int = 1, return_tuple: bool = True) -> TypeArray:
    """
    将数组切分为长度为n的多个数组
    :param array:
    :param gap_val:
    :param return_tuple:
    :return: 每个子数组的起始终止样本索引
    例子：
    array = [23, 11, 98, 55, 19, 76, 18, 41, 88, 59, 88, 20, 8, 38, 83, 79, 37]
    return_tuple=False [0, 5, 10, 15, 17]
    return_tuple=True  [(0, 5), (5, 10), (10, 15), (15, 17)]
    """
    if isinstance(array, np.ndarray):
        array = array.tolist()

    lens = len(array)
    if lens <= gap_val:
        return array

    gap_list = []
    exact_division = lens // gap_val  # 整除值
    if return_tuple:
        for i in range(1, exact_division + 1):
            gap_list.append((gap_val * (i - 1), gap_val * i))
        gap_list.append((exact_division * gap_val, lens))  # 加入最后一个元素的index
    else:
        for i in range(exact_division + 1):
            gap_list.append(gap_val * i)
        gap_list.append(lens)  # 加入最后一个元素的index

    return gap_list
