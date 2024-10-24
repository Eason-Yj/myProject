class Model:
    pass


if __name__ == '__main__':
    import numpy as np

    # 定义一个矩阵
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [4, 4, 5],
        [2, 2, 6],
        [3, 1, 4],
    ])

    # 定义一个向量
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([3, 2, 2])

    # 进行矩阵与向量的乘法
    result = np.dot(matrix, vector1)

    print("矩阵与向量的乘积是:")
    print(result)
