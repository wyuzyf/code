# -*-coding:utf-8-*-


import numpy as np
from scipy.spatial.distance import pdist

x=np.random.random(10)
y=np.random.random(10)

# x = [12,56]
# y = [34,98]

print x,y

#方法一：根据公式求解,2维
d1=np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

print d1

#方法二：根据scipy库求解，n维
X=np.vstack([x,y])
d2=1-pdist(X,'cosine')

print d2