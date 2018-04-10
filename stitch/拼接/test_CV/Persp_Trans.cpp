/**********************************
@Author:Zhao Lu
@Time: Created on 2017-11-3  10：58
@Funtion: 测试Opencv自带透视变换函数
***********************************/

/*
#include <iostream>
#include "opencv2/core/core.hpp"
#include "highgui.h"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/opencv.hpp"

using namespace std;
//using namespace cv;

int main()

{
    //get original image
    cv::Mat originalImage = cv::imread("/home/260158/code/Haikang/pictures/test.png");

    //透视变换图像
    cv::Mat perspectiveImage;

    //perspective transform, we need four points
    cv::Point2f objectivePoints[4], imagePoints[4];

    //原始像素点的坐标,pictures 1020 * 647
    imagePoints[0].x = 10.0; imagePoints[0].y = 457.0;
    imagePoints[1].x = 395.0;imagePoints[1].y = 291.0;
    imagePoints[2].x = 624.0; imagePoints[2].y = 291.0;
    imagePoints[3].x = 1000.0;imagePoints[3].y = 457.0;

    //透视变换图像对应的目标点 提升和向左移动
    double moveValueX = 0.0;
    double moveValueY = 0.0;

    objectivePoints[0].x = 46.0 + moveValueX; objectivePoints[0].y = 920.0 + moveValueY;
    objectivePoints[1].x = 46.0 + moveValueX; objectivePoints[1].y = 100.0 + moveValueY;
    objectivePoints[2].x = 600.0 + moveValueX; objectivePoints[2].y = 100.0 + moveValueY;
    objectivePoints[3].x = 600.0 + moveValueX; objectivePoints[3].y = 920.0 + moveValueY;

    //求得变换矩阵
    cv::Mat transform = getPerspectiveTransform(objectivePoints, imagePoints);

    //透视变换函数
    cv::warpPerspective(originalImage,    //原始图像
                        perspectiveImage,   //透视变换后的图像
                        transform,
                        cv::Size(originalImage.rows, originalImage.cols),
                        cv::INTER_LINEAR | cv::WARP_INVERSE_MAP);

    cv::imshow("perspective image", perspectiveImage);
    cvWaitKey(0);

    cv::imwrite("/home/260158/code/Haikang/test_CV/perspectiveImage.png", perspectiveImage);

    return 0;

}

*/






















