#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/9/11 11:03
# @IDE     : PyCharm
import pandas as pd

data = pd.read_excel('../data/catering_sale.xls', index_col=u'日期')
# 根据情况自定义过滤异常值
data = data[(data['销量'] > 400) & (data['销量'] < 5000)]
statistics = data.describe()
# 极差
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
# 变异系数
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
# 四分位数间距
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']

print(statistics)
