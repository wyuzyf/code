# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.1.20 17:27
@Function:测试梯度的计算
'''

import math

#example values
x = 3
y = -4

#forward pass
sigy = 1.0 / (1 + math.exp(-y)) #分子上的sigmod
num = x + sigy   #分子

sigx = 1.0 / (1 + math.exp(-x))  #分母上的sigmod
xpy = x + y
xpysqr = xpy**2
den = sigx + xpysqr  #分母
invden = 1.0 / den
f = num * invden  #函数构建完毕

# backprop f = num * invden
dnum = invden # gradient on numerator                             #(8)
dinvden = num                                                     #(8)
# backprop invden = 1.0 / den
dden = (-1.0 / (den**2)) * dinvden                                #(7)
# backprop den = sigx + xpysqr
dsigx = (1) * dden                                                #(6)
dxpysqr = (1) * dden                                              #(6)
# backprop xpysqr = xpy**2
dxpy = (2 * xpy) * dxpysqr                                        #(5)
# backprop xpy = x + y
dx = (1) * dxpy                                                   #(4)
dy = (1) * dxpy                                                   #(4)
# backprop sigx = 1.0 / (1 + math.exp(-x))
dx += ((1 - sigx) * sigx) * dsigx # Notice += !! See notes below  #(3)
# backprop num = x + sigy
dx += (1) * dnum                                                  #(2)
dsigy = (1) * dnum                                                #(2)
# backprop sigy = 1.0 / (1 + math.exp(-y))
dy += ((1 - sigy) * sigy) * dsigy                                 #(1)





