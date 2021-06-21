from flask import Flask, request, render_template, jsonify, make_response
from flask_cors import *

import time
import pymysql
import json
import copy
# 人脸识别相关
# import cv2

import os
import subprocess
import shutil
# 自定义模块
from py_modules.WearHat import myWearHat
from py_modules.FaceLoc import myFaceLoc
from py_modules.FaceRe import myFaceRe
from py_modules.VideoFaceRe import myVideoFaceRe

app = Flask(__name__,static_url_path='/static/',template_folder='templates')
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# base_dir = r"C:\\Users\\JOYCE\Desktop\\face_re\\public"
base_dir = r"F:\\OneDrive\\Documents\\ThirdYear\\MediaDataAnalysis\\MeidaBigData\\public"

@app.route('/api/get_face_loaction', methods=['POST'])
def get_face_loaction():
    '''
    人脸定位服务
    '''
    file_path, timestamp = save_img_to_server(request.files['file']) # 存图
    # 识别
    result = myFaceLoc(base_dir, file_path, timestamp)
    return make_response(result)

@app.route('/api/get_face_recognition', methods=['POST'])
def get_face_recognition():
    '''
    人脸匹配服务
    '''
    file_path, timestamp = save_img_to_server(request.files['file'])
    # 匹配
    result = myFaceRe(base_dir,file_path,-1,timestamp,0)
    return make_response(result)

@app.route('/api/video_face_re',methods=['POST'])
def video_face_re():
    '''
    视频切帧服务
    '''
    file_path, timestamp = save_video_to_server(request.files['file'])
    # 视频处理
    result = myVideoFaceRe(base_dir, file_path, timestamp)
    return make_response(result)

@app.route('/api/wear_hat', methods = ['POST'])
def wear_hat():
    '''
    人像戴帽子服务
    '''
    hatType = request.form['type'] # 得到帽子类型
    print(hatType)
    file_path, timestamp = save_img_to_server(request.files['file']) # 存图

    # 识别
    result = myWearHat(base_dir, file_path, timestamp, hatType)
    return make_response(result)

# 主页
@app.route('/')
def index():
    return "Hi"

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

def save_video_to_server(videoData):
    '''
    将视频保存到服务器，并返回保存路径
    '''
    path = base_dir + r'\\posts\\video\\'

    timestamp = str(int(round(time.time() * 1000)))
    videoName = "post_"+timestamp+".mp4"

    file_path = path + videoName
    # 保存视频
    videoData.save(file_path)

    return (file_path, timestamp)


# 处理函数
# ---------------------------------------------------------------------------------


if __name__ == '__main__':
    app.debug=True
    app.run('0.0.0.0', 5000)