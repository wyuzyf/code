///**********************************
//@Author:Zhao Lu
//@Time: Created on 2017-11-22  15：18
//@Funtion: 同态滤波，解决光照不均匀的问题
//***********************************/

//#include <stdio.h>
//#include <iostream>
//#include <opencv2/opencv.hpp>
//#include <opencv2/highgui/highgui.hpp>
//#include <opencv/cvaux.hpp>
//#include <fstream>
//#include <highgui.h>
//#include <iostream>

//#define BYTE unsigned char

//using namespace cv;
//using namespace std;

//void test();

//void HomoFilter(Mat srcImg, Mat &dst);
//void my_HomoFilter(Mat srcImg, Mat &dst);



//void test()
//{
//    printf("hello\n");
//}



//void HomoFilter(Mat srcImg, Mat &dst)
//{
//    srcImg.convertTo(srcImg, CV_64FC1);
//    dst = Mat::zeros(srcImg.rows, srcImg.cols, CV_64FC1);

//    // 构造滤波矩阵
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
//            d2 = pow((i - srcImg.rows/2), 2.0) + pow((j - srcImg.cols/2), 2.0);
//            dataH_u_v[j] = 	(gammaH - gammaL)*(1 - exp(-C*d2/d0)) + gammaL;
//            totalWeight += dataH_u_v[j];
//        }
//    }

//    double gain = (srcImg.rows*srcImg.cols)/totalWeight;
//    //double gain = 2;
//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double * dataH_u_v = H_u_v.ptr<double>(i);
//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            //d2 = pow((i - srcImg.rows/2), 2.0) + pow((j - srcImg.cols/2), 2.0);
//            dataH_u_v[j] *= gain;
//            //totalWeight += dataH_u_v[j];
//        }
//    }

//    imshow("H_u_v", H_u_v);
//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double* srcdata = srcImg.ptr<double>(i);
//        //uint8_t* srcdata = srcImg.ptr<uint8_t>(i);
//        double* logdata = dst.ptr<double>(i);
//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            logdata[j] = log(srcdata[j]+0.0001);
//        }
//    }

//    /****************************傅里叶变换、滤波、傅里叶反变换*****************************/
//    Mat planes[] = {dst, Mat::zeros(dst.size(), CV_64F)};
//    Mat complexI;
//    merge(planes, 2, complexI); // Add to the expanded another plane with zeros
//    dft(complexI, complexI);    // this way the result may fit in the source matrix
//    // compute the magnitude and switch to logarithmic scale
//    // => log(1 + sqrt(Re(DFT(I))^2 + Im(DFT(I))^2))
//    split(complexI, planes);
//    //imshow("real: ", planes[0]);
//    //imshow("notreal:", planes[1]);
//    Mat IDFT[] = {Mat::zeros(dst.size(), CV_64F), Mat::zeros(dst.size(), CV_64F)};

//#if 1
//    //IDFT[0] = H_u_v.mul(planes[0]);//planes[0].mul(H_u_v);
//    //IDFT[1] = H_u_v.mul(planes[1]);//planes[1].mul(H_u_v);
//    planes[0].copyTo(IDFT[0]);
//    planes[1].copyTo(IDFT[1]);

//#else
//    IDFT[0] = planes[0].mul(H_u_v);
//    IDFT[1] = planes[1].mul(H_u_v);
//#endif
//    //imshow("fft real", <#InputArray mat#>)

//    merge(IDFT, 2, complexI);
//    idft(complexI, complexI);
//    split(complexI, IDFT);

//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double* dataRe = IDFT[0].ptr<double>(i);
//        double* dataIm = IDFT[1].ptr<double>(i);
//        double* logdata = dst.ptr<double>(i);

//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            if (dataIm[j] < 0)
//            {
//                logdata[j]  = dataRe[j]*dataRe[j] - dataIm[j]*dataIm[j];
//            }
//            else
//            {
//                logdata[j]  = dataRe[j]*dataRe[j] + dataIm[j]*dataIm[j];
//            }
//        }
//    }


//    normalize(dst, dst, 0, 5.545, CV_MINMAX);

//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double* logdata = dst.ptr<double>(i);
//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            logdata[j] = pow(2.718281828, logdata[j])+10;
//        }
//    }
//    dst.convertTo(dst, CV_8UC1);

//}


//void my_HomoFilter(Mat srcImg, Mat &dst)
//{

//    srcImg.convertTo(srcImg, CV_64FC1);
//    dst.convertTo(dst, CV_64FC1);
//    //1. ln
//    for (int i = 0; i < srcImg.rows; i++)
//    {
//        double* srcdata = srcImg.ptr<double>(i);
//        double* logdata = srcImg.ptr<double>(i);
//        for (int j = 0; j < srcImg.cols; j++)
//        {
//            logdata[j] = log(srcdata[j]+0.0001);
//        }
//    }

//    //spectrum
//    //2. dct
//    Mat mat_dct = Mat::zeros(srcImg.rows, srcImg.cols, CV_64FC1);
//    dct(srcImg, mat_dct);
//    imshow("dct", mat_dct);

//    //3. linear filter
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
//            dataH_u_v[j] = 	(gammaH - gammaL)*(1 - exp(-C*d2/d0)) + gammaL;
//            totalWeight += dataH_u_v[j];
//        }
//    }
//    H_u_v.ptr<double>(0)[0] = 1.1;

//    //H_u_v = Mat::ones(srcImg.rows, srcImg.cols, CV_64FC1);
//    imshow("H_u_v", H_u_v);


//    //imshow("before filter", mat_dct);

//    mat_dct = mat_dct.mul(H_u_v);
//    //Mat tmp = mat_dct.mul(H_u_v);
//    //tmp.copyTo(mat_dct);
//    //4. idct
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
//    //5. exp
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

////void  homomorphicfiltering(IplImage* src, IplImage* dst,
////                           const double & gammaH,
////                           const double& gammaL,
////                           const double& C,
////                           const double & d0)
////{
////    if ( gammaH < 1 || gammaL > 1 )
////    {
////        cerr<< "gammaH > 1 && gammaL < 1时高频增强，低频减小!" <<endl;
////        return;
////    }
////    if (src->nChannels != 2 || dst->nChannels != 2 )
////    {
////        cerr<< "通道数y必须为a1！！" <<endl;
////        return;
////    }
////    if (src->width != dst->width || src->height != dst->height)
////    {
////        cvError(CV_StsUnmatchedSizes, "homomorphicfiltering", "图像的长和宽必须相等" ,  __FILE__, __LINE__ );
////    }
////    //图像大小
////    CvSize sz = cvSize(src->width, src->height);
////    CvMat* temp = cvCreateMat(src->height, src->width, CV_64FC1);
////    double P = src->width/2;
////    double Q = src->height/2;
////    IplImage* imgRe = cvCreateImage(sz, src->depth, 1);
////    IplImage* imgIm = cvCreateImage(sz, src->depth, 1);
////    IplImage* srcTemp = cvCloneImage(src);
////    IplImage* dstTemp = cvCloneImage(src);
////    fftshift(src, srcTemp);
////    cvSplit(srcTemp, imgRe, imgIm, NULL, NULL);
////    for (int y = 0; y != src->height; ++y)
////    {
////        for (int x = 0; x != src->width; ++x)
////        {
////            double d2 = pow (pow(x - P, 2.0) + pow(y - Q, 2.0), 0.5);
////            *(( double*)CV_MAT_ELEM_PTR(*temp, y, x)) = (gammaH - gammaL)*(1 - exp(-C*d2/pow (d0, 2))) + gammaL;
////        }
////    }
////    cvMul(imgRe, temp, imgRe);
////    cvMul(imgIm, temp, imgIm);
////    cvMerge(imgRe, imgIm, NULL, NULL, dst);
////    fftshift(dst, dst);
////}




//int main(int argc, const char * argv[])

//{
//    // insert code here...
//    int width = 4;
//    int height = 4;
//    int size = width*height*3/2;

//#if 0
//    int frames = 100/1;

//    char fp_str[200] = "/Users/lilingyu1/Documents/collection_noise_estimation/noise_sequence/ipod5_368x640_f100.yuv";
//    width = 368;
//    height = 640;
//#endif


//#if 0
//    int frames = 240/1;

//    char fp_str[200] = "/Users/lilingyu1/Documents/collection_noise_estimation/noise_sequence/test2_1280x720.yuv";

//    width = 1280;
//    height = 720;

//#endif

//#if 0
//    int frames = 240/1;

//    char fp_str[200] = "/Users/lilingyu1/Documents/collection_noise_estimation/noise_sequence/jianchuan_rd_night_720x1280.yuv";

//    width = 720;
//    height = 1280;

//#endif

//#if 1
//    int frames = 1;

//    char fp_str[200] = "/Users/lilingyu1/Documents/dark_1136x1136.yuv";

//    width = 1136;
//    height = 1136;

//#endif


//#if 0
//    char fpo_str[200];


//    strcpy(fpo_str, fp_str);
//    //strcat(fpo_str, ".hdr_tone_map.yuv");
//    strcat(fpo_str, ".homo.yuv");


//    size = width*height*3/2;

//    FILE* fp = fopen(fp_str, "rb");
//    assert(NULL != fp);

//    FILE* fpo = fopen(fpo_str, "wb");
//    assert(NULL != fpo);

//    uint8_t* src = (uint8_t*)malloc(size);
//    assert(NULL != src);

//    //homo_filt_context* homo_ctx_p = malloc(sizeof(*homo_ctx_p));
//    //assert(NULL != homo_ctx_p);
//    float delta = 4.0/20;
//    int filter_radius = 3;
//    //homo_filter_init((void*)homo_ctx_p, width, height, delta, filter_radius);
//    //cv::Mat src_mat = Mat::zeros(height, width, CV_8UC1);

//    cv::Mat src_mat, dst_mat;
//    src_mat.data = src;
//    src_mat.rows = height;
//    src_mat.cols = width;

//    dst_mat = Mat::zeros(src_mat.rows, src_mat.cols, CV_8UC1);

//    long period = 0;
//    float seconds_per_frame=0.0;

//    for (int frame=0; frame<frames; frame++) {
//        fseek(fp, frame*width*height*3/2, 0);
//        fread(src, 1, width*height*3/2, fp);
//        memcpy(src_mat.data, src, width*height);

//        long tic = clock();
//        //hdr_tone_map_1ch(src, width, height);
//        //homo_filter((void*)homo_ctx_p, src, width, height);
//        //HomoFilter(src_mat, dst_mat);
//        my_HomoFilter(src_mat, dst_mat);

//        //test();

//        long toc = clock();
//        period += toc-tic;
//        float seconds = (toc-tic+0.0)/(CLOCKS_PER_SEC+0.0);
//        seconds_per_frame += seconds;
//        fwrite(dst_mat.data, 1, width*height, fpo);
//        fwrite(src+(width*height), 1, width*height/2, fpo);

//        printf("frame %3d: %8d\t%f\n", frame, (int)(toc-tic), seconds);


//    }
//    period /= frames;
//    seconds_per_frame /= frames;
//    printf("avg:\nclocks: %4d \tseconds: %8f\n", (int)period, seconds_per_frame);



//    fclose(fp);
//    fclose(fpo);
//    free(src);
//    //free(homo_ctx_p);
//    //homo_filter_close((void*)homo_ctx_p);
//#endif

//#if 0 //array test
//    uint8_t src[4*4] = {1, 1, 1, 1,
//                        1, 1, 1, 1,
//                        1, 1, 1, 1,
//                        1, 1, 1, 1};
//    width = 4;
//    height = 4;
//    cv::Mat src_mat = Mat::ones(height, width, CV_8UC1);
//    cout<<src_mat<<endl;

//    for (int y=0; y<height; y++) {
//        for (int x=0; x<width; x++) {
//            src_mat.data[y*width+x] = 0x80;
//        }
//    }

//    cv::Mat dst_mat;
//    //src_mat.data = src;
//    //src_mat.rows = height;
//    //src_mat.cols = width;

//    HomoFilter(src_mat, dst_mat);

//#endif

//#if 0
//    //get the image from the directed path
//    IplImage* img = cvLoadImage("/Users/lilingyu1/Documents/video_enhance/data/sample.jpg", 1);
//    //NSLog(img);
//    //create a window to display the image
//    cvNamedWindow("picture", 1);
//    //show the image in the window
//    cvShowImage("picture", img);
//    //wait for the user to hit a key
//    cvWaitKey(0);
//    //delete the image and window
//    cvReleaseImage(&img);
//    cvDestroyWindow("picture");
//#endif

//#if 1
//    char fpo_str[200];


//    strcpy(fpo_str, fp_str);
//    //strcat(fpo_str, ".hdr_tone_map.yuv");
//    strcat(fpo_str, ".homo.yuv");


//    size = width*height*3/2;

//    FILE* fp = fopen(fp_str, "rb");
//    assert(NULL != fp);

//    FILE* fpo = fopen(fpo_str, "wb");
//    assert(NULL != fpo);

//    uint8_t* src = (uint8_t*)malloc(size);
//    assert(NULL != src);
//    fread(src, 1, width*height*3/2, fp);



//    Mat src_mat = imread("/Users/lilingyu1/Documents/dark_1136x1136.jpg", 0);//
//    imshow("src:", src_mat);
//    Mat dst_mat(src_mat.rows, src_mat.cols, src_mat.type());
//    //HomoFilter(src_mat, dst_mat);
//    my_HomoFilter(src_mat, dst_mat);

//    fwrite(dst_mat.data, 1, width*height, fpo);
//    fwrite(src+(width*height), 1, width*height/2, fpo);

//    fclose(fp);
//    fclose(fpo);
//    free(src);

//    imshow("dst:", dst_mat);
//    cvWaitKey(0);


//#endif

//    return 0;

//}





