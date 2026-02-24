import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Alice", "Charlie"],
    "age": [25, 30, 35, 40, 25, np.nan],
    "score": [80, np.nan, 90, 95, 80, np.nan],
    "gender": ["F", "M", "M", np.nan, np.nan, np.nan],
}

df = pd.DataFrame(
    data,
    index=["s1", "s2", "s3", "s4", "s5", "s6"],
    columns=["name", "age", "score", "gender"],
)
print(df,"\n")
# 列维度的缺失值数量统计：
# df.isnull() 返回与 df 同形状的布尔矩阵，True 表示该位置是缺失值（NaN）
# .sum() 在列方向（axis=0，默认）对 True 计数，得到每一列的缺失值个数
print("每一列缺失值数量")
print(df.isnull().sum())

# 行维度的缺失值数量统计：
# 指定 axis=1 表示沿着列聚合（逐行统计），得到每一行的缺失值个数
print("每一行缺失值数量")
print(df.isnull().sum(axis=1))

# 行缺失率：
# 每一行缺失数量 / 列总数；列总数使用 df.shape[1] 获取，避免误用行数 len(df)
print("每一行缺失率")
print(df.isnull().sum(axis=1) / df.shape[1])

#gender缺失率
print("gender缺失率:",df["gender"].isnull().sum()/len(df))