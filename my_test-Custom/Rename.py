# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2017.12.21 16:17
@Function:重命名文件夹下的文件名
'''

import os
import time

class Rename():
    def __init__(self):
        self.path = '/home/260158/company/yolo-pic/test/'       #原图片路径
        self.path_1 = '/home/260158/company/yolo-pic/test1/'    #修改后路径


    #对文件夹下的图片先按名称进行升序
    def sort(self):
        fileslist = os.listdir(self.path)  # 图片列表
        total_num = len(fileslist)

        # 将数字排序
        for i in range(total_num):
            fileslist[i] = fileslist[i].split('.')
            fileslist[i][0] = int(fileslist[i][0])
            fileslist.sort()

        # 加‘.jpg’后排序
        for i in range(total_num):
            fileslist[i][0] = str(fileslist[i][0])
            fileslist[i] = fileslist[i][0] + '.' + fileslist[i][1]
        return fileslist

    #对排好序的图片重命名
    def rename(self):
        files = demo.sort()
        total_num = len(files)
        a = 1800

        for item in files:
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(self.path),item)
                dst = os.path.join(os.path.abspath(self.path_1),str(a) + '.jpg')
                os.rename(src,dst)
                a = a + 1
                print a

        print 'total %d to rename & converted %d jpgs' % (total_num,a)


if __name__ == '__main__':
    start = time.clock()
    demo = Rename()

    demo.rename()
    end = time.clock()
    print end - start




