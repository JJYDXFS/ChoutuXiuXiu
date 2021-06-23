import cv2
import face_recognition
import numpy as np
import json

def myFaceRe(BASE_DIR, imageData, index, timestamp, save_path):
    '''
    人脸识别模块
    @refer
    https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py

    @param
    BASE_DIR: 服务器存储文件全局路径
    imageData: 图像数据，单图检测传入图片路径，视频检测传入图片数据
    index: index=-1时对应单图检测，index为正整数时对应视频检测的图片下标
    timestamp: 时间戳，用于定义新建目录名
    save_path: 图片保存路径，仅在index≠-1时有效

    @return
    单图检测模式下返回图片相对前端的路径
    视频检测模式下不返回有意义值
    '''
    if index == -1: unknown_img = cv2.imread(imageData)
    else: unknown_img = imageData
    face_locations = face_recognition.face_locations(unknown_img)
    face_encodings = face_recognition.face_encodings(unknown_img, face_locations)
    # 导入人脸数据
    name_list = ['Queen Elizabeth II','Prince Charles','Princess Anne','Princess Diana','Lady Thatcher','Earl of Snowdon','Princess Margaret','Harold Wilson','Duke of Edinburgh','IU','song wei','The Queen Mother','King George V']
    known_face_encodings = np.load(BASE_DIR+'\\data\\face_encoding.npy')

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
        outname = BASE_DIR + "\\results\\face_"+timestamp+".jpg"
        cv2.imwrite(outname,unknown_img)
        return  json.dumps({'result_list':['results\\face_'+timestamp+'.jpg']},ensure_ascii=False)
    else: # 对于视频识别，按给定保存路径存，并命名
        outname = save_path+"\\image{}.jpg".format(index)
        cv2.imwrite(outname,unknown_img)
        return