#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/7/3 下午3:48
# @IDE     : PyCharm
import numpy as np
import pandas as pd


"""
对象的创建
"""
# 通过传入一些值的列表来创建一个Series， Pandas会自动创建一个默认的整数索引
s = pd.Series([1, 3, 5, np.nan, 7])
# 通过传递带有日期时间索引和带标签列的NumPy数组来创建DataFrame
dates = pd.date_range('20190701', periods=6)
df1 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# 通过传递可以转化为类似Series的dict对象来创建DataFrame
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

"""
查看数据
"""
# 查看DataFrame顶部和尾部的数据
df1.head()
df1.tail(3)
# 显示索引、列和底层NumPy数据
print(df1.index)
print(df1.columns)
print(df1.values)
# describe() 方法显示数据的快速统计摘要
df1.describe()
# 转置
df1.T
# 按轴排序
df1.sort_index(axis=1, ascending=False)
# 按值排序
df1.sort_values(by="B")


"""
选择
"""
print(df1["A"])
print(df1[0:3])
# 通过标签选择
df1.loc[dates[0]]
# 通过标签在多个轴上选择数据
df1.loc[:, ['A', 'B']]
# 通过标签同时在两个轴上切片
df1.loc['20190702':'20190704', ['A', 'B']]

# 按位置选择
print(df1.iloc[3])
print(df1.iloc[3:5, 0:2])

# 布尔索引
print(df1[df1.A > 0])
df3 = df1.copy()
df3['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df3[df3['E'].isin(['two', 'four'])])

"""
赋值
"""
# 添加新列将自动根据索引对齐数据
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20190701', periods=6))
df1['F'] = s1
# 通过标签赋值
df1.at[dates[0], 'A'] = 0
# 通过位置赋值
df1.at[dates[0], 'A'] = 0
# 通过位置赋值
df1.loc[:, 'D'] = np.array([5] * len(df1))


"""
缺失值
"""
# 重建索引允许你更改/添加/删除指定轴上的索引。 这个操作会返回一个副本(不会更改原来的对象)
df4 = df1.reindex(index=dates[0:4], columns=list(df1.columns) + ['E'])
df4.loc[dates[0]:dates[1], 'E'] = 1
# 删除任何带有缺失值的行
df4.dropna(how='any')
# 填充缺失值
df4.fillna(value=5)
# 获取值为na的掩码(True/False)
pd.isna(df4)

