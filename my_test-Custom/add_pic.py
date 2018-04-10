# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.1.17 10:25
@Function:将多个视频流显示再同一个区域
Q：如果显示器的分辨率变了，那代码也得变化
'''

import cv2


# 调整图片的显示位置
# img = cv2.imread('/home/260158/company/test_pictures/pictures/1.jpg')
# image = cv2.resize(img,(640,480))
# cv2.namedWindow('aa')
# cv2.moveWindow('aa',600,100)
# cv2.imshow('aa',image)
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()


#调整视频的显示位置
# source = '/home/260158/company/test_video/1_1.avi'
# cam = cv2.VideoCapture(source)
# img_counter = 0
# while(cam.isOpened()):
#     ret, frame = cam.read()
#     image = cv2.resize(frame, (640, 480))
#     cv2.namedWindow('aa')
#     cv2.moveWindow('aa',0, 500)
#     cv2.imshow("aa", frame)
#     if cv2.waitKey(100) == 27:  #or if cv2.waitKey(100) == ord('q')
#         break
#
# cam.release()
# cv2.destroyAllWindows()



