# -*-coding:utf-8-*-
'''
@Author: Zhao Lu
@Time: 2018.3.30 14：58
@Function:第一个tensorflow程序
'''

import tensorflow as tf
import numpy as np

#（1）生成及加载数据
'''
#构造满足一元二次方程的函数
'''
x_data = np.linspace(-1,1,300)[:,np.newaxis]  #生成等差数列，300个点分布到（-1，1）
# print(x_data)
noise = np.random.normal(0,0.05,x_data.shape) #均值为0，方差为0.05的正态分布
y_data = np.square(x_data)-0.5 + noise  #y=x^2-0.5+噪声

#x,y的占位符，作为将要输入神经网络的变量
xs = tf.placeholder(tf.float32,[None, 1])
ys = tf.placeholder(tf.float32,[None, 1])

#(2)构建网络模型
'''
一个隐藏层，一个输出层，4个变量，输入数据及维度，输出数据的维度，激活函数
'''
def add_layer(inputs,in_size,out_size,activatiion_function=None):

    #构建权重：in_size * out_size的矩阵
    weights = tf.Variable(tf.random_normal([in_size,out_size]))


    #构建偏置：1 * out_size的矩阵
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    #print(biases)

    #矩阵相乘
    Wx_plus_b = tf.matmul(inputs,weights) + biases
    if activatiion_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activatiion_function(Wx_plus_b)

    # print(weights)
    return outputs


#构建隐藏层,有10个神经元
h1 = add_layer(xs,1,20,activatiion_function = tf.nn.relu)


#构建输出层,输出层和输入层一样，有1个神经元
prediction = add_layer(h1,20,1,activatiion_function=None)

#计算预测值和真实值之间的误差
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1])) #平方求和再取平均值
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  #梯度下降进行训练


#（3）训练模型
'''
训练1000次，每50次输出训练的损失值
'''
a = 0
b = 0
init = tf.global_variables_initializer()  #初始化所有变量
sess = tf.Session()  #创建会话
sess.run(init)

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})

    if i % 50 == 0:
        print(x_data)
        b = b+1  #输出20个值
    a = a+1
    print(a)
    print(b)
        # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))

'''
输出数据，输入数据
总个300个输入数据，将这300个数据连续带入计算y值，计算1000次，
每次都会得到一个w和b，连续使用GD1000次
会输出300个y值
'''



