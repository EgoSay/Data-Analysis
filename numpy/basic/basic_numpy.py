# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/12 下午5:19
# @IDE     : PyCharm
# @Description : Numpy基础篇
import numpy as np

# numpy中的数组
my_array1 = np.array([1, 2, 3, 4, 5])
print(my_array1.shape)

my_array2 = np.zeros(5)
print(my_array2)
my_random_array = np.random.random(5)
print(my_random_array)

# 创建二维数组
my_2d_array = np.ones((2, 3))
print(my_2d_array)

my_array3 = np.array([[4, 5], [6, 1]])
print("矩阵的行列数为:{}".format(my_array3.shape))
print("矩阵第二列的数为:{}".format(my_array3[:, 1]))

