# -*- coding: utf-8 -*-
'''
@Author: Zhao YinFa
@Time: 2018.2.1 16:53
@Function:在OpenCV中通过图片的URL地址获取图片
'''
import numpy as np
import urllib.request
import cv2


# URL到图片
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    # bytearray将数据转换成（返回）一个新的字节数组
    # asarray 复制数据，将结构化数据转换成ndarray
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    # cv2.imdecode()函数将数据解码成Opencv图像格式
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image


# initialize the list of image URLs to download
urls = [
    "http://npic7.edushi.com/cn/zixun/zh-chs/2017-12/15/7dd397ae82be483a9f5edf042a9572a0.jpg"

]

# loop over the image URLs
for url in urls:
    # download the image URL and display it
    print("downloading %s" % (url))
    image = url_to_image(url)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


