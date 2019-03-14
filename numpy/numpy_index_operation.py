# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/13 下午8:13
# @IDE     : PyCharm
import numpy as np
import matplotlib.pyplot as plt

print("========# 花式索引 ========")
a1 = np.arange(0, 1000, 100)
indices = [1, 5, -1]
b1 = a1[indices]
print(a1)
print(b1)

print("\n=======# 布尔屏蔽 =======")
# 布尔屏蔽是一个有用的功能，它允许我们根据我们指定的条件检索数组中的元素
a2 = np.linspace(0, 2 * np.pi, 50)
b2 = np.sin(a2)
plt.plot(a2, b2)
mask = b2 >= 0
"""=================================================================================
颜色                               数据点的形状
r  Red           |                 +  Plus sign
g  Green         |                 o  Circle
b   Blue         |                 *  Asterisk
c   Cyan         |                 .  Point 
m  Magenta       |                 x    Cross
y  Yellow        |                 'square' or s    Square 
k   Black        |                 'diamond' or d    Diamond
w  White         |                 ^  Upward-pointing triangle
                 |                 v   Downward-pointing triangle
                 |                 >  Right-pointing triangle
                 |                 'pentagram' or p    Five-pointed star (pentagram)
                 |                 'hexagram' or h     Six-pointed star (hexagram)
====================================================================================
"""
plt.plot(a2[mask], b2[mask], 'bo')
mask = (b2 >= 0) & (a2 <= np.pi / 2)
plt.plot(a2[mask], b2[mask], 'go')
plt.show()


print("\n=======# 缺省索引 =======")
a3 = np.arange(0, 100, 10)
b3 = a3[:5]
c3 = a3[a3 >= 50]
print(b3)  # >>>[ 0 10 20 30 40]
print(c3)  # >>>[50 60 70 80 90]


print("\n=======# where函数（返回一个使得条件为真的元素的列表） =======")
a4 = np.arange(0, 100, 10)
b4 = np.where(a4 < 50)
c4 = np.where(a4 >= 50)[0]
print(b4)  # >>>(array([0, 1, 2, 3, 4]),)
print(c4)  # >>>[5 6 7 8 9]