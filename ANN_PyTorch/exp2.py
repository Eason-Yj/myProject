import numpy as np
from typing import Union
import torch
import numpy as np

# a = torch.randn(5, 5)
# b = torch.IntTensor([1])
# c = torch.Tensor()
# print(a)
# print(b)
# print(a.shape)
# q = a.index_select(1, b)
# print(q)
# print(q.shape)
# torch.index_select()

# print(a[..., 1:2])
# print(a[..., 1:2].size())

# res = a.ge(0.5)
# print(res)
# res = torch.masked_select(a, res)
# print(res)
#
# print(torch.take(a, torch.tensor([1, 2, 5])))

# full
# print(np.full(shape=(2, 3), fill_value=10))
# print(torch.full(size=(2, 3), fill_value=10))

# range
# print(torch.arange(start=1, end=12, step=2, out=torch.zeros(size=(3, 2))))
# print(torch.range(1, 10, step=2))
# print(np.arange(start=1, stop=10, step=2))

# 随机创建
# print(torch.randint(low=1, high=10, size=(2, 2)))
# print(np.random.randint(low=1, high=10, size=(2, 2)))
#
# print(torch.rand(size=(2, 2)))
# print(np.random.rand(2, 2))
#
# print(torch.randn(size=(2, 2)))
# print(np.random.randn(2, 2))

# print(torch.normal(mean=0.1, std=0.2, size=(5, 2)))
# print(np.random.normal(loc=[0, 2], scale=[0.1, 2], size=(5, 2)))

# print(torch.randperm(10))
# print(np.random.permutation(10))

# print(np.random.choice([1, 2, 3], size=25, replace=True, p=[0.1, 0.1, 0.8]))
# print(torch.multinomial(input=torch.tensor([0.1, 0.2, 0.3, 0.5, 0.6]), num_samples=25, replacement=True))

# print(np.random.uniform(low=1, high=2, size=(3, 3)))
# print(torch.distributions.uniform.Uniform(low=torch.tensor([0.0]), high=torch.tensor([5.0])).sample((3)))
