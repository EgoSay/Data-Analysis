#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/7/3 下午4:21
# @IDE     : PyCharm
import pandas as pd

"""
将每一row的字典列表集合转成一个列表
>>> [[{'a': (1, 2)}, {'b': (3, 4)}], [{'a': (2, 3)}, {'b': (4, 5)}]]
==>
>>> [{'a': (1, 2)}, {'b': (3, 4)}, {'a': (2, 3)}, {'b': (4, 5)}]
==>
>>> [{'a': [(1, 2, (2, 3)]}, {'b': [(3, 4), (4, 5)]}]
"""
d1 = [{'checking_min': 1, 'checking_max': 4, 'checking_q1': 1.0, 'checking_median': 2.0, 'checking_q3': 2.0, 'duration_min': 6, 'duration_max': 72, 'duration_q1': 12.0, 'duration_median': 24.0, 'duration_q3': 36.0, 'GEO_Y': 1}, {
    'checking_min': 1, 'checking_max': 4, 'checking_q1': 2.0, 'checking_median': 3.0, 'checking_q3': 4.0, 'duration_min': 4, 'duration_max': 60, 'duration_q1': 12.0, 'duration_median': 18.0, 'duration_q3': 24.0, 'GEO_Y': 0}]
pd_df = pd.DataFrame(data=d1)
print(pd_df)
