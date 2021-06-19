from flask import Flask, request, render_template, jsonify, make_response
from flask_cors import *

import time
import pymysql
import json
import copy
# 人脸识别相关
import cv2
import face_recognition
import os
import subprocess
import shutil

app = Flask(__name__,static_url_path='/static/',template_folder='templates')
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})

# base_dir = r"C:\\Users\\JOYCE\Desktop\\face_re\\public"
base_dir = r"F:\\OneDrive\\Documents\\ThirdYear\\MediaDataAnalysis\\MeidaBigData\\public"
dbSize = 6

@app.route('/api/get_face_loaction', methods=['POST'])
def get_face_loaction():
    '''
    接收用户上传图片，并保存到指定路径
    '''
    imgData = request.files['file']

    path = base_dir + r'\\posts\\'

    imgName = "unknown.jpg"
    file_path = path + imgName
    # # 保存图片
    imgData.save(file_path)
    # 识别
    result = detect_2()
    return make_response(result)

@app.route('/api/get_face_recognition', methods=['POST'])
def get_face_recognition():
    '''
    接收用户上传图片，并保存到指定路径
    '''
    imgData = request.files['file']

    path = base_dir + r'\\posts\\'

    imgName = "unknown.jpg"
    file_path = path + imgName
    # # 保存图片
    imgData.save(file_path)
    # 识别
    result = detect_1()
    return make_response(result)

@app.route('/api/get_img_path',methods=['GET'])
def get_img_path():
    movie_path=request.args.get('movie_path')
    movie_path=movie_path.replace('\\','/')
    print(movie_path)
    
    return cut_movie(movie_path)

# 主页
@app.route('/')
def index():
    return "Hi"

def detect_1():
    '''
    未知人脸与数据库匹配
    '''
    #显示已知图片
    known_encoding=[]

    img_path = base_dir + "\\face_db\\"

    for i in range(1,dbSize,1):
        known_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(img_path+str(i)+".jpg"))[0])

    unknown_image = face_recognition.load_image_file(base_dir+"\\posts\\unknown.jpg")

    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces(known_encoding,
                                            unknown_encoding,
                                            tolerance=0.6)
    result_list = []
    for i in range(dbSize-1):
        if results[i]==True:
            result_dir = 'face_db/'+str(i+1)+".jpg"
            result_list.append(result_dir)
    
    return json.dumps({'result_list':result_list},ensure_ascii=False)
    
def detect_2():
    '''
    人脸检测
    '''
    face_cascade = cv2.CascadeClassifier("G:\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

    filename = base_dir+"\\posts\\unknown.jpg"

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    outname=base_dir+"\\face.jpg"
    cv2.imwrite(outname,img)
    return json.dumps({'result_list':['face.jpg']},ensure_ascii=False)
    

def cut_movie(movie_path):
    os.chdir('C:\\Users\\JOYCE\\Desktop')
    image_save='/pic'
    # shutil.rmtree('F:\\flask\\face_re\\public\\pic')
    if not os.path.exists("C:\\Users\\JOYCE\Desktop\\face_re\\public\\pic"):
        os.mkdir('C:\\Users\\JOYCE\Desktop\\face_re\\public\\pic')

    cap=cv2.VideoCapture(movie_path)
    frame_count=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(int(frame_count)):
        _,img=cap.read()
        img=cv2.cvtColor(img,cv2.cv2.COLOR_RGB2HSV)   #cv2.COLOR_RGB2HSV     cv2.COLOR_BGR2GRAY
        # img = cv2.GaussianBlur(img, (3, 3), 0)
        # img = cv2.Canny(img, 30, 100)
        cv2.imwrite('C:\\Users\\JOYCE\Desktop\\face_re\\public\\pic\\image{}.jpg'.format(i),img)


    return json.dumps({'path':image_save+'/image','count':frame_count},ensure_ascii=False)

if __name__ == '__main__':
    app.debug=True
    app.run('127.0.0.1', 5000)