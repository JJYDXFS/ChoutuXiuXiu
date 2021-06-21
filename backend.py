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
    人脸定位服务
    '''
    # file_path, timestamp = save_img_to_server(request.files['file'])
    imgData = request.files['file']
    file_path, timestamp = save_img_to_server(request.files['file']) # 存图
    # 识别
    result = myFaceLoc(file_path, timestamp)
    return make_response(result)

@app.route('/api/get_face_recognition', methods=['POST'])
def get_face_recognition():
    '''
    人脸匹配服务
    '''
    imgData = request.files['file']

    path = base_dir + r'\\posts\\'

    timestamp = str(int(round(time.time() * 1000)))
    imgName = "unknown_"+timestamp+".jpg"
    file_path = path + imgName
    # # 保存图片
    imgData.save(file_path)
    # 识别
    result = myFaceRe(timestamp)
    return make_response(result)

@app.route('/api/get_img_path',methods=['GET'])
def get_img_path():
    '''
    视频切帧服务
    '''
    movie_path=request.args.get('movie_path')
    movie_path=movie_path.replace('\\','/')
    print(movie_path)
    
    return cut_movie(movie_path)

@app.route('/api/wear_hat', methods = ['POST'])
def wear_hat():
    '''
    人像戴帽子服务
    '''
    hatType = request.form['type'] # 得到帽子类型
    print(hatType)
    file_path, timestamp = save_img_to_server(request.files['file']) # 存图

    # 识别
    result = myWearHat(file_path, timestamp, hatType)
    return make_response(result)

# 主页
@app.route('/')
def index():
    return "Hi"

def myFaceLoc(img_path, timestamp):
    '''
    人脸定位
    '''
    image = cv2.imread(img_path)

    face_locations_noCNN=face_recognition.face_locations(image)
    face_num2=len(face_locations_noCNN)

    for i in range(0,face_num2):
        top = face_locations_noCNN[i][0]
        right = face_locations_noCNN[i][1]
        bottom = face_locations_noCNN[i][2]
        left = face_locations_noCNN[i][3]

        start = (left, top)
        end = (right, bottom)

        color = (0,255,255)
        thickness = 2
        cv2.rectangle(image, start, end, color, thickness)
    
    outname=base_dir+"\\results\\face_"+timestamp+".jpg"
    cv2.imwrite(outname,image)

    return json.dumps({'result_list':['results\\face_'+timestamp+'.jpg']},ensure_ascii=False)

# 辅助函数
# ----------------------------------------------------------------------------------------------------
def save_img_to_server(imgData):
    '''
    将图像保存到服务器，并返回保存路径
    '''
    path = base_dir + r'\\posts\\'

    timestamp = str(int(round(time.time() * 1000)))
    imgName = "post_"+timestamp+".jpg"

    file_path = path + imgName
    # 保存图片
    imgData.save(file_path)

    return (file_path, timestamp)


# 处理函数
# ---------------------------------------------------------------------------------
def myWearHat(file_path,timestamp,hatType):
    '''
    给人像戴上选中的帽子
    https://github.com/vipstone/faceai/blob/master/doc/compose.md
    '''

    img = cv2.imread(file_path)
    faceRects=face_recognition.face_locations(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换灰色
    color = (0, 255, 0)  # 定义绘制颜色

    hat_path = ""

    if hatType=="mxm":
        hat_path = base_dir+'\\hat_raw\\mxm.jpg'
    if hatType=="csm":
        hat_path = base_dir+'\\hat_raw\\csm.jpg'
    if hatType=="xcm":
        hat_path = base_dir+'\\hat_raw\\xcm.jpg'

    imgCompose = cv2.imread(hat_path)
    if len(faceRects):
        for faceRect in faceRects:
            top, right, bottom, left = faceRect
            x, y ,w, h = left, top ,abs(top-bottom), abs(right-left)
            sp = imgCompose.shape
            imgComposeSizeH = int(sp[0]/sp[1]*w)
            if imgComposeSizeH>(y-50):
                imgComposeSizeH=(y-50)
            imgComposeSize = cv2.resize(imgCompose,(w, imgComposeSizeH), interpolation=cv2.INTER_NEAREST)
            top = (y-imgComposeSizeH-50)
            if top<=0:
                top=0
            rows, cols, channels = imgComposeSize.shape
            roi = img[top:top+rows,x:x+cols]

            # Now create a mask of logo and create its inverse mask also
            img2gray = cv2.cvtColor(imgComposeSize, cv2.COLOR_RGB2GRAY)
            ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) 
            mask_inv = cv2.bitwise_not(mask)

            # Now black-out the area of logo in ROI
            img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

            # Take only region of logo from logo image.
            img2_fg = cv2.bitwise_and(imgComposeSize, imgComposeSize, mask=mask)

            # Put logo in ROI and modify the main image
            dst = cv2.add(img1_bg, img2_fg)
            img[top:top+rows, x:x+cols] = dst

    outname = base_dir+"\\results\\hat_"+timestamp+".jpg"
    cv2.imwrite(outname,img)

    return json.dumps({'result_list':['results\\hat_'+timestamp+'.jpg']},ensure_ascii=False)

if __name__ == '__main__':
    app.debug=True
    app.run('0.0.0.0', 5000)