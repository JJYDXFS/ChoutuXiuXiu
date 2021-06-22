import cv2
import face_recognition
import json
import numpy as np
import pandas as pd

def myChangeFace(BASE_DIR,timestamp):
    '''
    换脸模块
    @refer: https://blog.csdn.net/qq_41562735/article/details/104978448?spm=1001.2014.3001.5501
    
    @param:
    BASE_DIR: 服务器存储文件全局路径
    
    @return:
    返回生成图片相对前端的路径
    '''
    face1_path = BASE_DIR+"\\posts\\changeface\\image0.jpg"
    face2_path = BASE_DIR+"\\posts\\changeface\\image1.jpg"
    image_save = BASE_DIR+"\\results\\changeface_"+timestamp+".jpg"
    changeFaceMain(image_save,face1_path,face2_path)

    return json.dumps({'result_list':['\\results\\changeface_'+timestamp+'.jpg']},ensure_ascii=False)

def ladmasktuple(img):
    faces_loaction=face_recognition.face_locations(img,number_of_times_to_upsample = 0,model ='cnn')
    face_feature=face_recognition.face_landmarks(img,face_locations=faces_loaction)
    face_feature1=pd.DataFrame(face_feature)
    def listexpend(X):
        a=[]
        for i in list(X):
            a.extend(i)      
        return a
    h1=[]
    for j in range (0,9):
        h=listexpend(face_feature1.iloc[:,j])
        h1+=h
    return h1

def extract_index_nparray(nparray):
    index = None
    for num in nparray[0]:
        index = num
        break
    return index

def changeFaceMain(image_save,face1_path,face2_path):
    img=cv2.imread(face1_path)
    img2=cv2.imread(face2_path)#目标图像

    landmarks_points=ladmasktuple(img)
    #points1
    landmarks_points2=ladmasktuple(img2)


    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(img_gray)
    points = np.array(landmarks_points, np.int32)
    convexhull = cv2.convexHull(points)
    points2 = np.array(landmarks_points2, np.int32)
    convexhull2 = cv2.convexHull(points2)
    # cv2.polylines(img, [convexhull], True, (255, 0, 0), 3)
    cv2.fillConvexPoly(mask, convexhull, 255)

    # Delaunay triangulation
    rect = cv2.boundingRect(convexhull)
    subdiv = cv2.Subdiv2D(rect)
    subdiv.insert(landmarks_points)
    triangles = subdiv.getTriangleList()
    triangles = np.array(triangles, dtype=np.int32)

    indexes_triangles = []
    for t in triangles:
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])

        index_pt1 = np.where((points == pt1).all(axis=1))
        index_pt1 = extract_index_nparray(index_pt1)

        index_pt2 = np.where((points == pt2).all(axis=1))
        index_pt2 = extract_index_nparray(index_pt2)

        index_pt3 = np.where((points == pt3).all(axis=1))
        index_pt3 = extract_index_nparray(index_pt3)

        if index_pt1 is not None and index_pt2 is not None and index_pt3 is not None:
            triangle = [index_pt1, index_pt2, index_pt3]
            indexes_triangles.append(triangle)

    #img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    height, width, channels = img2.shape
    img2_new_face = np.zeros((height, width, channels), np.uint8)
    lines_space_mask = np.zeros_like(img_gray)

    for triangle_index in indexes_triangles:
        # Triangulation of the first face
        tr1_pt1 = landmarks_points[triangle_index[0]]
        tr1_pt2 = landmarks_points[triangle_index[1]]
        tr1_pt3 = landmarks_points[triangle_index[2]]
        triangle1 = np.array([tr1_pt1, tr1_pt2, tr1_pt3], np.int32)


        rect1 = cv2.boundingRect(triangle1)
        (x, y, w, h) = rect1
        cropped_triangle = img[y: y + h, x: x + w]
        cropped_tr1_mask = np.zeros((h, w), np.uint8)


        points = np.array([[tr1_pt1[0] - x, tr1_pt1[1] - y],
                           [tr1_pt2[0] - x, tr1_pt2[1] - y],
                           [tr1_pt3[0] - x, tr1_pt3[1] - y]], np.int32)

        cv2.fillConvexPoly(cropped_tr1_mask, points, 255)

        # Lines space
        cv2.line(lines_space_mask, tr1_pt1, tr1_pt2, 255)
        cv2.line(lines_space_mask, tr1_pt2, tr1_pt3, 255)
        cv2.line(lines_space_mask, tr1_pt1, tr1_pt3, 255)

        # Triangulation of second face
        tr2_pt1 = landmarks_points2[triangle_index[0]]
        tr2_pt2 = landmarks_points2[triangle_index[1]]
        tr2_pt3 = landmarks_points2[triangle_index[2]]
        triangle2 = np.array([tr2_pt1, tr2_pt2, tr2_pt3], np.int32)

        rect2 = cv2.boundingRect(triangle2)
        (x, y, w, h) = rect2

        cropped_tr2_mask = np.zeros((h, w), np.uint8)

        points2 = np.array([[tr2_pt1[0] - x, tr2_pt1[1] - y],
                            [tr2_pt2[0] - x, tr2_pt2[1] - y],
                            [tr2_pt3[0] - x, tr2_pt3[1] - y]], np.int32)

        cv2.fillConvexPoly(cropped_tr2_mask, points2, 255)

        # Warp triangles
        points = np.float32(points)
        points2 = np.float32(points2)
        M = cv2.getAffineTransform(points, points2)
        warped_triangle = cv2.warpAffine(cropped_triangle, M, (w, h))
        warped_triangle = cv2.bitwise_and(warped_triangle, warped_triangle, mask=cropped_tr2_mask)

        # Reconstructing destination face
        img2_new_face_rect_area = img2_new_face[y: y + h, x: x + w]
        img2_new_face_rect_area_gray = cv2.cvtColor(img2_new_face_rect_area, cv2.COLOR_BGR2GRAY)
        _, mask_triangles_designed = cv2.threshold(img2_new_face_rect_area_gray, 1, 255, cv2.THRESH_BINARY_INV)
        warped_triangle = cv2.bitwise_and(warped_triangle, warped_triangle, mask=mask_triangles_designed)

        img2_new_face_rect_area = cv2.add(img2_new_face_rect_area, warped_triangle)
        img2_new_face[y: y + h, x: x + w] = img2_new_face_rect_area
    
    
    img2_face_mask = np.zeros_like(img2_gray,dtype='uint8')
    img2_head_mask = cv2.fillConvexPoly(img2_face_mask, convexhull2,255)
    #cv2.fillPoly(img=img2_face_mask ,pts=convexhull2,color=(255,255,255))
    img2_face_mask = cv2.bitwise_not(img2_head_mask)

    #img2_face_mask=np.uint8(img2_face_mask)
    img2_head_noface = cv2.bitwise_and(img2, img2, mask=img2_face_mask)
    result = cv2.add(img2_head_noface, img2_new_face)

    (x, y, w, h) = cv2.boundingRect(convexhull2)
    center_face2 = (int((x + x + w) / 2), int((y + y + h) / 2))

    seamlessclone = cv2.seamlessClone(result, img2, img2_head_mask, center_face2, cv2.NORMAL_CLONE)
    img_want=cv2.cvtColor(seamlessclone, cv2.COLOR_BGR2RGB)
    b,g,r=cv2.split(img_want)#修改图片色差
    img_newWant=cv2.merge([r,g,b])
    
    cv2.imwrite(image_save,img_newWant)

    return image_save

# if __name__=="__main__":
#     BASE_DIR = r"F:\\OneDrive\\Documents\\ThirdYear\\MediaDataAnalysis\\MeidaBigData\\public"
#     timestamp = "123456789"
#     myChangeFace(BASE_DIR,timestamp)