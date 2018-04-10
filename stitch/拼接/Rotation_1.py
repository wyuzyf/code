# -*-coding:utf-8-*-

'''
@Author: Zhao YinFa
@Time: 2017.11.20 15:00
@Function:在同一坐标系下的图片旋转,保持前景尺度不变
'''

import cv2
from math import *
import numpy as np


img = cv2.imread("/home/260158/code/pictures-data/pictures/2.jpg")
#img = cv2.imread('/home/260158/下载/R.png')
height,width=img.shape[:2]
# print img.shape

'''
#(1)如何计算这个旋转角度
    根据俩个点的坐标来计算旋转角度
'''
# cos(theta) = np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))  #这个是cos(theta)
# degree = math.acos(cos(theta)) * 180  / math.pi    #弧度转换为角度
degree=-30

'''
(2) 旋转后的尺寸
    @radians(),角度转换为弧度,计算出的是新图像的w,h的坐标
    h = w*sin(theta) + h*cos(theta)
    w = h*sin(theta) + w*cos(theta)
'''
heightNew=int(width * fabs(sin(radians(degree))) + height*fabs(cos(radians(degree))))
widthNew=int(height * fabs(sin(radians(degree))) + width*fabs(cos(radians(degree))))


'''
(3) 求旋转矩阵，以图片中心点为旋转中心
    @getRotationMatrix2D()返回一个2 * 3 矩阵，可以看成是一个2维的数组
'''
matRotation = cv2.getRotationMatrix2D((width/2,height/2),degree,1)
# print matRotation

'''
@旋转矩阵的第1行第3列，和第2行第3列是引入齐次坐标后的平移值，
 参考点是图片的坐标中心
'''
matRotation[0,2] +=(widthNew-width)/2
matRotation[1,2] +=(heightNew-height)/2
# print matRotation

'''
(4)最后得到的图像，边界是黑色
'''
imgRotation = cv2.warpAffine(img, matRotation, (widthNew,heightNew), borderValue=(0,0,0))

#我把像素值 > 0 的区域提取出来
#作二值化，将阈值设置为50，阈值类型为cv2.THRESH_BINARY，则灰度在大于50的像素其值将设置为255，其它像素设置为0
#retval, dst = cv2.threshold(imgRotation, 50, 255, cv2.THRESH_BINARY)

cv2.imshow("img",img)
cv2.imshow("imgRotation",imgRotation)
#cv2.imwrite("imgRotation_1.jpg",imgRotation)
cv2.waitKey(0)



