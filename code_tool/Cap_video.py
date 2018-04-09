# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.1.3 09:13
@Function:从已保存的视频中截取图片帧
'''

import cv2
# import numpy as np
import time


def cap():
    # cap = cv2.VideoCapture('/home/260158/company/test_video/1.mkv')  #原视频地址

    cap = cv2.VideoCapture(0)

    print ('Capture ok')

    framenum = 0
    fpsnum = 1

    while(cap.isOpened()):
        success,frame = cap.read()

        # print (success,frame)

        if success == True:
            framenum += 1
            if framenum % 10 == 1:
                # re_frame = cv2.resize(frame,(640,480))
                cv2.imwrite('/home/260158/company/test_video/2/' + str(fpsnum) + '.jpg',frame)  #图片的地址
                print (fpsnum)
                fpsnum += 1
        else:
            break
    print ('video capture success')
    cap.release()


if __name__ == '__main__':
    start = time.clock()
    cap()
    end = time.clock()
    print (end - start)
