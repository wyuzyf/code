# -*-coding:utf-8-*-
'''
@Author: Zhao Lu
@Time: 2018.3.31 10：46
@Function:minst应用
'''

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

#（1）加载数据 one_hot是一个长度为n的数组，只有一个元素是1.0
mnist = input_data.read_data_sets('/home/260158/code/tensorflow/MNIST_data/',one_hot=True)

#（2）构建回归模型
x = tf.placeholder(tf.float32, [None,784])   #占位符
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x,W) + b   #预测值

#定义损失函数和优化器
y_ = tf.placeholder(tf.float32, [None,10])

#计算预测值y和y_的差值，并取均值
# cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y,y_))
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y))
#采用SGD作为优化器
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


#(3)训练模型
sess = tf.InteractiveSession()     #交互式会话
tf.global_variables_initializer().run()  #初始化变量并在会话中启动模型

#Train
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)  #随机抓取100个数据点来替换之前的占位符
    sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
    if i % 100 ==0:
        print(sess.run(cross_entropy, feed_dict={x:batch_xs,y_:batch_ys}))
        print(sess.run(y, feed_dict={x: batch_xs, y_: batch_ys}))
        print(sess.run(y_, feed_dict={x: batch_xs, y_: batch_ys}),'\n\n')
        # print(y)
        # print(y_,'\n')

#(4)评估模型
correct_prediction = tf.equal(tf.arg_max(y,1), tf.arg_max(y_,1))  #y是预测值，y_是正确值
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))   #布尔型转化为浮点数，并取平均值

#计算模型在测试集上的准确率
print(sess.run(accuracy,feed_dict={x:mnist.test.images,
                                   y_:mnist.test.labels}))





