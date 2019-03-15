# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/14 下午4:58
# @IDE     : PyCharm
# @Description : 广播是一种强大的机制，它允许numpy在执行算术运算时使用不同形状的数组
import numpy as np

# 向矩阵的每一行添加一个常数向量
print("\n================\n")
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)

"""
当矩阵 x 非常大时，在Python中计算显式循环可能会很慢。
我们可以像如下这样实现这种方法：向矩阵 x 的每一行添加向量 v 等同于通过垂直堆叠多个 v 副本来形成矩阵 vv，然后执行元素的求和x 和 vv。 
"""
print("\n================\n")
vv = np.tile(v, (4, 1))
print("向量v垂直堆叠4个副本后:\n{}".format(vv))
y = x + vv
print("矩阵添加向量v后的结果:\n{}".format(y))

print("\n================\n")
"""
Numpy广播允许我们在不实际创建v的多个副本的情况下执行此计算，即使用广播机制
"""
y2 = x + v
print(y2)

