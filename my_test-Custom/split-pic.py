# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.1.29 17:30
@Function:切割图片
'''

import cv2


# img = cv2.imread('/home/260158/company/test_pictures/pictures/geli.jpg')
#
# x = 0
# y = 0
# width = 1600
# height = 900
# image = cv.SetImageROI(img, (x, y, width, height))
# cv2.imshow('aa',image)
#
# if cv2.waitKey() == 27:
#     cv2.destroyAllWindows()

#提取出感兴趣的图像
# def imageROI():
img = cv2.imread("/home/260158/company/test_pictures/pictures/geli.jpg" )

print(img.shape)
#img.size返回图像的像素数目 = 高度 * 宽度 * 3（色彩通道）
# print(img.size)
# #img.dtype: 返回图像的数据类型
# print("图像的数据类型:")
# print(img.dtype)


image = img[0:2560 , 28000:28699 ]  #高 * 宽
# pic = cv2.resize(image,(2560,1500))
cv2.imwrite('/home/260158/company/test_pictures/pictures/hahaha/qwe/15.jpg',image)

# cv2.imshow("image" , image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# if __name__ == '__main__':
#     imageROI()




