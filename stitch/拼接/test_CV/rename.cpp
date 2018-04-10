/**********************************
@Author:Zhao Lu
@Time: Created on 2017-11-30  09：52
@Funtion: 对同一个文件夹中的图片按一定规则重命名
          重命名文件夹内的所有图像并写入txt，同时也可通过重写图像修改格式
          配用Opencv2.4.10
Q:找不到 io.h ，进而报错：没有声明_finddata_t
***********************************/


//#include "stdafx.h"
#include "sys/io.h"
//#include "io.h"

//#include <dirent.h>
//#include <sys/types.h>
//#include <sys/stat.h>

#include "stdlib.h"
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <opencv2/opencv.hpp>
#define IMGNUM 20000 //图片所在文件夹中图片的最大数量
char img_files[IMGNUM][1000];

using namespace cv;
using namespace std;

int getFiles(char *path)
{
    int num_of_img = 0;
    long   hFile = 0;

    struct _finddata_t fileinfo;

    char p[700] = { 0 };
    strcpy(p, path);
//    strcat(p, "\\*");
    strcat(p,"/*");

    if ((hFile = _findfirst(p, &fileinfo)) != -1)
    {
        do
        {
            if ((fileinfo.attrib & _A_SUBDIR))
            {
                if (strcmp(fileinfo.name, ".") != 0 && strcmp(fileinfo.name, "..") != 0)
                    continue;
            }
            else
            {
                strcpy(img_files[num_of_img], path);
//                strcat(img_files[num_of_img], "\\");
                strcat(img_files[num_of_img], "/");

                strcat(img_files[num_of_img++], fileinfo.name);
            }
        }
        while (_findnext(hFile, &fileinfo) == 0);
        _findclose(hFile);
    }
    return num_of_img;
}


int main()
{
//    char path[] = "SrcImage";                               //source image
    char path[] = "/home/260158/pictures-data/mark-pic/video3/images/";

//    char dstpath[] = "DstImage";                            //destination image
    char dstpath[] = "/home/260158/pictures-data/my_VOC/JPEGImages/";

    int num = getFiles(path);
    int i;
    char order[1000];
    FILE *fp = fopen("train.txt", "w");
    for (i = 0; i<num; ++i)
    {
        printf("%s\n", img_files[i]);
        IplImage *pSrc = cvLoadImage(img_files[i]);
        sprintf(order, "/home/260158/pictures-data/my_VOC/JPEGImages/%05d.jpg", i);
        fprintf(fp, "%05d\n", i);
        cvSaveImage(order, pSrc);
        printf("Saving %s!\n", order);
        cvReleaseImage(&pSrc);
    }
    fclose(fp);
    return 0;
}
