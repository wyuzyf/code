/**********************************
@Author:Zhao Lu
@Time: Created on 2017-11-21  10：58
@Funtion: 测试在同一坐标系下的旋转，尺度不变
***********************************/

//#include <iostream>
//#include "opencv2/highgui/highgui.hpp"
//#include "opencv2/core/core.hpp"
//#include "opencv2/imgproc/imgproc.hpp"

////using namespace cv;
//using namespace std;

//int main()
//{
//    cv::Mat src = cv::imread("/home/260158/code/pictures-data/pictures/1.jpg");
//    cv::Mat dst;
//    //float scale = 200.0/ src.rows;//缩放因子
//    //cv::resize(src, src, cv::Size(), scale, scale, cv::INTER_LINEAR);
//    //旋转角度-20度
//    double angle = -20;
//    //输出图像的尺寸与原图一样
//    cv::Size dst_sz(src.cols, src.rows);

//    //指定旋转中心
//    cv::Point2f center(src.cols / 2., src.rows / 2.);

//    //获取旋转矩阵（2x3矩阵）
//    cv::Mat rot_mat = cv::getRotationMatrix2D(center, angle, 0.78);
//    //设置选择背景边界颜色：绿色
////    cv::Scalar borderColor = cv::Scalar(0, 238, 0);
////    cv::warpAffine(src, dst, rot_mat, src.size(), cv::INTER_LINEAR, cv::BORDER_CONSTANT, borderColor);
//    cv::warpAffine(src, dst, rot_mat, dst_sz, cv::INTER_LINEAR, cv::BORDER_REPLICATE);


//    //显示旋转效果
//    cv::imshow("src image ", src);
//    cv::imshow("Rotation Image", dst);
//    cv::waitKey(0);
//    cv::imwrite("Rotation Image.jpg",dst);

//    return 0;

//}
