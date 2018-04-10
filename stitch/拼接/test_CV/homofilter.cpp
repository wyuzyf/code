///**********************************
//@Author:Zhao Lu
//@Time: Created on 2017-11-22  15：18
//@Funtion: 同态滤波，解决光照不均匀的问题
//        ·(1)第一版的只能处理灰度图
// 查找资料了解到的：
// -->光线均匀（使图片整体亮度范围变小）
//    ex：白平衡；去除高光；背景相减；中值滤波；
// -->照片镜面反射消除算法（MIT）
//***********************************/
//#include <stdio.h>
//#include <iostream>
//#include <fstream>
//#include "opencv2/highgui/highgui.hpp"
//#include "opencv2/core/core.hpp"
//#include "opencv2/imgproc/imgproc.hpp"
//#include <opencv2/opencv.hpp>
//#include <opencv/cvaux.hpp>
//#include <highgui.h>

//using namespace cv;
//using namespace std;

//void my_HomoFilter(Mat srcImg, Mat &dst)
//{

//    srcImg.convertTo(srcImg, CV_64FC1);
//    dst.convertTo(dst, CV_64FC1);
//    //(1) ln
//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double* srcdata = srcImg.ptr<double>(i);
//        double* logdata = srcImg.ptr<double>(i);
//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            logdata[j] = log(srcdata[j]+0.0001);
//        }
//    }

//    //spectrum,光照分量
//    //(2) dct 离散余弦变换，变换到频域
//    Mat mat_dct = Mat::zeros(srcImg.rows, srcImg.cols, CV_64FC1);
//    dct(srcImg, mat_dct);
//    //imshow("dct", mat_dct);
//    cout<<'ok'<<endl;

//    //(3)linear filter
//    Mat H_u_v;
//    double gammaH = 1.5;
//    double gammaL = 0.5;
//    double C = 1;
//    double d0 = (srcImg.rows/2)*(srcImg.rows/2) + (srcImg.cols/2)*(srcImg.cols/2);
//    double d2 = 0;
//    H_u_v = Mat::zeros(srcImg.rows, srcImg.cols, CV_64FC1);

//    double totalWeight = 0.0;
//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double * dataH_u_v = H_u_v.ptr<double>(i);
//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            d2 = pow((i), 2.0) + pow((j), 2.0);
//            dataH_u_v[j] =  (gammaH - gammaL)*(1 - exp(-C*d2/d0)) + gammaL;
//            totalWeight += dataH_u_v[j];
//        }
//    }
//    H_u_v.ptr<double>(0)[0] = 1.1;

//    //H_u_v = Mat::ones(srcImg.rows, srcImg.cols, CV_64FC1);
//    //imshow("H_u_v", H_u_v);


//    //imshow("before filter", mat_dct);

//    mat_dct = mat_dct.mul(H_u_v);
//    //Mat tmp = mat_dct.mul(H_u_v);
//    //tmp.copyTo(mat_dct);
//    //（4） idct ，逆变换到空域
//    idct(mat_dct, dst);

//#if 0
//    //spatial high high pass filter
//    Mat tmp = Mat::zeros(srcImg.rows, srcImg.cols, CV_64FC1);
//    GaussianBlur(srcImg, tmp, Size(9, 9), 1.5, 1.5);
//    const double alpha = 0.5;

//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double* srcdata = srcImg.ptr<double>(i);
//        double* blurdata = tmp.ptr<double>(i);
//        double* dstdata = dst.ptr<double>(i);
//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            dstdata[j] = (1+alpha)*srcdata[j] - alpha*blurdata[j];
//            //dstdata[j] = blurdata[j];

//        }
//    }



//#endif
//    //(5) exp
//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double* srcdata = dst.ptr<double>(i);
//        double* dstdata = dst.ptr<double>(i);
//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            dstdata[j] = exp(srcdata[j]);
//        }
//    }

//    //imshow("dst", dst);
//    dst.convertTo(dst, CV_8UC1);

//}


//int main()
//{
//    int resize_width = 600;
//    int resize_height = 560;
//    Mat src_mat;

//    Mat src = imread("/home/260158/下载/彩图.jpg",0);   //灰度图
//    resize(src, src_mat, Size(resize_width, resize_height), (0, 0), (0, 0), INTER_LINEAR);
//    imshow("src", src_mat);
//    cvWaitKey(0);

//    Mat dst_mat(src_mat.rows, src_mat.cols, src_mat.type());
//    my_HomoFilter(src_mat, dst_mat);

//    imshow("dst", dst_mat);
//    cvWaitKey(0);

//    return 0;
//}
