import cv2
import numpy as np
import face_recognition
import os
import json

from .FaceRe import myFaceRe

# 通过得到RGB每个通道的直方图来计算相似度
def classify_hist_with_split(image1, image2, size=(256, 256)):
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data

# 计算单通道的直方图的相似值
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    
    return degree

def myVideoFaceRe(base_dir,file_path,timestamp):
    '''
    接收视频路径，返回关键帧+识别结果
    '''
    v_path = file_path
    cap = cv2.VideoCapture(v_path)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # 定义关键帧保存路径
    save_path = base_dir+"\\results\\"+timestamp
    os.mkdir(save_path)
    # 初始化计数器
    count = 0
    # 逐帧处理
    for i in range(int(frame_count)-1):
        _,imgNext=cap.read()
        
        if i == 0: # 第一帧直接保存
            myFaceRe(base_dir,imgNext,count,0,save_path)
            img=imgNext
            continue
        # 从第二帧开始比较
        n = [0.0]

        try:
            n=classify_hist_with_split(img,imgNext)
        except Exception as e:
            continue
        
        if float(n[0])<0.7:
            count=count+1
            myFaceRe(base_dir,imgNext,count,0,save_path)
        img=imgNext
    
    return json.dumps({'path':"\\results\\"+timestamp,'count':count},ensure_ascii=False)