#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Since    : 2019/9/17 下午3:07
# @IDE     : PyCharm
import pandas as pd

data_path = '../data/catering_sale_all.xls'
data = pd.read_excel(data_path, index_col=u'日期')
# 相关系数矩阵， 即给出了任意两款菜式之间的相关系数
print(data.corr())
print("=======显示百合酱蒸凤爪与其他菜式的相关系数=======")
print(data.corr()[u'百合酱蒸凤爪'])
print("=========计算百合酱蒸凤爪与翡翠蒸香茜饺的相关系数=============")
print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']))
data.quantile()