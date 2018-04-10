#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")
img3 = cv2.imread("3.jpg")

img4 = cv2.imread("4.jpg")
img5 = cv2.imread("5.jpg")
img6 = cv2.imread("6.jpg")

# resize to same scale
im1 = cv2.resize(img1, (320, 240))
im2 = cv2.resize(img2, (320, 240))
im3 = cv2.resize(img3, (320, 240))

im4 = cv2.resize(img4, (320, 240))
im5 = cv2.resize(img5, (320, 240))
im6 = cv2.resize(img6, (320, 240))

hmerge_1 = np.hstack((im1, im2,im3) )#水平拼接
hmerge_2 = np.hstack((im4, im5,im6)) #水平拼接

vmerge = np.vstack( ( hmerge_1 , hmerge_2 ) )                  

cv2.imshow("test1", hmerge_1)
cv2.imshow("test2", hmerge_2)
cv2.imshow("test3", vmerge)

#cv2.imshow("test2", vmerge)

cv2.waitKey(0)
cv2.destroyAllWindows()
