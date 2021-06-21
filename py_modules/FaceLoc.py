import cv2
import face_recognition
import json

def myFaceLoc(base_dir, img_path, timestamp):
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
    
    outname = base_dir+"\\results\\face_"+timestamp+".jpg"
    cv2.imwrite(outname,image)

    return json.dumps({'result_list':['results\\face_'+timestamp+'.jpg']},ensure_ascii=False)