# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/12 下午5:19
# @IDE     : PyCharm
# @Description : Numpy数组操作
import numpy as np

print("\n===========# 数组逻辑运算==============\n")
a1 = np.array([[1.0, 2.0], [3.0, 4.0]])
b1 = np.array([[5.0, 6.0], [7.0, 8.0]])
sums = a1 + b1
difference = a1 - b1
product = a1 * b1
# 这里乘法运算符执行逐元素乘法而不是矩阵乘法，如下操作执行矩阵乘法
matrix_product = a1.dot(b1)
quotient = a1 / b1
print("Sum = {0}\nDifference = {1}\nProduct = {2}\nQuotient = {3}\nMatrix_product = {4}"
      .format(sums, difference, product, quotient, matrix_product))
# 当使用逻辑运算符比如 “<” 和 “>” 的时候，返回的将是一个布尔型数组
print(a1 < b1)

print("打印数组叠加和:{}".format(a1.cumsum()))

print("\n=====# 创建数组几种方法=======\n")
a2 = np.array([0, 1, 2, 3, 4])
b2 = np.array((0, 1, 2, 3, 4))
c2 = np.arange(5)
d2 = np.linspace(0, 2 * np.pi, 5)   # linspace函数在指定的时间间隔内返回均匀间隔的数字
e2 = np.empty((2, 3))               # empty函数创建一个数组。它的初始内容是随机的，取决于内存的状态
f2 = np.full((2, 2), 3)             # full函数创建一个填充给定值的n * n数组。
g2 = np.eye(3, 3)                   # eye函数可以创建一个n * n矩阵，对角线为1s，其他为0
h2 = np.random.random((2, 2))       # 生成随机数组
print(a2)
print(b2)
print(c2)
print(d2)
print(e2)
print(f2)
print(g2)
print(h2)

print("\n=========# 多维数组操作================\n")
multidimensional_arrays = np.array([[11, 12, 13, 14, 15],
                                    [16, 17, 18, 19, 20],
                                    [21, 22, 23, 24, 25],
                                    [26, 27, 28, 29, 30],
                                    [31, 32, 33, 34, 35]])
print("\n第二行第三四列的数据为:{}".format(multidimensional_arrays[1, 2:4]))
print("隔位打印:\n{}".format(multidimensional_arrays[::2, ::2]))
print("打印第2列:{}\n".format(multidimensional_arrays[:, 1]))

print("\n=========# 数组属性================\n")
print(
    "数组内数据类型为:{0}\n数组大小:{1}\n数组行列数:{2}\n数组每个数据项占用的字节数:{3}\n数组维度:{4}\n" .format(
        multidimensional_arrays.dtype,
        multidimensional_arrays.size,
        multidimensional_arrays.shape,
        multidimensional_arrays.itemsize,
        multidimensional_arrays.ndim))
