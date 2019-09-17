#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Since    : 2019/9/17 上午11:37
# @IDE     : PyCharm
"""绘制餐饮企业的菜品盈利的帕累托图进行其对企业总盈利的贡献度分析"""
import pandas as pd
import matplotlib.pyplot as plt

# import data
data_path = '../data/catering_dish_profit.xls'
data = pd.read_excel(data_path, index_col=u'菜品名')
profit_data = data[u'盈利'].copy()
profit_data.sort_values(ascending=False)

# Draw Plot
plt.figure()
plt.title('菜品盈利的帕累托图')
profit_data.plot(kind='bar')
plt.ylabel(u'盈利(元)')
# 函数cumsum(): 依次给出前1，2...n个数的和
contribution = 1.0 * profit_data.cumsum() / profit_data.sum()
contribution.plot(color='r', secondary_y=True, style='-o', linewidth=2)
plt.annotate(format(contribution[6], '.4%'),
             xy=(6, contribution[6]),
             xytext=(6*0.9, contribution[6]*0.9),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.ylabel(u'盈利(比例)')
plt.show()