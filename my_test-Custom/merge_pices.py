# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.2.7 09:03
@Function:串接一个路径下的多张图片
'''

import cv2
import numpy as np
import os
import time

# def merge():

# fileslist = os.listdir('/home/260158/company/test_pictures/pictures/hahah1/')  # 图片列表
# total_num = len(fileslist)

# img1 = [0 for x in range(total_num)]
# img2 = [0 for x in range(total_num)]
# hmerge = [0 for x in range(total_num)]
start = time.clock()
# for i in range(total_num):
img1 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/1.jpg')  # 一定要加上路径
img2 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/2.jpg')
img3 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/3.jpg')
img4 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/4.jpg')
img5 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/5.jpg')
img6 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/6.jpg')
img7 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/7.jpg')
img8 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/8.jpg')
img9 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/9.jpg')
img10 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/10.jpg')
img11 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/11.jpg')
img12 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/12.jpg')
img13 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/13.jpg')
img14 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/14.jpg')
img15 = cv2.imread('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/qwe/15.jpg')


hmerge = np.hstack((img1, img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15))

cv2.imwrite('/home/260158/code/face-detection/mxnet-finding-tiny-face/results/finally.jpg', hmerge)
# cv2.imshow('sf',hmerge)
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()
# print(i)

end = time.clock()
print(end - start)


# if __name__ == 'main':
#     merge()
