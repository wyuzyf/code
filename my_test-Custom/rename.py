# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2017.11.30 11:34
@Function:对同一个文件夹中的图片按一定规则重命名
          # 重命名文件夹内的所有图像并写入txt，同时也可通过重写图像修改格式
          配用Opencv2.4.10
'''

import os

class BatchRename():
    def __init__(self):
        self.path = "/home/260158/pictures-data/my_VOC/JPEGImages/"   #原图片路径
        self.path_1 = "/home/260158/pictures-data/my_VOC/ImageSets/Main/train.txt"   #train.txt文件路径

    #重命名图片
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            if item.endswith('.jpg'):   #判断是否以指定后缀命名
                #os.path.join将多个路径组合后返回
                src = os.path.join(os.path.abspath(self.path), item)
                # dst = os.path.join(os.path.abspath(self.path), str(i) + '.jpg')
                dst = os.path.join(os.path.abspath(self.path), str("%06d" % i) + '.jpg')  #以6位数命名

                try:
                    os.rename(src, dst)   #自带重命名函数
                    print 'converting %s to %s ...' % (src, dst)
                    i = i + 1
                except:
                    continue

        print 'total %d to rename & converted %d jpgs' % (total_num, i)

    #提取图片名称，不包括后缀
    def extract_fname(self):
        names = os.listdir(self.path)  # 路径
        i = 0  # 用于统计文件数量是否正确，不会写到文件里
        train = open(self.path_1, 'w')
        for name in names:
            index = name.rfind('.')   #返回‘.’最后一次出现的位置
            name = name[:index]
            train.write(name + '\n')
            i = i + 1
        print '总共提取图片:', i


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
    demo.extract_fname()


