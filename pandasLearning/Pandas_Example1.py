# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/7/5 21:48
# @IDE     : PyCharm

import numpy as np
import pandas as pd

# 将数据转成20行5列的DataFrame
data = np.array([49, 33, -
                53, 40, -
                137, 74, -
                11, -
                114, 208, 34, -
                44, 217, -
                183, -
                143, 112, -
                24, -
                181, 55, 0, -
                59, -
                75, 132, -
                107, 65, 87, -
                22, -
                82, -
                91, 85, 10, -
                93, -
                19, 145, 27, -
                223, -
                125, -
                66, -
                103, -
                164, 12, 112, 43, 64, -
                42, 53, -
                95, -
                22, -
                63, -
                44, -
                158, 163, 70, 199, 82, 143, 68, -
                38, -
                71, -
                140, 221, -
                36, -
                266, -
                76, -
                70, -
                67, 44, 170, -
                43, -
                74, -
                25, 54, 33, 137, 34, -
                108, 89, 5, 52, 128, 134, 55, -
                64, 91, 25, 150, -
                104, -
                31, 72, -
                62, -
                200, 122, -
                72, -
                155, 43, 74, -
                111, -
                18, -
                43, -
                43, -
                98]).reshape((20, 5))
df = pd.DataFrame(data)
# df2 = df.copy()
df.quantile(q=0.25, axis=1)
# 计算每一行的和
df['sum'] = df.apply(lambda x: x.sum(), axis=1)
# 计算25%分位数
df['q1'] = df.iloc[:, :5].quantile(q=0.25, axis=1)
# 统计每一行的和大于其25%分位数的行
df = df[df['sum'] > df['q1']]
# 得到结果
result = df.loc[:, ['sum']].apply(sum)
print(result.loc['sum'])

