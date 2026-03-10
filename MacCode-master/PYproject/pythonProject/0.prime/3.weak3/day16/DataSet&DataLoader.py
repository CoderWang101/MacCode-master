import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import multiprocessing as mp

class RandomDataset(Dataset):
    def __init__(self, num_samples=1000, feature_dim=20):
        """
        初始化数据集，随机生成特征和标签
        :param num_samples: 样本总数
        :param feature_dim: 特征维度
        """
        self.num_samples = num_samples
        self.feature_dim = feature_dim
        # 生成随机特征数据 (num_samples, feature_dim)
        self.data = torch.randn(num_samples, feature_dim)
        # 生成随机二分类标签 (0 或 1)
        self.labels = torch.randint(0, 2, (num_samples,))

    def __len__(self):
        """返回数据集中的样本总数"""
        return self.num_samples

    def __getitem__(self, idx):
        """
        根据索引 idx 返回一个样本及其标签
        这里返回的是一个元组 (feature, label)
        """
        return self.data[idx], self.labels[idx]

if __name__ == '__main__':
    try:
        mp.set_start_method('spawn', force=True)
    except RuntimeError:
        pass
    dataset = RandomDataset(num_samples=1000, feature_dim=20)
    dataloader = DataLoader(
        dataset,
        batch_size=32,
        shuffle=True,
        num_workers=2,
        drop_last=False
    )
    
    # 打印所有 DataLoader 批次
    '''batch_idx: 批次索引, features shape: 特征形状, labels shape: 标签形状'''
    for batch_idx, (features, labels) in enumerate(dataloader):
        print(f"Batch {batch_idx+1}: features shape = {features.shape}, labels shape = {labels.shape}")
        # break
