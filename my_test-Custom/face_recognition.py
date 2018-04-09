# -*-coding:utf-8-*-
'''
@Author: Zhao YinFa
@Time: 2018.02.08 13:49
@Function:python自带的人脸识别算法和人脸比对
'''


import face_recognition
import cv2

# 检测人脸
def face():
    # 读取图片并识别人脸
    img = face_recognition.load_image_file('/home/260158/company/test_pictures/pictures/geli-1.jpg')
    face_locations = face_recognition.face_locations(img)
    # print(face_locations) #打印人脸的坐标

    img = cv2.imread("/home/260158/company/test_pictures/pictures/geli-1.jpg")
    # 遍历每个人脸，并标注
    faceNum = len(face_locations)
    print(faceNum)
    for i in range(faceNum):
        top =  face_locations[i][0]
        right =  face_locations[i][1]
        bottom = face_locations[i][2]
        left = face_locations[i][3]

        start = (left, top)
        end = (right, bottom)

        color = (55,255,155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)

    # 显示识别结果
    cv2.imshow("aa", img)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()


#人脸比对
girls2_image = face_recognition.load_image_file("/home/260158/code/code_tool/faces/girls2.png");
girls3_image = face_recognition.load_image_file("/home/260158/code/code_tool/faces/girls3.png");
boy1_image = face_recognition.load_image_file("/home/260158/code/code_tool/faces/boy1.png");

girls2_encoding = face_recognition.face_encodings(girls2_image)[0]
girls3_encoding = face_recognition.face_encodings(girls3_image)[0]
boy1_encoding = face_recognition.face_encodings(boy1_image)[0]

results = face_recognition.compare_faces([girls2_encoding, girls3_encoding], boy1_encoding )
labels = ['girls2', 'girls3']

print('results:'+str(results))

for i in range(0, len(results)):
    if results[i] == True:
        print('The person is:'+labels[i])



