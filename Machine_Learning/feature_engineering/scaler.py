import numpy as np
import pandas as pd
from typing import Union


def z_score(x: Union[np.ndarray, pd.Series, pd.DataFrame, list]):
    """
    z-score normalization
    不会改变分布(distribution)的偏斜（skewness）。原始数据的均值(mean)和方差(variance)分别转为 0 和 1。实际的分布形状保持不变。

    result = (样本 - 样本均值) / 样本标准差

    :param x:
    :return:
    """
    if isinstance(x, list):
        x = np.array(x)
    elif isinstance(x, (pd.Series, pd.DataFrame)):
        x = x.values

    return (x - x.mean()) / x.std()
