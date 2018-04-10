# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.1.12 15:15
@Function:显示界面
'''

from tkinter import *
import cv2

from PIL import Image
from PIL import ImageTk

def callback():
    var.set('\n吹吧你,我才不信呢')


# filename = '/home/260158/company/test_pictures/pictures/f.jpg'
# a = cv2.imread(filename)
# img = cv2.resize(a,(640,480), interpolation=cv2.INTER_AREA)

root = Tk()

frame1 = Frame(root)  # Frame    框架控件；在屏幕上显示一个矩形区域，多用来作为容器
frame2 = Frame(root)

var = StringVar()  # 设置字符串
var.set("\n你所下载的影片含有末成人限制内容,\n\n请满18周岁后再点击观看")

textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)

textLabel.pack(side=LEFT)

photo = ImageTk.PhotoImage(file=r"/home/260158/company/test_pictures/pictures/f.jpg")

# photo = cv2.imread("/home/260158/company/test_pictures/pictures/z.jpg")

imgLabel = Label(frame1, text="图片一", image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="我已满18周岁", command=callback)  # 定义一个按钮
theButton.pack()

frame1.pack(padx=10, pady=10)  # 定义位置
frame2.pack(padx=50, pady=50)

mainloop()




# from tkinter.filedialog import askopenfilename
# from tkinter import *
#
# import cv2
#
#
# def get_file():
#     global filename
#     # 创建文件对话框,只打开txt类型文件
#     filename = askopenfilename(filetypes=[("photo file", "*")])
#     var.set(filename)
#     # print (filename)
#
# def photo_open():
#  #   photo = ImageTk.PhotoImage(file=r"filename")
#     photo = cv2.imread(filename)
#     cv2.imshow('qewq',photo)
#     if cv2.waitKey(0) == 27:  # 如果输入ESC退出
#         cv2.destroyAllWindows()
#
#     # return photo
#
# if __name__ == '__main__':
#
#     # 创建根窗口
#     root = Tk()
#     root.title("标签项目")
#     root.geometry("400x200+450+210")  # width x height;起始坐标
#
#     frame = Frame(root)
#     frame.pack()
#
#     frm_L = Frame(frame)
#     var = StringVar()
#     Label(frm_L, text="").pack()
#     Entry(frm_L, textvariable=var, bd=1).pack(expand=1)
#     Label(frm_L, text="").pack()
#     frm_L.pack()
#
#     frm_R = Frame(frame)
#     Button(frm_R, text="打开文件", command=get_file, height=2, width=8).pack(side=LEFT)
#     Button(frm_R, text="解密", command=photo_open, height=2, width=10).pack(side=RIGHT)
#     frm_R.pack()
#
#     frm_D = Frame(root)
#     Button(frm_D, text="退出", command=frm_R.quit, height=2, width=8, bg="#B0D060").pack()
#     frm_D.pack(side=BOTTOM)
#
#     root.mainloop()