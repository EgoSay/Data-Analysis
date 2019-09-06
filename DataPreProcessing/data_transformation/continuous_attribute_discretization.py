#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/8/22 上午11:22
# @IDE     : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data_file = '../data/discretization_data.xls'
data = pd.read_excel(data_file)
data = data[u'肝气郁结证型系数'].copy()
k = 4

# 等宽离散化， 各个类比依次命名为0, 1, 2, 3
d1 = pd.cut(data, k, labels=range(k))
print(d1)

# 等频率离散化
w = [1.0 * (i / k) for i in range(k + 1)]
# 使用describe函数自动计算分位数
w = data.describe(percentiles=w)[4:4 + k + 1]
w[0] = w[0] * (1 - 1e-10)
d2 = pd.cut(data, w, labels=range(k))
print(d2)

# 基于聚类分析的方法
# 建立模型, n_jobs是并行数， 一般等于CPU数较好
kmodel = KMeans(n_clusters=k, n_jobs=2)
# 训练模型
kmodel.fit(pd.DataFrame(data))
# 输出聚类中心， 并且排序(默认是随机排序)
c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0)
w2 = c.rolling(2).mean().iloc[1:]
w2 = [0] + list(w2[0]) + [data.max()]
d3 = pd.cut(data, w2, labels=range(k))
print(d3)


def cluster_plot(d, k):
    # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(8, 3))
    for j in range(0, k):
        plt.plot(data[d == j], [i for i in d[d == j]], 'o')

    plt.ylim(-0.5, k-0.5)
    return plt


cluster_plot(d1, k).show()
cluster_plot(d2, k).show()
cluster_plot(d3, k).show()