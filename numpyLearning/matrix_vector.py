# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/14 上午10:12
# @IDE     : PyCharm
import numpy as np


# 构建向量
vector1 = np.array([[2], [1], [3]])
print(vector1)
# 转置行向量
vector2 = np.transpose(vector1)
print(vector2)

# 用numpy求解方程组
A = np.array([[2, 1, -2], [3, 0, 1], [1, 1, -1]])
B = np.transpose(np.array([[-3, 5, -2]]))
x = np.linalg.solve(A, B)
print(x)
