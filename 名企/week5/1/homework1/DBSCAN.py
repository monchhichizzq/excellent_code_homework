#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time : 2020/9/27 15:16 

# @Author : ZFJ

# @File : DBSCAN.py 

# @Software: PyCharm
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN

coordinate, type_index = make_blobs(
    # 1000个样本
    n_samples=1000,
    # 每个样本2个特征,代表x和y
    n_features=2,
    # 4个中心
    centers=4,
    # 随机数种子
    random_state=3
)
fig0, axi0 = plt.subplots(1)
# 传入x、y坐标，macker='o'代表打印一个圈，s=8代表尺寸
axi0.scatter(coordinate[:, 0], coordinate[:, 1], marker='o', s=8)
# 打印所有的点
plt.show()
color = np.array(['red', 'yellow', 'blue', 'black'])
fig1, axi1 = plt.subplots(1)
# 下面显示每个点真实的类别
for i in range(4):
    axi1.scatter(
        coordinate[type_index == i, 0],
        coordinate[type_index == i, 1],
        marker='o',
        s=8,
        c=color[i]
    )
plt.show()
# eps：半径，min_samples：使用附近的多少个样本来构建中心点
y_pred = DBSCAN(eps=1.8, min_samples=3).fit_predict(coordinate)
plt.scatter(coordinate[:, 0], coordinate[:, 1], c=y_pred, s=8)
plt.show()
