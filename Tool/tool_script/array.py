from typing import Union
import numpy as np

TypeArray = Union[list, np.ndarray]
X = list(np.random.randint(1, 100, 17))
X2 = np.random.randint(1, 100, size=(17, 1))


class arrayOperate():
    pass


def equalInterval(array: TypeArray, count: int = 1, return_tuple: bool = True):
    """"""
    if isinstance(array, np.ndarray):
        array = array.tolist()
    lens = len(array)
    if lens < count:
        count = lens


def specifyLength(array: TypeArray, gap: int = 1, return_tuple: bool = True) -> TypeArray:
    """
    将数组切分为固定长度的多个数组
    :param array:
    :param gap:
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
    if lens <= gap:
        return array
    gap_list = []
    exact_division = lens // gap  # 整除值
    if return_tuple:
        for i in range(1, exact_division + 1):
            gap_list.append((gap * (i - 1), gap * i))
        gap_list.append((exact_division * gap, lens))  # 加入最后一个元素的index
    else:
        for i in range(exact_division + 1):
            gap_list.append(gap * i)
        gap_list.append(lens)  # 加入最后一个元素的index

    return gap_list


# res1 = specifyLength(X, 5, False)
# res2 = specifyLength(X, 5, True)
# print(res1)
# print(res2)
# print(X)
# print([X[i[0]:i[1]] for i in res2])
#
# res1 = specifyLength(X2, 5, False)
# res2 = specifyLength(X2, 5, True)
# print(res1)
# print(res2)
# print(X2.tolist())
# print([X2[i[0]:i[1]].tolist() for i in res2])
