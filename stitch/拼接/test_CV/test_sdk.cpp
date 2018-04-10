///**********************************
//@Author:Zhao Lu
//@Time: Created on 2018-1-23  15：47
//@Funtion: 测试，调用海康SDK，是获取服务器上的视频流，不是本地的
//***********************************/

#include <X11/Xlib.h>
#include <assert.h>
#include "math.h"
#include "pthread.h"

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include "MvCameraControl.h"

#define MAX_IMAGE_DATA_SIZE 20*1024*1024
#define NIL 0

//等待用户输入enter键来结束取流或结束程序
void PressEnterToExit(void)
{
    int c;
    while((c = getchar()) != '\n' && c != EOF)   //原程序中的有分号？？？
        fprintf(stderr, "\nPress enter to exit.\n");
    while(getchar() != '\n')
        sleep(1);
}

//显示设备的信息
bool PrintDeviceInfo(MV_CC_DEVICE_INFO* pstMVDevInfo)
{
    if (NULL == pstMVDevInfo)
    {
        printf("%s\n", "The Pointer of pstMVDevInfoList is NULL");
        return false;
    }
    if(pstMVDevInfo->nTLayerType == MV_GIGE_DEVICE)
    {
        //打印当前相机ip和用户自定义名字
        printf("%s %x\n","nCurrentIp:",pstMVDevInfo->SpecialInfo.stGigEInfo.nCurrentIp);
        printf("%s %x\n","chUserDefinedName:",pstMVDevInfo->SpecialInfo.stGigEInfo.chUserDefinedName);
    }
    else if(pstMVDevInfo->nTLayerType == MV_USB_DEVICE)
    {
        printf("UserDefinedName:%s\n\n",pstMVDevInfo->SpecialInfo.stGigEInfo.chUserDefinedName);
    }
    else
    {
        printf("Not support.\n");
    }
    return true;
}

int main()
{
    Window w;
    Display *dpy;

    memset(&w, 0, sizeof(Window));
    dpy = NULL;
    printf("%d\n",sizeof(Window));

    //打开连接到X服务器的连接
    dpy = XOpenDisplay(NIL);
    int whiteColor = WhitePixel(dpy,DefaultScreen(dpy));
    w = XCreateSimpleWindow(dpy,DefaultRootWindow(dpy),0,0,752,480,0,0xffff00ff,0xff00ffff);

    //获取改变窗口大小事件
    XSelectInput(dpy,w,StructureNotifyMask);
    //使窗口可见
    XMapWindow(dpy,w);
    //创建图像上下文给出绘图函数的属性
    GC gc = XCreateGC(dpy,w,0,NIL);
    //告诉GC使用白色
    XSetForeground(dpy,gc,whiteColor);
    //等待事件的到来
    for(;;)
    {
        XEvent e;
        XNextEvent(dpy,&e);
        if(e.type == MapNotify)
        {
            break;
        }
    }

    int nRet = MV_OK;
    void* handle = NULL;
    MV_CC_EnumDevices(MV_GIGE_DEVICE | MV_USB_DEVICE,&stDeviceList);
    memset(&stDeviceList, 0, sizeof(MV_CC_DEVICE_INFO_LIST));

    // 枚举设备,列出所有设备
    nRet = MV_CC_EnumDevices(MV_GIGE_DEVICE | MV_USB_DEVICE, &stDeviceList);
    if (MV_OK != nRet)
    {
        printf("MV_CC_EnumDevices fail! nRet [%x]\n", nRet);
        return -1;
    }
    unsigned int nIndex = 0;
    if (stDeviceList.nDeviceNum > 0)
    {
        for (int i = 0; i < stDeviceList.nDeviceNum; i++)
        {
            printf("[device %d]:\n", i);
            MV_CC_DEVICE_INFO* pDeviceInfo = stDeviceList.pDeviceInfo[i];
            if (NULL == pDeviceInfo)
            {
                break;
            }
            PrintDeviceInfo(pDeviceInfo);
        }
    }
    else
    {
        printf("Find No Devices!\n");
        return -1;
    }

    scanf("%d", &nIndex); //等待输入选择的设备号

    // 选择设备并创建句柄
    nRet = MV_CC_CreateHandle(&handle, stDeviceList.pDeviceInfo[nIndex]);
    if (MV_OK != nRet)
    {
        printf("MV_CC_CreateHandle fail! nRet [%x]\n", nRet);
        return -1;
    }

    // 打开设备
    nRet = MV_CC_OpenDevice(handle);
    if (MV_OK != nRet)
    {
        printf("MV_CC_OpenDevice fail! nRet [%x]\n", nRet);
        return -1;
    }

    // 开始取流
    nRet = MV_CC_StartGrabbing(handle);
    if (MV_OK != nRet)
    {
        printf("MV_CC_StartGrabbing fail! nRet [%x]\n", nRet);
        return -1;
    }

    nRet= MV_CC_Display(handle, (void*)w);
    if (MV_OK != nRet)
    {
        printf("MV_CC_Display fail! nRet [%x]\n", nRet);
        return -1;
    }
    printf("Display succeed\n");
    PressEnterToExit();

    // 停止取流
    nRet = MV_CC_StopGrabbing(handle);
    if (MV_OK != nRet)
    {
        printf("MV_CC_StopGrabbing fail! nRet [%x]\n", nRet);
        return -1;
    }

    // 关闭设备
    nRet = MV_CC_CloseDevice(handle);
    if (MV_OK != nRet)
    {
        printf("MV_CC_CloseDevice fail! nRet [%x]\n", nRet);
        return -1;
    }

    // 销毁句柄
    nRet = MV_CC_DestroyHandle(handle);
    if (MV_OK != nRet)
    {
        printf("MV_CC_DestroyHandle fail! nRet [%x]\n", nRet);
        return -1;
    }

    printf("exit\n");

    return 0;

}








