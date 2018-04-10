/***********************************
@Author:Zhao Lu
@Time: Created on 2017-11-6  16：25
@Funtion: 测试Opencv自带图片拼接函数
************************************/


//#include <iostream>
//#include <opencv2/core/core.hpp>
//#include <opencv2/highgui/highgui.hpp>
//#include <opencv2/imgproc/imgproc.hpp>
//#include <opencv2/stitching/stitcher.hpp>

//#include <time.h>

//typedef long clock_t;

//using namespace std;
//using namespace cv;
//bool try_use_gpu = false;
//vector<Mat> imgs;
//string result_name = "/home/260158/code/Haikang/pictures/stitch_result/dst3.jpg";

//clock_t start,finish;
//double totaltime;
////time = string totaltime;

//int main()
//{
//    Mat img1 = imread("/home/260158/code/Haikang/pictures/church01.jpg");
//    Mat img2 = imread("/home/260158/code/Haikang/pictures/church02.jpg");

//    imshow("p1", img1);
//    imshow("p2", img2);

//    if (img1.empty() || img2.empty())
//    {
//        cout << "Can't read image" << endl;
//        return -1;
//    }
//    imgs.push_back(img1);
//    imgs.push_back(img2);

//    //进行计时
//    start = clock();
//    Stitcher stitcher = Stitcher::createDefault(try_use_gpu);
//    // 使用stitch函数进行拼接
//    Mat pano;
//    Stitcher::Status status = stitcher.stitch(imgs, pano);
//    finish = clock();

//    if (status != Stitcher::OK)
//    {
//        cout << "Can't stitch images, error code = " << int(status) << endl;
//        return -1;
//    }

//    totaltime = (double)(finish - start) / CLOCKS_PER_SEC;
//    cout << "\n此次拼接用时为"<<totaltime<< "秒！"<<endl;

//    imwrite(result_name, pano);
//    Mat pano2 = pano.clone();

//    // 显示源图像，和结果图像
//    imshow("全景图像", pano2);
//    if (waitKey() == 27)
//        return 0;
//}



















