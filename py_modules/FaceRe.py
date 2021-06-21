from time import time
import cv2
import face_recognition
import numpy as np
import json
import os

def myFaceRe(base_dir, imageData, index, timestamp, save_path):
    '''
    人脸识别并保存识别结果
    index=-1时表明是普通检测，按timestamp保存图片
    否则，按index保存图片
    '''
    if index == -1: unknown_img = cv2.imread(imageData)
    else: unknown_img = imageData
    face_locations = face_recognition.face_locations(unknown_img)
    face_encodings = face_recognition.face_encodings(unknown_img, face_locations)
    # 导入人脸数据
    name_list = ['Queen Elizabeth II','Prince Charles','Princess Anne','Princess Diana','Lady Thatcher','Earl of Snowdon','Princess Margaret','Harold Wilson','Duke of Edinburgh','IU','song wei']
    known_face_encodings = np.load(base_dir+'\\data\\face_encoding.npy')

    face_names = []

    # if len(face_encodings) == 0 : 
    #     print("没有识别到人脸")

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        # 直接使用最短距离
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = name_list[best_match_index]

        face_names.append(name)

    # 标记结果
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(unknown_img, (left, top), (right, bottom), (0, 0, 200), 2)

        cv2.rectangle(unknown_img, (left, bottom - 35), (right, bottom), (0, 0, 200), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(unknown_img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    if index == -1: # 对于单张识别
        outname = base_dir + "\\results\\face_"+timestamp+".jpg"
        cv2.imwrite(outname,unknown_img)
        return  json.dumps({'result_list':['results\\face_'+timestamp+'.jpg']},ensure_ascii=False)
    else: # 对于视频识别，按给定保存路径存，并命名
        outname = save_path+"\\image{}.jpg".format(index)
        cv2.imwrite(outname,unknown_img)
        return
    

    