# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/15 上午11:53
# @IDE     : PyCharm
import numpy as np


"""广播的简单应用"""
v = np.array([1, 2, 3])  # v has shape (3,)
w = np.array([4, 5])     # w has shape (2,)

# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:
# [[ 4  5]
#  [ 8 10]
#  [12 15]]
print(np.reshape(v, (3, 1)) * w)

print("\n================\n")
# Add a vector to each row of a matrix
x = np.array([[1, 2, 3], [4, 5, 6]])
# giving the following matrix:
# [[2 4 6]
#  [5 7 9]]
print(x + v)

print("\n================\n")
# Add a vector to each column of a matrix
# x has shape (2, 3) and w has shape (2,).
# If we transpose x then it has shape (3, 2) and can be broadcast
# against w to yield a result of shape (3, 2); transposing this result
# yields the final result of shape (2, 3) which is the matrix x with
# the vector w added to each column. Gives the following matrix:
# [[ 5  6  7]
#  [ 9 10 11]]
print((x.T + w).T)