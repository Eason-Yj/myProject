import numpy as np
from typing import Union
import torch
import torchvision.transforms
from torch import nn
from torch.nn import functional as F
from torch import optim
from torch.utils.data import DataLoader, IterableDataset
from torchvision import datasets
import PIL.Image as images

dataset_transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.1307,), (0.3081,))
])

train_loader = DataLoader(datasets.MNIST(
    "data/MNIST", train=True, download=True,
    transform=dataset_transform), batch_size=512, shuffle=True)  # type:
test_loader = DataLoader(datasets.MNIST(
    "data/MNIST/", train=False, download=True,
    transform=dataset_transform), batch_size=512)


# data = train_loader
# print(type(data))
# print(type(data.dataset))
# print(data)
# print(data[0].shape)
# print(data[1])

class DummyAndOneHot():
    """
    独热编码和哑变量编码
    """

    def __init__(self, is_dummy=False):  # type: (bool)->None
        self.is_dummy = is_dummy
        self.uni_dict = dict()
        self.is_dummy = 1 if is_dummy else 0

    def transform(self, x):  # type: (Union[np.ndarray, list, torch.Tensor])->Union[np.ndarray,torch.Tensor]
        if isinstance(x, torch.Tensor):
            self.unique = x.unique()
            res_matrix = torch.zeros(size=(len(x), len(self.unique) - self.is_dummy))
            for idx, uni_val in enumerate(self.unique):
                self.uni_dict[str(uni_val.data)] = idx
            for idx, i in enumerate(x):
                uni_idx = self.uni_dict[str(i.data)]
                if self.is_dummy and i == self.unique[-1]:
                    continue
                res_matrix[idx, uni_idx] = 1

        else:
            self.unique = np.unique(x)
            res_matrix = np.zeros(shape=(len(x), len(self.unique) - self.is_dummy))
            for idx, uni_val in enumerate(self.unique):
                self.uni_dict[str(uni_val)] = idx
            for idx, i in enumerate(x):
                uni_idx = self.uni_dict[str(i)]
                if self.is_dummy and i == self.unique[-1]:
                    continue
                res_matrix[idx, uni_idx] = 1

        return res_matrix


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.fc1 = nn.Linear(28 * 28, 256)
        self.fc2 = nn.Linear(256, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


# net = Net()
# param = net.parameters()
# optimizer = optim.SGD(params=param, lr=0.01, momentum=0.9)
#
# for epoch in range(3):
#     for batch_idx, (x, y) in enumerate(train_loader):
#         x = x.view(x.size(0), 28 * 28)  # type:torch.Tensor
#         out = net(x)
#         # res = DummyAndOneHot().transform(y)
#         res = F.one_hot(y).float()
#         loss = F.mse_loss(out, res)
#         loss.backward()
#         optimizer.step()
#         print("#### epoch %s" % epoch, "   batch_idx %s" % batch_idx, "   loss %s" % loss.item())
#     break
