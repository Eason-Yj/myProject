"""
二分查找法
"""


def binary_search(array, target_val, start_idx=0, end_idx=None):
    """
    递归
    Parameters
    ----------
    array
    target_val
    start_idx
    end_idx

    Returns
    -------

    """
    if end_idx is None:
        end_idx = len(array) - 1
    mid_idx = int(((start_idx + end_idx) / 2))

    if mid_idx == start_idx or mid_idx == end_idx:
        raise ValueError("数组中不存在目标值！")

    if target_val == array[mid_idx]:
        return mid_idx
    elif target_val == array[start_idx]:
        return start_idx
    elif target_val == array[end_idx]:
        return end_idx
    else:
        if target_val < array[mid_idx]:
            return binary_search(array=array, target_val=target_val, start_idx=start_idx, end_idx=mid_idx)
        elif target_val > array[mid_idx]:
            return binary_search(array=array, target_val=target_val, start_idx=mid_idx, end_idx=end_idx)


def binary_search2(array, target_val):
    """
    循环
    Parameters
    ----------
    array
    target_val

    Returns
    -------

    """
    start_idx = 0
    end_idx = len(array) - 1
    while True:
        mid_idx = int(((start_idx + end_idx) / 2))
        if end_idx - start_idx <= 1:
            raise ValueError("数组中不存在目标值！")
        if target_val == array[start_idx]:
            return start_idx
        elif target_val == array[mid_idx]:
            return mid_idx
        elif target_val == array[end_idx]:
            return end_idx
        else:
            if target_val < array[mid_idx]:
                end_idx = mid_idx
            else:
                start_idx = mid_idx


array = [1, 2, 3, 4, 5, 7, 8, 9, 11, 15, 19, 21, 24, 26, 27, 29, 31, 33, 39, 100, 120, 199, 200, 201, 222, 230, 234,
         235, 236, 270]

for idx, target in enumerate(array):
    print("########## {}".format(idx))
    print(binary_search(array=array, target_val=target))
    print(binary_search2(array=array, target_val=target))
