QT -= gui

CONFIG += c++11 console
CONFIG -= app_bundle

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

INCLUDEPATH += /usr/local/include \
               /usr/local/include/opencv \
               /usr/local/include/opencv2 \
               /usr/include \
               /home/260158/company/海康大数据中心/软件包/Linux系统/Linux系统SDK/Samples_LinuxSDK/include

LIBS += /usr/local/lib/libopencv_* \
        /home/260158/company/海康大数据中心/软件包/Linux系统/Linux系统SDK/Samples_LinuxSDK/lib/64

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    Persp_Trans.cpp \
    test_stitch.cpp \
    cvsamples_stitch.cpp \
    surf_stitch.cpp \
    test_imshow.cpp \
    rotation.cpp \
    homofilter.cpp \
    homofilter_1.cpp \
    rename.cpp \
    test_sdk.cpp \
    real_data_callback.cpp
