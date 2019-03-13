# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/12 下午5:19
# @IDE     : PyCharm
# @Description : Numpy数组操作
import numpy as np
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sums = a + b
difference = a - b
product = a * b
# 这里乘法运算符执行逐元素乘法而不是矩阵乘法，如下操作执行矩阵乘法
matrix_product = a.dot(b)
quotient = a / b
print("Sum = {0}\nDifference = {1}\nProduct = {2}\nQuotient = {3}\nMatrix_product = {4}".format(sums, difference, product, quotient, matrix_product))

# 创建数组几种方法
a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2 * np.pi, 5)
print(a)
print(b)
print(c)
print(d)

# 多维数组
multidimensional_arrays = np.array([[11, 12, 13, 14, 15],
                                    [16, 17, 18, 19, 20],
                                    [21, 22, 23, 24, 25],
                                    [26, 27, 28 ,29, 30],
                                    [31, 32, 33, 34, 35]])
print("第二行第三四列的数据为:{}".format(multidimensional_arrays[1, 2:4]))

