from typing import Union, List
import numpy as np

TypeArray = Union[list, np.ndarray]


def unique(array: TypeArray, is_dict: bool = False) -> Union[list, dict]:
    """
    数组唯一值，统计唯一值个数
    和np.unique()

    :param array: 输入的数组
    :param is_dict: 是否输出字典，会统计每个唯一值的个数
    :return:
    """
    _dict = dict()
    for i in array:
        if i in _dict:
            _dict[i] += 1
        else:
            _dict[i] = 1
    if is_dict:
        return {k: v for k, v in sorted(_dict.items(), key=lambda x: x[0])}  # 字典按k排序
    else:
        return sorted(_dict.keys())


def equalWidth(array: TypeArray, bin_num: int = 1, return_tuple: bool = True):
    """
    将数组等间隔切分为n个数组(等宽切割)
    numpy.linspace | pd.cut 效果类似

    :param array:
    :param bin_num:
    :param return_tuple:
    :return:
    """
    if isinstance(array, np.ndarray):
        array = array.tolist()

    unique_list = unique(array, is_dict=False)  # 获取唯一值
    if bin_num >= len(unique_list):  # 当切分数大于数组唯一值个数时，设置切分数为数组唯一值个数
        bins_nodes = unique_list
    else:
        min_val, max_val = float(min(array)), float(max(array))
        gap_val = (max_val - min_val) / bin_num  # 每个间隔的大小
        bins_nodes = [round(min_val + gap_val * i, 6) for i in range(bin_num)] + [max_val]  # 生成切分节点
        bins_nodes = sorted(bins_nodes)
    print(bins_nodes)
    if not return_tuple:
        return bins_nodes

    tuple_bins = []
    for i in range(1, len(bins_nodes)):
        tuple_bins.append((bins_nodes[i - 1], bins_nodes[i]))
    print(tuple_bins)
    return tuple_bins


def specialFrequency(array: TypeArray, num: int = 1, return_tuple: bool = True) -> TypeArray:
    """
    固定每个分组的样本数去切分数组
    :param array:
    :param num:
    :param return_tuple:
    :return: 每个子数组的起始终止样本索引
    例子：
    array = [23, 11, 98, 55, 19, 76, 18, 41, 88, 59, 88, 20, 8, 38, 83, 79, 37]
    return_tuple=False [0, 5, 10, 15, 17]
    return_tuple=True  [(0, 5), (5, 10), (10, 15), (15, 17)]
    """
    if isinstance(array, np.ndarray):
        array = array.tolist()

    array_lens = len(array)
    min_val, max_val = float(min(array)), float(max(array))

    if num >= array_lens:
        bins_nodes = [min_val, max_val]
    else:
        unique_dict = unique(array, is_dict=True)
        unique_list = sorted(unique_dict.keys())
        current_num = 0
        bins_nodes = []

        for idx in range(1, len(unique_list)):
            prev_unique = unique_list[idx - 1]
            current_unique = unique_list[idx]

            current_unique_count = unique_dict[current_unique]

            prev_num = unique_dict[prev_unique] if idx == 1 else current_num
            current_num = current_unique_count + prev_num

            if current_num >= num >= prev_num:
                # 判断当前分箱增加一个唯一值的统计值和不增加唯一值的统计值哪个更接近目标样本数
                prev_diff = num - prev_num
                curr_diff = current_num - num

                if prev_diff <= curr_diff:  # 若不增加新唯一值的统计值时更接近，则添加当前前一个唯一值作为节点
                    bins_nodes.append(current_unique)
                    current_num = current_unique_count
                elif (idx + 1) != len(unique_list):
                    bins_nodes.append(unique_list[idx + 1])
                    current_num = 0

    if bins_nodes[0] != min_val:
        bins_nodes.insert(0, min_val)
    bins_nodes.append(99999)  # 在最后添加正无穷（使用9999代替）

    if not return_tuple:
        return bins_nodes

    tuple_bins = []
    for idx in range(1, len(bins_nodes)):
        tuple_bins.append((bins_nodes[idx - 1], bins_nodes[idx]))
    return tuple_bins


def equalFrequency(array: TypeArray, bin_num: int = 1, return_tuple: bool = True) -> TypeArray:
    """
    将数组等数量切分为n个数组(等频切割)
    :param array:
    :param bin_num:
    :param return_tuple:
    :return: 每个子数组的起始终止样本索引
    例子：
    array = [23, 11, 98, 55, 19, 76, 18, 41, 88, 59, 88, 20, 8, 38, 83, 79, 37]
    return_tuple=False [0, 5, 10, 15, 17]
    return_tuple=True  [(0, 5), (5, 10), (10, 15), (15, 17)]
    """
    if isinstance(array, np.ndarray):
        array = array.tolist()

    unique_list = unique(array)
    if bin_num >= len(unique_list):
        bins_nodes = unique_list
        if not return_tuple:
            return bins_nodes
        tuple_bins = []
        for idx in range(1, len(bins_nodes)):
            tuple_bins.append((bins_nodes[idx - 1], bins_nodes[idx]))
    else:
        array_lens = len(array)
        num = array_lens // bin_num
        num = num + 1 if (array_lens % bin_num) > 0.5 * num else num
        bin_rules = specialFrequency(array=array, num=num, return_tuple=return_tuple)
        if len(bin_rules) != bin_num:
            if return_tuple:
                bin_rules.pop()
                bin_rules[-1] = (bin_rules[-1][0], 9999)
            else:
                bin_rules.pop(-2)
        return bin_rules


def getBinArrays(array: TypeArray, bins_rule: List[tuple]) -> dict:
    output_dict = {}
    for val in array:
        bins_rule_str = [f"[{l}, {r})" for l, r in bins_rule]
        for idx, _bin in enumerate(bins_rule):
            if _bin[0] <= val < _bin[1]:
                if bins_rule_str[idx] in output_dict:
                    output_dict[bins_rule_str[idx]].append(val)
                else:
                    output_dict[bins_rule_str[idx]] = [val]
    return output_dict


if __name__ == '__main__':
    array1 = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 12, 12, 12]
    # array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    res2 = equalFrequency(array=array1, bin_num=4)
    # res2 = specialFrequency(array=array1, num=4)
    print(res2)
    print(getBinArrays(array=array1, bins_rule=res2))
