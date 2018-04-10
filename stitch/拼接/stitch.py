#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:36:27 2017

@author: 260158
"""

import cv2

'''
@使用OopenCV自带的函数实现全景拼接
@param:
@return:
'''
def stitch():

    try_use_gpu = False   #不使用GPU
    #imgs = np.Mat()

    result_name = 'dst1.jpg'

    #pano = np.zeros(0)
    #pano2 = np.Mat()

    img1 = cv2.imread( '/home/260158/code/Haikang/pictures/yard1.jpg' )
    img2 = cv2.imread( '/home/260158/code/Haikang/7pictures/yard2.jpg' )
    #print img1

    cv2.imshow('p1', img1)
    cv2.imshow('p2', img2)

#        if img1.empty()  or  img2.empty():
#                print 'can not read image'



    #imgs = img1.append(img2)

    stitcher = cv2.createStitcher(try_use_gpu)

    result  = stitcher.stitch( (img1, img2) )

#        if status != cv2.Stitcher.OK:
#                print 'Can not stitch images, error code ='  and status

   cv2.imwrite(result_name, result[1])

    #pano2 = pano.clone()

   cv2.imshow('全景图像', result[1])
   if cv2.waitKey() == 27:
        return 0


if __name__ == '__main__':

    stitch()

































        
        
        
                
