# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2017.12.20 19:25
@Function:串接俩个路径的图片，并将拼接好的图片合成视频
'''

import numpy as np
import cv2
import time
import os

class Merge_Pic():

    def __init__(self):
        self.path_1 = '/home/260158/company/yolo-pic/Kong_Three/3_4_2_12_a/'  #原图片路径
        self.path_2 = '/home/260158/company/yolo-pic/Kong_Four/3_Han/'   #原图片路径
        self.path_3 = '/home/260158/company/test_video/'    #合成视频后的路径
        self.path_4 = '/home/260158/company/yolo-pic/aaa/'  #串接图片后的路径

        self.fps = 10
        self.fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self.video = 'aaa.avi'  #合成视频名
        self.resolution = (1280,480)  #合成视频的分辨率

    #对文件夹下的图片按名称进行升序
    def sort(self):
        fileslist = os.listdir(self.path_1)  #图片列表
        total_num = len(fileslist)

        #将数字排序
        for i in range(total_num):
            fileslist[i] = fileslist[i].split('.')
            fileslist[i][0] = int(fileslist[i][0])
            fileslist.sort

        #加‘.jpg’后排序
        for i in range(total_num):
            fileslist[i][0] = str(fileslist[i][0])
            fileslist[i] = fileslist[i][0] + '.' + fileslist[i][1]
        return fileslist

    def sort_1(self):
        fileslist = os.listdir(self.path_2)  #图片列表
        total_num = len(fileslist)

        #将数字排序
        for i in range(total_num):
            fileslist[i] = fileslist[i].split('.')
            fileslist[i][0] = int(fileslist[i][0])
            fileslist.sort

        #加‘.jpg’后排序
        for i in range(total_num):
            fileslist[i][0] = str(fileslist[i][0])
            fileslist[i] = fileslist[i][0] + '.' + fileslist[i][1]
        return fileslist

    def sort_2(self):
        fileslist = os.listdir(self.path_4)  #图片列表
        total_num = len(fileslist)

        #将数字排序
        for i in range(total_num):
            fileslist[i] = fileslist[i].split('.')
            fileslist[i][0] = int(fileslist[i][0])
            fileslist.sort   #python2 是fileslist.sort()

        #加‘.jpg’后排序
        for i in range(total_num):
            fileslist[i][0] = str(fileslist[i][0])
            fileslist[i] = fileslist[i][0] + '.' + fileslist[i][1]
        return fileslist

    #开始串接图片
    def merge(self):
        imgs_1 = demo.sort()
        imgs_2 = demo.sort_1()

        num = len(imgs_1)

        img1 = [0 for x in range(num)]
        img2 = [0 for x in range(num)]
        hmerge = [0 for x in range(num)]

        start = time.clock()
        for i in range(num):
            img1[i] = cv2.imread(self.path_1 + imgs_1[i])   #一定要加上路径
            img2[i] = cv2.imread(self.path_2 + imgs_2[i])

            hmerge[i] = np.hstack((img1[i],img2[i]))

            cv2.imwrite('/home/260158/company/yolo-pic/test/' + str(i) + '.jpg', hmerge[i])
            print (i)

        end = time.clock()
        print (end - start)

    def Video(self):
        pic = []
        frame = []
        out_video = cv2.VideoWriter(self.path_3 + self.video,self.fourcc,self.fps,self.resolution)
        pic = demo.sort_2()

        start = time.clock()
        for i in range(len(pic)):
            frame = cv2.imread(self.path_4 + pic[i])
            out_video.write(frame)  #合成视频
            print (i)  #合成第几张图片

        out_video.release()
        end = time.clock()
        print (end - start)



if __name__ == '__main__':
    demo = Merge_Pic()
    # demo.merge()
    demo.Video()













