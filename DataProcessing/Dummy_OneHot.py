from typing import Union
import numpy as np


class DummyAndOneHot():
    """
    独热编码和哑变量编码
    """

    def __init__(self, is_dummy=False):  # type: (bool)->None
        self.is_dummy = is_dummy

    def transform(self, x):  # type: (Union[np.ndarray, list])->np.ndarray
        self.unique = np.unique(x)
        count_x = len(x)
        uni_dict = dict()

        for idx, uni_val in enumerate(self.unique):
            uni_dict[uni_val] = idx
        if self.is_dummy:
            res_matrix = np.zeros(shape=(count_x, len(self.unique) - 1))
        else:
            res_matrix = np.zeros(shape=(count_x, len(self.unique)))

        for idx, i in enumerate(x):
            uni_idx = uni_dict[i]
            if self.is_dummy and i == self.unique[-1]:
                continue
            res_matrix[idx, uni_idx] = 1

        return res_matrix


if __name__ == '__main__':
    x = [0, 1, 2, 3, 1, 2, 4, 1, 2]
    transform = DummyAndOneHot(is_dummy=True)
    print(transform.transform(x))
