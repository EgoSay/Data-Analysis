#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/8/20 下午7:29
# @IDE     : PyCharm
"""异常值分析"""

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据， 指定 "日期列" 为索引列
catering_sale = '../data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')
# describe()可以看到计数count， 其count是非空值数，再与len(data)比较可知是否存在缺失值
print("数据量为:{}".format(len(data)))
print(data.describe())

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
p = data.boxplot(return_type='dict')

# filers标签为异常值， 其他key还有['whiskers', 'caps', 'boxes', 'medians', 'fliers', 'means']
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
# 从小到大排序, 该方法直接改变原对象
y.sort()

# 用annotate添加注释
# 以下参数都是经过调试的， 需要具体问题具体调试
for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8/(y[i]-y[i-1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
plt.show()

