# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/15 下午2:14
# @IDE     : PyCharm
# @Decription : Scipy是一个在numpy库的基础上增加了众多的数学、科学以及工程计算中的常用的库函数

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
"""
问题描述：假定有一组实验数据(Xi, Yi),他们之间满足函数关系f(x) = kx + b，求解k和b是多少
"""


# 样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi = np.array([160, 165, 158, 172, 159, 176, 160, 162, 171])
Yi = np.array([58, 63, 57, 65, 62, 66, 58, 59, 62])


# 需要拟合的函数func :指定函数的形状 k= 0.42116973935 b= -8.28830260655
def func(p, x):
    k, b = p
    return k * x + b


# 偏差函数：x,y都是列表:这里的x,y跟上面的Xi,Yi中是一一对应的
def error(p, x, y):
    return func(p, x) - y


# k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
p0 = [1, 20]

# 把error函数中除了p0以外的参数打包到args中(使用要求)
Para = leastsq(error, p0, args=(Xi, Yi))

# 读取结果
k, b = Para[0]
print("k=", k, "b=", b)

# 画样本点
plt.figure(figsize=(8, 6))  # 指定图像比例： 8：6
plt.scatter(Xi, Yi, color="green", label="样本数据", linewidth=2)

# 画拟合直线
x = np.linspace(150, 190, 100)  # 在150-190直接画100个连续点
y = k * x + b  # 函数式
plt.plot(x, y, color="red", label="拟合直线", linewidth=2)
plt.legend()  # 绘制图例
plt.show()
