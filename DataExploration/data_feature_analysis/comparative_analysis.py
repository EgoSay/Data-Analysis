#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/5 下午3:31
# @IDE     : PyCharm
"""对比分析"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
from functools import reduce
"""绘制柱状图和折线图对比分析每天的销售量情况"""
data = pd.read_excel('../data/catering_sale_all.xls', index_col=u'日期')
df = pd.DataFrame(data)

fig, ax1 = plt.subplots(figsize=(12, 10))
# 以日期作为柱状图横坐标轴
x_index = df.index.astype(str).values.tolist()
# 统计每一天的销售量作为纵坐标轴
y_volume = df.sum(axis=1).values.tolist()

# 绘制柱状图
ax1.bar(x_index, y_volume, color={'silver', 'wheat'})
fig.autofmt_xdate()
ax1.tick_params(labelsize='large', width=5)
ax1.set_xlabel("日期")
ax1.set_ylabel("销售量")

# 绘制折线图， 和柱状图共享y轴
ax2 = ax1.twiny()
# 无法同时共享X轴， 所以选择隐藏不展示x轴
ax2.xaxis.set_visible(False)

ax2.plot(x_index, y_volume, 'g', marker='*', ms=10)

# 标注销量
for i, val in enumerate(y_volume):
    plt.text(i, val + 4, float(val),
             horizontalalignment='center',
             verticalalignment='bottom',
             fontdict={'fontweight': 500, 'size': 12})
plt.title("销售量对比分析图")

plt.show()
print("============END==========")
