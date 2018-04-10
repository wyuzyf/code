# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2017.11.20 11:16
@Function:在同一坐标系下的图片旋转
@Q: 有问题，实现效果不好
'''

import cv2
import matplotlib.pyplot as plt
import math

img = cv2.imread('/home/260158/code/pictures-data/pictures/1.jpg')
rows,cols = img.shape[:2]
angle = 30


'''
@前提是以图片中心点为旋转中心
 获得旋转后最大的x,y坐标的绝对值，
 解决图片显示不完整的问题
'''
def MAX_axis():

    #角度变弧度
    anglePi = angle * math.pi / 180.0
    cosA = math.cos(anglePi)
    sinA = math.sin(anglePi)


    #ceil():返回大于或者等于指定表达式的最小整数
    X1 = math.ceil(abs(0.5 * rows * cosA + 0.5 * cols * sinA))
    Y1 = math.ceil(abs(-0.5 * rows * sinA + 0.5 * cols * cosA))
    X2 = math.ceil(abs(0.5 * rows * cosA - 0.5 * cols * sinA))
    Y2 = math.ceil(abs(-0.5 * rows * sinA - 0.5 * cols * cosA))
    H = int(2 * max(Y1,Y2))
    W = int(2 * max(X1,X2))

    for i in range(rows):
            for j in range(cols):
                x = int(cosA * i-sinA * j - 0.5 * cols * cosA+0.5 * rows * sinA + 0.5 * W)
                y = int(sinA * i+cosA * j - 0.5 * cols * sinA-0.5 * rows * cosA + 0.5 * H)

    return x,y


cols_1, rows_1 = MAX_axis()

'''
@获得图像绕着某一点的旋转矩阵
@getRotationMatrix2D(),params:
                        (1)旋转中心;
                        (2)旋转角度;
                        (3)缩放比例;
'''
R = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 0.5)
#R = cv2.getRotationMatrix2D((0,0), angle, 0.72)


'''
@得到仿射变换后的图片
@warpAffine(),params:
                src: 输入源图像
                warp_dst: 输出图像
                warp_mat: 仿射变换矩阵
                warp_dst.size(): 输出图像的尺寸
'''
res = cv2.warpAffine(img, R, (cols_1,rows_1))
# borderColor = cv2.scalar(0, 238, 0);
# res = cv2.warpAffine(img, R, (cols,rows),cv2.INTER_LINEAR, cv2.BORDER_REPLICATE)

retval, dst = cv2.threshold(res, 0, 255, cv2.THRESH_BINARY)
#将阈值设置为50，阈值类型为cv2.THRESH_BINARY，则灰度在大于50的像素其值将设置为255，其它像素设置为0


cv2.imshow('img',img)
# cv2.imshow('res',res)
cv2.imshow('dst',dst)
#cv2.imwrite('Rotation1.jpg',res)
cv2.waitKey(0)






