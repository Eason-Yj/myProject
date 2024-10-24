from typing import Union
import numpy as np

from ..feature_engineering import scaler
class DummyAndOneHot():
    """
    独热编码和哑变量编码
    """

    def __init__(self, is_dummy: bool = False, output_sparse_matrix: bool = True):
        """

        :param is_dummy: 是否为哑变量编码
        :param output_sparse_matrix: 是否输出稀疏矩阵
        """
        self.is_dummy = is_dummy
        self.output_sparse_matrix = output_sparse_matrix
        self.cols_idx = dict()  # 稀疏矩阵的 {col_name：col_idx}
        self.res_matrix = None

    def transform(self, x: Union[np.ndarray, list]) -> np.ndarray:
        """

        :param x: 转换的目标矩阵
        :return:
        """
        if isinstance(x, list):
            x = np.array(x)
        if len(x.shape) == 1:
            x = np.reshape(x, (-1, 1))
        elif len(x.shape) > 2:
            raise ValueError("transform: len(x.shape) 应该小于等于2，当前 x.shape({})".format(x.shape))

        for col_idx in range(x.shape[1]):
            sparse_matrix, unique_dict = self._transform(x[:, col_idx])
            max_idx = max(self.cols_idx.values()) if len(self.cols_idx) > 0 else -1
            update_dict = {"{}_{}".format(col_idx, k): (v + max_idx + 1) for k, v in unique_dict.items()}
            self.cols_idx.update(update_dict)
            if self.res_matrix is None:
                self.res_matrix = sparse_matrix
            else:
                self.res_matrix = np.append(self.res_matrix, sparse_matrix, axis=1)

        return self.res_matrix

    def _transform(self, x: np.ndarray) -> (np.ndarray, dict):
        """

        :param x:一列或一行数组
        :return res_matrix: 输出稀疏矩阵
        :return unique_dict: {每个唯一值：对应索引}
        """
        if len(x.shape) == 2 and x.shape[0] == 1:  # shape:(1,x)->(x,)
            x = x[0]
        elif len(x.shape) == 2 and x.shape[1] == 1:  # shape:(x,1)->(x,)
            x = x.reshape(shape=(-1, 1))[0]
        elif len(x.shape) != 1:
            raise ValueError("_transform：x.shape 应该为1行或1列，当前 x.shape({})".format(x.shape))

        unique = np.unique(x)
        unique_dict = dict(zip(unique, range(len(unique))))
        row_count = x.size

        if self.is_dummy:
            res_matrix = np.zeros(shape=(row_count, len(unique) - 1))
        else:
            res_matrix = np.zeros(shape=(row_count, len(unique)))

        for idx, i in enumerate(x):
            uni_idx = unique_dict[i]
            if self.is_dummy and i == unique[-1]:
                continue
            res_matrix[idx, uni_idx] = 1

        return res_matrix, unique_dict


if __name__ == '__main__':
    # x = [0, 1, 2, 3, 1, 2, 4, 1, 2]
    # x = np.reshape(x, (1, -1))
    matrix = [[1, "a", "cc"],
              [1, "c", "cc"],
              [2, "a", "cc"],
              [3, "b", "dd"],
              [5, "a", "ff"]]

    transform = DummyAndOneHot(is_dummy=False)
    print(transform.transform(matrix))
    print(transform.cols_idx)
