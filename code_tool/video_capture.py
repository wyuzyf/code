# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.1.4 09:27
@Function:从智能眼睛读取视频流
'''

import os
import cv2


img_save_dir = "/home/260158/company/test_video/Webcam/"
if not os.path.exists(img_save_dir):
    os.makedirs(img_save_dir)

source = "rtmp://120.78.167.216:1935/live/stream_56"
cam = cv2.VideoCapture(source)
img_counter = 0
while(cam.isOpened()):
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if not ret:
        break
    # press ESC to escape (ESC ASCII value: 27)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    # press Space to capture image (Space ASCII value: 32)
    elif cv2.waitKey(1) & 0xFF == 32:
        print ("Saving image ...")
        img_file = img_save_dir + "/opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_file, frame)
        print ("WebCam Image {}: {} written!").format(img_counter, img_file)
        img_counter += 1
    else:
        pass

cam.release()
cv2.destroyAllWindows()
