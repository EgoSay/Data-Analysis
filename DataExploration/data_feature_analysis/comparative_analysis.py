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
"""绘制柱状图对比分析每天的销售量情况"""
data = pd.read_excel('../data/catering_sale_all.xls', index_col=u'日期')
df = pd.DataFrame(data)

# 以日期作为柱状图横坐标轴
x_index = df.index.astype(str).values.tolist()
# 统计每一天的销售量作为纵坐标轴
y_volume = df.sum(axis=1).values.tolist()

plt.bar(x_index, y_volume, color='rgb')
plt.show()
print("============END==========")
