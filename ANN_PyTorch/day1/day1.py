"""
/Users/v_wangyuji1/Desktop/myLearn/dataset/iris.csv
"""
import torch
from torch import nn
from torch import optim
from torch.utils.data import Dataset
import os
import pandas as pd
import numpy as np
import tqdm

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class IrisDataset(Dataset):
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath)  # type: pd.DataFrame

        self.numpy_data = self.data.iloc[:, :-1].to_numpy(dtype=np.float32)
        self.numpy_target = self.data.iloc[:, [-1]].to_numpy(dtype=np.float32)

        self.train_data = (self.numpy_data - np.mean(self.numpy_data, axis=0)) / np.std(self.numpy_data, axis=0)

        self.tensor = torch.from_numpy(self.train_data)
        self.target = torch.from_numpy(self.numpy_target)

        print(self.tensor)
        print(self.target)
        self.data_len = len(self.data)

    def __len__(self):
        return self.data_len

    def __getitem__(self, index):
        return self.numpy_data[index].tolist(), self.numpy_target[index].tolist()


class expNN(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim1, hidden_dim2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer_1 = nn.Linear(input_dim, hidden_dim1)
        self.layer_2 = nn.Linear(hidden_dim1, hidden_dim2)
        self.layer_3 = nn.Linear(hidden_dim2, output_dim)

    def forward(self, x):
        x = self.layer_1(x)
        x = self.layer_2(x)
        x = self.layer_3(x)

        return x


if __name__ == '__main__':
    data = IrisDataset('/Users/v_wangyuji1/Desktop/myLearn/dataset/iris.csv')
    print(data[0])
