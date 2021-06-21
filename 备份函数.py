def myFaceLoc_junior(timestamp):
    '''
    人脸定位初级版
    '''
    face_cascade = cv2.CascadeClassifier("G:\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

    filename = base_dir+"\\posts\\unknown_"+timestamp+".jpg"

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    outname=base_dir+"\\face_"+timestamp+".jpg"
    cv2.imwrite(outname,img)
    return json.dumps({'result_list':['face_'+timestamp+'.jpg']},ensure_ascii=False)

def cut_movie(movie_path):
    '''
    视频切帧
    '''
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

def myFaceRe(timestamp):
    '''
    未知人脸与数据库匹配
    '''
    #显示已知图片
    known_encoding=[]

    img_path = base_dir + "\\face_db\\"

    for i in range(1,dbSize,1):
        known_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(img_path+str(i)+".jpg"))[0])

    unknown_image = face_recognition.load_image_file(base_dir+"\\posts\\unknown_"+timestamp+".jpg")

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