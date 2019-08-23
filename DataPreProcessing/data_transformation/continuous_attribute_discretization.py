#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/8/22 上午11:22
# @IDE     : PyCharm
import pandas as pd

data_file = '../data/discretization_data.xls'
data = pd.read_excel(data_file)
data = data[u'肝气郁结证型系数'].copy()
splits = 4

# 等宽离散化， 各个类比依次命名为0, 1, 2, 3
d1 = pd.cut(data, splits, labels=range(splits))
print(d1)

# 等频率离散化
w = [1.0 * (i / splits) for i in range(splits + 1)]
# 使用describe函数自动计算分位数
w = data.describe(percentiles=w)[4:4 + splits + 1]
w[0] = w[0] * (1 - 1e-10)
d2 = pd.cut(data, w, labels=range(splits))
print(d2)