# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.1.25 09:19
@Function:再图片上写字
'''

# import cv2.cv as cv
#
# #创建一个窗口，命名为you need tostruggle,
# #cv.CV_WINDOW_AUTOSIZE这个参数设定显示窗口虽图片大小自动变化
# cv.NamedWindow('You need to struggle', cv.CV_WINDOW_AUTOSIZE)
#
# #加载一张图片，第二个参数指定当图片被加载后的格式，还有另外两个可选参数
# #CV_LOAD_IMAGE_GREYSCALE and CV_LOAD_IMAGE_UNCHANGED，分别是灰度格式和不变格式
# image=cv.LoadImage('/home/260158/图片/zyf.jpg', cv.CV_LOAD_IMAGE_COLOR)
#
# #创建一个矩形，来让我们在图片上写文字，参数依次定义了文字类型，高，宽，字体厚度等。。
# font=cv.InitFont(cv.CV_FONT_HERSHEY_SCRIPT_SIMPLEX, 1, 1, 0, 3, 8)
#
# #将文字框加入到图片中，(5,20)定义了文字框左顶点在窗口中的位置，最后参数定义文字颜色
# cv.PutText(image, "Hello World", (30,30), font, (0,255,0))
#
# #在刚才创建的窗口中显示图片
# cv.ShowImage('You need to struggle', image)
# cv.WaitKey(0)
#
# #保存图片
# cv.SaveImage('/home/260158/图片/', image)

# from PIL import Image, ImageDraw, ImageFont
# import cv2
# import numpy as np
#
#
# im = cv2.imread('/home/260158/图片/zyf.jpg')
# cv2_im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB) # cv2和PIL中颜色的hex码的储存顺序不同
# pil_im = Image.fromarray(cv2_im)
#
# draw = ImageDraw.Draw(pil_im) # 括号中为需要打印的canvas，这里就是在图片上直接打印
# font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8") # 第一个参数为字体文件路径，第二个为字体大小
# draw.text((175, 110), "eg：打印在这里", (0, 0, 255), font=font) # 第一个参数为打印的坐标，第二个为打印的文本，第三个为字体颜色，第四个为字体
#
# cv2_text_im = cv2.cvrColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
# cv2.imshow("a", cv2_text_im)



import cv2
import numpy as np

# 原始图片
img = cv2.imread('/home/260158/图片/zyf.jpg')
image = cv2.resize(img,(1920,1080))
# cv2.imshow('Original image', image)


# # 在图片上画一个框
# imageRect = image.copy()
# p1 = (300, 200)
# p2 = (500, 300)
# color = (0, 0, 255)  # BGR的顺序，这个颜色为红色
# cv2.rectangle(imageRect, p1, p2, color)
# cv2.imshow('Rectangle an image', imageRect)
#
# # 保留单一通道色彩，通道顺序是BGR
# b = image.copy()
# b[:, :, 1] = 0
# b[:, :, 2] = 0
# cv2.imshow('Blue image', b)
#
# g = image.copy()
# g[:, :, 0] = 0
# g[:, :, 2] = 0
# cv2.imshow('Green image', g)
#
# r = image.copy()
# r[:, :, 1] = 0
# r[:, :, 0] = 0
# cv2.imshow('Red image', r)
#
# # 改变对比度和亮度
# # 公式
# # result = ori*alpha + beta
# # ndarray是直接支持乘法和加法操作的，但是要注意
# # 乘加后的结果必须在[0,255]范围内，所以稍做一下处理
# alpha = 2
# beta = -200
# # result1 = image*2 - 200 #直接这么处理会有问题，会不在范围
# p = []
# for i in range(256):
#     p.append(max(min(round(alpha * i + beta), 255), 0))
# parray = np.array(p, np.uint8)
# result = parray[image]
# cv2.imshow('Change contrast and brightness', result)


# 显示文字
imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 0, 0), thickness=4, lineType=8)
cv2.putText(imageText, 'Z Y F', (500, 600), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 10, (255, 255, 255),thickness=4, lineType=8)
cv2.imshow('a', imageText)
cv2.imwrite('/home/260158/company/test_pictures/pictures/ayf3.jpg',imageText)


# # 字体：FONT_HERSHEY_COMPLEX_SMALL
# imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_COMPLEX_SMALL, 4,
#             (255, 0, 0), thickness=4, lineType=8)
# cv2.imshow('Show text FONT_HERSHEY_COMPLEX_SMALL', imageText)
#
#
# # 字体：FONT_HERSHEY_DUPLEX
# imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_DUPLEX, 4, (255, 0, 0),
#             thickness=4, lineType=8)
# cv2.imshow('Show text FONT_HERSHEY_DUPLEX', imageText)
#
#
# # 字体：FONT_HERSHEY_PLAIN
# imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0),
#             thickness=4, lineType=8)
# cv2.imshow('Show text FONT_HERSHEY_PLAIN', imageText)
#
#
# # 字体：FONT_HERSHEY_SCRIPT_COMPLEX
# imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4,
#             (255, 0, 0), thickness=4, lineType=8)
# cv2.imshow('Show text FONT_HERSHEY_SCRIPT_COMPLEX', imageText)
#
#
# # 字体：FONT_HERSHEY_SCRIPT_SIMPLEX
# imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4,
#             (255, 0, 0), thickness=4, lineType=8)
# cv2.imshow('Show text FONT_HERSHEY_SCRIPT_SIMPLEX', imageText)
#
#
# # 字体：FONT_HERSHEY_SIMPLEX
# imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_SIMPLEX, 4,
#             (255, 0, 0), thickness=4, lineType=8)
# cv2.imshow('Show text FONT_HERSHEY_SIMPLEX', imageText)
#
#
# # 字体：FONT_HERSHEY_TRIPLEX
# imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_HERSHEY_TRIPLEX, 4,
#             (255, 0, 0), thickness=4, lineType=8)
# cv2.imshow('Show text FONT_HERSHEY_TRIPLEX', imageText)
#
#
# # 字体：FONT_ITALIC
# imageText = image.copy()
# cv2.putText(imageText, 'cly', (imageText.shape[0] / 2, imageText.shape[1] / 3), cv2.FONT_ITALIC, 4, (255, 0, 0),
#             thickness=4, lineType=8)
# cv2.imshow('Show text FONT_ITALIC', imageText)


# 退出窗口
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

