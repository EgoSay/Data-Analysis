#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/7/4 下午6:00
# @IDE     : PyCharm

"""
关于pandas的合并操作示例
Pandas提供了各种工具，可以轻松地将Series，DataFrame和Panel对象与各种赋值逻辑组合在一起，用于索引和连接/合并类型操作时的关系代数功能
"""

import pandas as pd
import numpy as np

"""
拼接操作
"""
# concat连接操作
df = pd.DataFrame(np.random.rand(8, 3), columns=['A', 'B', 'C'])
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

# join操作
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
pd.merge(left, right, on='key')

# 追加
s = df.iloc[3]
df.append(s, ignore_index=True)

"""
“group by“是指涉及下列一项或多项步骤的程序：
    - Splitting：根据一些标准将数据分解成组
    - Applying：将函数独立地应用于每个组
    - Combining：将结果组合成数据结构
"""
df1 = pd.DataFrame({'A2': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B2': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C2': np.random.randn(8), })
df1.groupby(['A2', 'B2']).sum()

"""
重塑(Reshaping)
"""
# 堆叠(Stack)
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'bar', 'bar', 'baz', 'baz'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df2 = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# stack()方法压缩DataFrame的列
stacked = df2[:4].stack()
#  stack()的逆操作是unstack()，默认情况下取消最后压缩的那个级别
stacked.unstack(1)

"""
数据透视表(PivotTables)
"""

"""
时间序列
"""
rng = pd.date_range('7/5/2019 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
ts_utc = ts.tz_localize('UTC')
# 转换为另一个时区
ts_utc.tz_convert('US/Eastern')
ts.to_period()

"""
分类
"""
df3 = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
df3["grade"] = df3["raw_grade"].astype("category")
df3["grade"].cat.categories = ["very good", "good", "very bad"]
# 对categories重新排序并同时添加缺少的category(Series.cat下的方法默认返回一个新的Series)
df3["grade"] = df3["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
# 按分好类的列分组(groupby)可以显示空categories
df3.groupby("grade").size()