import face_recognition
import cv2
import json

def myWearHat(base_dir, file_path,timestamp,hatType):
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