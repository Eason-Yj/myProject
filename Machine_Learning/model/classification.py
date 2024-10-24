import numpy as np
from Machine_Learning.model.base_model import Model


class Distance:
    def __init__(self, mode: str = "Euclidean"):
        self.mode = mode

    @staticmethod
    def sklearn_euclidean(x1: np.ndarray, x2: np.ndarray) -> np.ndarray:
        from sklearn.metrics.pairwise import euclidean_distances
        return euclidean_distances(x1, x2)

    @staticmethod
    def euclidean(x1: np.ndarray, x2: np.ndarray) -> np.ndarray:
        """
        欧式距离计算
        :param x1:
        :param x2:
        :return:
        """
        lens_x1, lens_x2 = x1.shape[0], x2.shape[0]
        res_array = np.zeros(shape=(lens_x1, lens_x2))
        for x1_i in range(lens_x1):
            for x2_i in range(lens_x2):
                res_array[x1_i, x2_i] = np.sqrt(np.sum(np.square(x1[x1_i] - x2[x2_i])))
        return res_array

    def fit_transform(self, x1: np.ndarray, x2: np.ndarray) -> np.ndarray:
        if self.mode == "Euclidean":
            return self.euclidean(x1, x2)


class KNN(Model):
    """ K近邻算法 """

    def __init__(self, k: int = 3, return_top_k: bool = False):
        """

        :param k: 近邻数
        :param return_top_k: 是否返回最近邻的k个样本的索引
        """
        self.k = k
        self.return_top_k = return_top_k
        self.train = None
        self.target = None
        self._square_matrix = None

    def fit(self, data: np.ndarray, target: np.ndarray):
        self.train = data
        self.target = target
        self.k = self.k if self.k <= self.train.shape[0] else self.train.shape[0]

        return self

    def transform(self, test: np.ndarray) -> np.ndarray:
        distance_matrix = Distance.euclidean(test, self.train)
        predictions = []
        top_k_ls = []
        start_idx = 0
        if np.allclose(self.train, test):
            self.k = self.k + 1 if self.train.shape[0] >= self.k + 1 else self.k
            start_idx = 1

        for distance in distance_matrix:
            top_k_idx = np.argsort(distance)[start_idx:self.k]
            top_k_ls.append(top_k_idx)
            top_k = self.target[top_k_idx]
            uniques, counts = np.unique(top_k, return_counts=True)
            predictions.append(uniques[np.argmax(counts)])

        if self.return_top_k:
            return np.array(top_k_ls)
        else:
            return np.array(predictions)

    def fit_transform(self, train: np.ndarray, test: np.ndarray, target: np.ndarray) -> np.ndarray:
        self.fit(train, target)
        return self.transform(test)


if __name__ == '__main__':
    data1 = np.array([
        [1, 1, 1],
        [1, 2, 1],
        [1, 2, 1],
        [2, 2, 2],
        [2, 3, 2],
    ])
    target1 = np.array([1, 1, 1, 2, 2])

    data2 = np.array([[2, 2, 2],
                      [2, 3, 2]])

    model = KNN(k=99, return_top_k=True).fit(data1, target1)
    print(model.transform(data1))
