# 写一个冒泡法函数，输入一个列表，返回一个排序后的列表
def bubble_sort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

# 写一个从小到大排列的冒泡法函数，输入一个列表，返回一个排序后的列表
def bubble_sort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list


# 写一个调用摄像头的函数，返回一个视频
import cv2
def get_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
# get_video()

# 识别身份证号码
import re
def id_card():
    id = input('请输入身份证号码：')
    if re.match(r'^\d{17}[\dxX]$',id):
        print('身份证号码正确')
    else:
        print('身份证号码错误')
# id_card()

# 通过一张图片识别身份证号码
import cv2
import numpy as np
import re
def id_card():
    img = cv2.imread('1.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('thresh',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 识别身份证号码
    id = re.findall(r'\d{17}[\dxX]',str(thresh))
    print(id)
id_card()

