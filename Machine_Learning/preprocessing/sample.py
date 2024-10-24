from Machine_Learning.model.classification import KNN
from typing import List, Union
import numpy as np


class Sample:
    def __init__(self, num: Union[int, float] = None, replace: bool = False, axis: int = 0, seed: int = 0, **xargs):
        """

        :param num: 采样数
        :param axis: 0-对行采样，1-对列采样
        :param replace: 是否重复采样
        :param seed: 随机数种子
        :param xargs:
        """
        self.sample_num = num
        self.replace = replace
        self.axis = axis
        self.seed = seed
        self.schema = None
        self.rows_num = None
        self.cols_num = None

        assert self.axis in [0, 1], "axis 只能为0，1"

    @staticmethod
    def _check_arg_type(arg, arg_num, _type):
        """
        检查参数类型
        :param arg: 参数值
        :param arg_num: 参数名
        :param _type: 正确的参数类型
        :return:
        """
        if isinstance(arg, _type):
            raise TypeError(f"参数{arg_num}，只能是{_type}类型，当前类型为: {type(arg)}。")

    @staticmethod
    def check_data(data: Union[np.ndarray, List], target: Union[np.ndarray, List] = None) -> np.ndarray:
        """
        数据检查，并转换为np.ndarray格式
        :param data:
        :param target:
        :return:
        """

        if isinstance(data, list):
            data = np.array(data)
        if target is not None and isinstance(target, list):
            target = np.array(target)

        assert isinstance(data, np.ndarray), f"data数据集类型必须为[np.ndarray,list]，当前为：{type(data)}"
        if target is not None:
            assert isinstance(target, np.ndarray), f"target数据集类型必须为[np.ndarray,list]，当前为：{type(data)}"
            assert data.shape[0] == target.shape[0], f"data:{data.shape[0]} 和 target:{target.shape[0]} 长度不一致！"
        return data

    @staticmethod
    def get_schema(data: Union[np.ndarray, List]) -> np.ndarray:
        dtype = []
        for i in range(data.shape[1]):
            dtype.append(data[i].dtype)
        return np.array(dtype)

    def _get_sample_number(self, x: Union[np.ndarray, List]) -> int:
        """
        获取采样数
        :param x:
        :return:
        """
        if isinstance(self.sample_num, float):
            size = int(np.ceil(self.sample_num * x.shape[self.axis]))
        elif isinstance(self.sample_num, int):
            size = self.sample_num
        else:
            raise ValueError(f"采样数num只能为int或float类型，当前类型为：{type(self.sample_num)}")
        size = size if size >= 1 else 1

        if not self.replace:
            size = size if size <= x.shape[0] else x.shape[0]
        return size


class RandomSample(Sample):
    def _fit_transform(self, x: Union[np.ndarray, List]) -> np.ndarray:
        """

        :param x:
        :return:
        """
        np.random.seed(self.seed)

        size = self._get_sample_number(x)
        target_idx = np.random.choice(x.shape[self.axis], size=size, replace=self.replace)

        if self.axis == 0:
            return x[target_idx]
        else:
            return x[:, target_idx]

    def fit_transform(self, data: Union[np.ndarray, List]) -> np.ndarray:
        """

        :param data:
        :return:
        """
        x = self.check_data(data)
        return self._fit_transform(x)


class StratifiedSample(RandomSample):
    def __init__(self, num: Union[int, float], stratified: int, replace: bool = False, axis: int = 0, seed: int = 0,
                 **xargs):
        """

        :param num: 采样数
        :param stratified: 需要分层的行或列
        :param axis: 0-对行采样，1-对列采样
        :param replace: 是否重复采样
        :param seed: 随机数种子
        :param xargs:
        """
        super().__init__(num=num, axis=axis, replace=replace, seed=seed, **xargs)
        self.stratified = stratified
        self.replace = replace

    def fit_transform(self, x: Union[np.ndarray, List]) -> np.ndarray:
        """

        :param x:
        :return:
        """
        x = self.check_data(x)
        np.random.seed(self.seed)
        array_ls = []
        if self.axis == 0:
            assert self.stratified <= x.shape[1], f"stratified：{self.stratified}列索引大于数据的列数"
            feature = x[:, self.stratified]
            for unique in np.unique(feature):
                part_x = x[feature == unique, :]
                array_ls.append(self._fit_transform(part_x))
        else:
            assert self.stratified <= x.shape[0], f"stratified：{self.stratified}行索引大于数据的行数"
            row = x[self.stratified, :]
            for unique in np.unique(row):
                part_x = x[:, row == unique]
                array_ls.append(self._fit_transform(part_x))
        return np.concatenate(array_ls, axis=self.axis)


class SMOTE(Sample):
    def __init__(self, num: Union[int, float], k: int = 5, replace: bool = False, axis: int = 0):
        super().__init__(num=num, replace=replace, axis=axis)
        self.k = k
        self.cols_idx = None

    def _random_choice(self, sample, top_sample, choice_method: List) -> List:
        return_sample = []

        for idx, i, j in zip(self.cols_idx, sample, top_sample):
            start, end = (i, j) if i >= j else (j, i)
            choice_val = choice_method[idx](start, end)
            return_sample.append(choice_val)

        return return_sample

    def fit_transform(self, data: Union[np.ndarray, List], target: Union[np.ndarray, List]) -> np.ndarray:
        data, target = self.check_data(data), self.check_data(target)
        self.rows_num, self.cols_num, self.cols_idx = data.shape[0], data.shape[1], list(range(data.shape[1]))
        top_k_ls = KNN(self.k, True).fit_transform(data, data, target)
        samples_idx = np.random.choice(data.shape[0], size=self._get_sample_number(data), replace=self.replace)
        samples_top_k = top_k_ls[samples_idx]
        choice_method = []
        for schema in self.get_schema(data):
            if np.issubdtype(schema, np.integer):
                choice_method.append(np.random.randint)
            elif np.issubdtype(schema, np.floating):
                choice_method.append(np.random.uniform)
            else:
                raise TypeError("数据类型只能为 int 或 float！")
        results = []
        for sample_i, top_k_idx in enumerate(samples_top_k):
            _sample, _top_sample = data[sample_i], data[np.random.choice(top_k_idx)]
            while np.allclose(_sample, _top_sample):
                _top_sample = data[np.random.choice(top_k_idx)]
            new_sample = self._random_choice(_sample, _top_sample, choice_method)
            new_sample.append(target[sample_i])
            results.append(new_sample)

        return np.array(results)


if __name__ == '__main__':
    dt1 = np.dtype([
        ('a', np.int32),  # Unicode 字符串，长度为10
        ('b', np.int64),  # 32位整数
        ('c', np.float32),  # 32位浮点数
        ('d', np.float64)  # 32位浮点数
    ])
    data1 = np.array([
        [1, 1, 3, 1.1],
        [1, 1, 3, 1.2],
        [1, 1, 3, 1.3],
        [2, 2, 3, 1.1],
        [2, 3, 3, 1.2],
        [2, 3, 3, 1.3],
        [3, 4, 3, 1.4],
        [3, 5, 3, 1.5],
        [3, 5, 3, 1.1]
    ])
    target1 = [1, 2, 1, 1, 1, 1, 2, 1, 1]
    data2 = np.array([
        (1, 1, 3, 1),
        (2, 4, 3, 2),
        (3, 1, 3, 1)
    ], dtype=dt1)

    print(data2)
    print(data2["a"])
    print(data2["b"])
    print(data2["c"])
    print(data2["d"])

    print(f"原始数据：{data1.shape}")
    print(f" 实验:RandomSample ".center(100, "-"))
    rs = RandomSample(2, replace=False, axis=1).fit_transform(data1)
    print(rs, "\n", f"shape: {rs.shape}")
    print(f" 实验:StratifiedSample ".center(100, "-"))
    ss = StratifiedSample(2, stratified=0, replace=True, axis=1).fit_transform(data1)
    print(ss, "\n", f"shape: {ss.shape}")
    print(f" 实验:SMOTE ".center(100, "-"))
    smote = SMOTE(3, k=3, replace=False).fit_transform(data1, target1)
    print(smote, "\n", f"shape: {smote.shape}")

    """
    export PYTHONPATH=$PYTHONPATH:/Users/v_wangyuji1/Desktop/myLearn/myProject
    """
