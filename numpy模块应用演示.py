from numpy import *
import numpy.matlib
import numpy as np


print(eye(4))                            #输出4角阵列

a = np.array([[1,  2],  [3,  4]])        #输出自定义阵列
print(a)

b = np.array([1,  2,  3], dtype=complex) #输出dtype complex(+J)阵列
print(b)

c = np.matlib.rand(3, 3)                 #输出随机3*3格(也是个)的随机数(可能是任何小数或整数)
print(c)
