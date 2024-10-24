import numpy as np


def SSE(y_pred, y):
    """
    sum of squares due to error
    误差平方和（预测值与实际值之差的平方和）
    https://en.wikipedia.org/wiki/Residual_sum_of_squares
    """
    return np.sum((y_pred - y) ** 2)


def SSR(y_pred, y):
    """
    sum of squares due to regression
    回归平方和（预测值与实际值的均值之差的平方和）
    https://en.wikipedia.org/wiki/Explained_sum_of_squares
    """
    return np.sum((y_pred - np.mean(y)) ** 2)


def SST(y):
    """
    Total sum of squares
    总偏差平方和（实际值与均值之差的平方和）
    https://en.wikipedia.org/wiki/Total_sum_of_squares
    """
    return np.sum((y - np.mean(y)) ** 2)


def RSquared(y_pred, y):
    """
    Coefficient of determination
    可决系数
    https://en.wikipedia.org/wiki/Coefficient_of_determination
    """
    return 1 - SSE(y_pred, y) / SST(y)


def AdjustedRSquared(cols, y_pred, y):
    """
    adjusted coefficient of determination
    调整可决系数
    https://en.wikipedia.org/wiki/Coefficient_of_determination#Adjusted_R2
    """
    n = len(y)  # 样本数
    p = len(cols)  # 特征数
    return 1 - (1 - RSquared(y_pred, y)) * (n - 1) / (p - n - 1)


def MSE(y_pred, y):
    """
    mean squares error
    均方误差
    """
    return np.mean((y_pred - y) ** 2)


def RMSE(y_pred, y):
    """
    root mean squares error
    :param y_pred:
    :param y:
    :return:
    """
    return np.sqrt(MSE(y_pred, y))


def MAE(y_pred, y):
    """
    mean absolute error
    均方误差
    :param y_pred:
    :param y:
    :return:
    """
    return np.mean(np.abs(y_pred - y))


def MAPE(y_pred, y):
    """
    mean absolute percentage error
    平均绝对百分比误差
    :param y_pred:
    :param y:
    :return:
    """
    return np.mean(np.abs((y_pred - y) / y))


def MASE(y_pred, y):
    """
    mean absolute scaled error
    平均绝对尺度误差
    :param y_pred:
    :param y:
    :return:
    """
    return np.mean(np.abs(y_pred - y))
