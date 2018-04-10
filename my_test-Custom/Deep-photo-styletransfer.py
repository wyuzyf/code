# -*- coding: utf-8 -*-
'''
@Author: Zhao YinFa
@Time: 2018.2.2 09:52
@Function:实现滤镜,失败
'''

import numpy as np
import cv2

#提取天空区域
# def skyRegion():
#     iLow = np.array([100,43,46])
#     iHigh = np.array([124,255,255])
#     img = cv2.imread('/home/260158/company/test_pictures/pictures/hehe/mmexport1517492834999.jpg')
#     imgOriginal = cv2.imread('/home/260158/company/test_pictures/pictures/hehe/mmexport1517492834999.jpg')
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     # cv2.imshow('a',img)
#     # if cv2.waitKey(0) == 27:
#     #     cv2.destroyAllWindows()
#
#     #HSV split
#     h,s,v = cv2.split(img)
#     v = cv2.equalizeHist(v)  #直方图均衡化，该函数能归一化图像亮度和增强对比度
#     hsv = cv2.merge((h,s,v))
#
#     imgThresholded = cv2.inRange(hsv,iLow,iHigh)   #实现二值化功能（这点类似threshold()函数），更关键的是可以同时针对多通道进行操作，使用起来非常方便！
#     imgThresholded = cv2.medianBlur(imgThresholded,9) #中值滤波是一种典型的非线性滤波，是基于排序统计理论的一种能够有效抑制噪声的非线性信号处理技术，
#                                                       # 基本思想是用像素点邻域灰度值的中值来代替该像素点的灰度值，让周围的像素值接近真实的值从而消除孤立的噪声点。
#                                                       # 该方法在取出脉冲噪声、椒盐噪声的同时能保留图像的边缘细节
#
#     #open 运算
#     kernel = np.ones((5,5),np.uint8) #创建元素全为1的数组
#     imgThresholded=  cv2.morphologyEx(imgThresholded,cv2.MORPH_OPEN,kernel,iterations=10)  #形态学函数，开运算
#     imgThresholded = cv2.medianBlur(imgThresholded,9)
#
#     image = cv2.resize(imgThresholded,(1280,720))
#     cv2.imshow('aa',image)
#     if cv2.waitKey(0) == 27:
#         cv2.destroyAllWindows()
    # cv2.imwrite('/home/260158/company/test_pictures/pictures/hehe/otp.jpg',image)
    # return image



#泊松融合
'''
skyname-- '新海城'画风的图片 
picname--要融合的图片 自己的图片
maskname--天空mask，即上面得到的结果
'''
def seamClone():

    skyname = '/home/260158/company/test_pictures/style/2.png'
    picname = '/home/260158/company/test_pictures/pictures/hehe/mmexport1517492834999.jpg'
    maskname = '/home/260158/company/test_pictures/pictures/hehe/otp.jpg'
    #read images
    src = cv2.imread(skyname)  #源文件
    dst = cv2.imread(picname)   #目标文件

    src_mask = cv2.imread(maskname,0)
    # src_mask0 = cv2.imread(maskname)
    contours = cv2.findContours(src_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    cnt = contours[0]

    # cv2.imshow('aa3', cnt)
    # if cv2.waitKey(0) == 27:
    #     cv2.destroyAllWindows()

    x,y,w,h = cv2.boundingRect(cnt)
    print(x,y,w,h)
    if w == 0 or h == 0:
        return dst
    # dst_x = len(dst[0])
    # dst_y = len(dst[1])
    # src_x = len(src[0])
    # # print(src_x)
    # src_y = len(src[1])
    # scale_x = w*1.0 / src_x
    src1 = cv2.resize(src,(1280,720),interpolation=cv2.INTER_CUBIC)


    # cv2.imwrite('src_sky.jpg',src)
    center =(int((x+w) / 2),int((y+h) / 2))

    print(center)

    output = cv2.seamlessClone(src1,dst,src_mask,center,cv2.NORMAL_CLONE)
    # return output
    img = cv2.resize(output,(1600,1080))
    cv2.imshow('aa', img)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

#对色卡操作
# def myFilter(orimap,newmap,picname):
#     ori = cv2.imread(orimap)
#     new = cv2.imread(newmap)
#     my = cv2.imread(picname)
#
#     pic_name = picname.split('/')[-1].split('.')[0]
#     style_name = newmap.split('/')[-1].split('.')[0]
#
#     tmp = 'tmp/' + pic_name + '-' + style_name + '.jpg'
#
#     #filter
#     for i in range(len(my)):
#         for j in range(len(my[0])):
#             pos = findPos(my[i][j],ori)
#             my[i][j] = new[pos[0],pos[1]]
#     cv2.imwrite(tmp,my)
#
#     return tmp



# skyRegion()
# seamClone()


# Read images


src = cv2.imread("/home/260158/company/test_pictures/pictures/airplane.jpg")

# src1 = cv2.resize(src,(640,480))
dst = cv2.imread("/home/260158/company/test_pictures/pictures/sky.jpg")
# dst1 = cv2.resize(dst,(1600,900))

# Create a rough mask around the airplane.
src_mask = np.zeros(src.shape, src.dtype)
# print(src_mask.shape)

poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))  #填充多边形
# cv2.imshow('aaf', src_mask)
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()


# This is where the CENTER of the airplane will be placed
center = (800,100)

# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)
cv2.imwrite('/home/260158/company/test_pictures/pictures/aaaaaa.jpg',output)
# ss = cv2.resize(output,(1600,900))
# cv2.imshow('aa', output)
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()








