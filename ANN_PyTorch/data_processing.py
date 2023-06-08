"""
conda install pytorch torchvision torchaudio cpuonly -c pytorch
conda install opencv

"""
from torch.utils.data import dataset
import os
import PIL.Image as images


class myDataset(dataset.Dataset):
    def __init__(self, images_data, label_data):
        self.images_dir = images_data
        self.label_dir = label_data
        self.images_list = os.listdir(self.images_dir)
        self.label_list = os.listdir(self.images_dir)

    def __getitem__(self, idx):
        image_name = self.images_list[idx]
        image_label = self.label_list[idx]
        image_path = os.path.join(self.images_dir, image_name)
        images_data = images.open(image_path)  # 路径中不能包含中文和大写字母

        return images_data, image_label


images_path = r"dataset\hymenoptera_exp_data\train\ants_image"
label_path = r"dataset\hymenoptera_exp_data\train\ants_label"
data = myDataset(images_data=images_path, label_data=label_path)

print(data[0])
print(data[0][0].size)
