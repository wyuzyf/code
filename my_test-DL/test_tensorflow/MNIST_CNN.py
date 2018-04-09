# -*-coding:utf-8-*-
'''
@Author: Zhao Lu
@Time: 2018.3.31 17：30
@Function:用CNN训练MNIST
'''

#1、加载数据
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data


#2、构建模型

#（1）定义输入数据并预处理数据。分别得到训练集和测试集的图片和标记的矩阵
mnist  = input_data.read_data_sets('/home/260158/code/tensorflow/MNIST_data/',one_hot=True)
trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels

trX = trX.reshape(-1, 28,28, 1)   #处理输入的训练数据 -1比表示不考虑输入图片的数量， 28*28是图片的像素数， 1表示一个通道（黑白）
teX = teX.reshape(-1,28,28,1)   #测试数据

X = tf.placeholder('float', [None, 28,28, 1])  #第一个参数是数据类型，第二个是数据的结构
Y = tf.placeholder('float', [None,10])

#（2）初始化权重和定义网络结构
'''
拥有3个卷积层和3个池化层，
随后接1个全连接层和1个输出层
'''
def init_weights(shape):
    return tf.Variable(tf.random_normal(shape,stddev=0.01))

#初始化权重
w = init_weights([3,3,1,32])    #patch大小为3*3，输入维度为1，输出维度为32
w2 = init_weights([3,3,32,64])
w3 = init_weights([3,3,64,128])
w4 = init_weights([128*4*4,625])   #全连接层，输入维度为128*4*4，是上一层的输出数据又三维的转变成一维，输出维度为625
w_o = init_weights([625,10])  #输出层，输入维度为10，代表10类（laabels）

'''
X:输入数据
w：每一层的权重
p_keep_conv, p_keep_hidden：dropout要保留的神经元比例
'''
def model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden):

    #第一组卷积层及池化层，最后dropout一些神经元
    l1a = tf.nn.relu(tf.nn.conv2d(X, w, strides=[1,1,1,1], padding='SAME'))
    l1 = tf.nn.max_pool(l1a,ksize=[1,2,2,1],strides=[1,2,2,1],padding=  'SAME')
    l1 = tf.nn.dropout(l1,p_keep_conv)

    #第二组卷积层及池化层，最后dropout一些神经元
    l2a = tf.nn.relu(tf.nn.conv2d(l1, w2, strides=[1,1,1,1], padding='SAME'))
    l2 = tf.nn.max_pool(l2a, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    l2 = tf.nn.dropout(l2, p_keep_conv)

    #第三组卷积层及池化层，最后dropout一些神经元
    l3a = tf.nn.relu(tf.nn.conv2d(l2, w3, strides=[1, 1, 1, 1], padding='SAME'))
    l3 = tf.nn.max_pool(l3a, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    l3 = tf.reshape(l3,[-1,w4.get_shape().as_list()[0]])
    l3 = tf.nn.dropout(l3, p_keep_conv)

    #全连接层，最后dropout一些神经元
    l4 = tf.nn.relu(tf.matmul(l3, w4))
    l4 = tf.nn.dropout(l4, p_keep_hidden)

    #输出层
    pyx = tf.matmul(l4, w_o)
    return pyx  #返回预测值

#生成网络模型
p_keep_conv = tf.placeholder('float32')  #表示在一层中有多少比例的神经元被保留下来
p_keep_hidden = tf.placeholder('float32')
py_x = model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden)


#（3）定义损失函数
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y))
train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)   #定义训练的操作
predict_op = tf.argmax(py_x, 1)   #返回最大的那个数值所在的下标
                        #axis = 1:等于1的时候，比较范围缩小了，只会比较每个数组内的数的大小，结果也会根据有几个数组，产生几个结果。


#3、训练模型和评估模型

#（1）定义训练和评估时的批次大小
batch_size = 128
test_size = 256

#（2）在一个会话中，开始训练和评估
with tf.Session() as sess:
    tf.global_variables_initializer().run()  #初始化所有变量

    for i in range(100):
        training_batch = zip(range(0, len(trX), batch_size),
                            range(batch_size, len(trX) + 1 , batch_size))
        for start, end in training_batch:
            sess.run(train_op, feed_dict={X:trX[start:end], Y:trY[start:end], p_keep_conv:0.8, p_keep_hidden:0.5})
            test_indices = np.arange(len(teX))
            np.random.shuffle(test_indices)
        test_indices = test_indices[0:test_size]

        print(i, np.mean(np.argmax(teY[test_indices], axis=1) ==
              sess.run(predict_op, feed_dict={X: teX[test_indices],
                                              p_keep_conv:1.0,
                                              p_keep_hidden:1.0})))







