# -*-coding:utf-8-*-


import cv2
import datetime

img1 = cv2.imread('/home/260158/code/pictures-data/CMU0/medium00.JPG')

starttime = datetime.datetime.now()

fast = cv2.FastFeatureDetector_create(100)
kp = fast.detect(img1,None)
img2 = cv2.drawKeypoints(img1,kp,(0,0,255))

endtime = datetime.datetime.now()
a = endtime- starttime


#cv2.namedWindow('fast', cv2.WINDOW_NORMAL)

cv2.imshow('fast',img2)
cv2.waitKey(0)
print a

# a = 1
# b = 2
# c = (float) (a / b )
# print c