import cv2
import numpy as np
im=cv2.imread("pred_6_color.png")
canny = cv2.Canny(im, 20, 30)  # 20是最小阈值,50是最大阈值 边缘检测
# minLINELENGTH=20
# lines = cv2.HoughLinesP( canny, 1, np.pi/180, minLINELENGTH, 0 )
# #print(lines.shape)
# #
# for i in lines:
#     print(i)
#     point=i[0]
#     cv2.line(canny, (point[0],point[1]), (point[2],point[3]), (0, 255, 0), 1, 4)
#     #cv2.line(canny, (point[0],point[1]), (point[2],point[3]) color[, thickness[, lineType[, shift]]])
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dilation = cv2.dilate(canny,kernel,iterations = 1)#膨胀一下，来连接边缘
contours, hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#找边框
#print(len(contours))
p1=()
p2=()
p3=()
p4=()
pp=[p1,p2,p3,p4]
for t in range(len(contours)):
    hull = cv2.convexHull(contours[t])
    epsilon = 0.1*cv2.arcLength(hull, True)#0.36081735求边框周长，epsilon 是精度

    point=cv2.approxPolyDP(hull, epsilon, True) 
    if (len(point) == 4):# and epsilon>100 and epsilon<600 ):#and (int(point[0][0][0:1])>700) and (int(point[0][0][1:2])>1000)这里找身份证特征，因为背景简单直接判断边框周长就行
        for i in range(len(point)-1):
            cv2.line(im, tuple(point[i][0]), tuple(point[i+1][0]), (0,255,0), 1)
            pp[i]=tuple(point[i][0])
            if(i==(len(point)-2)):
                pp[i+1]=tuple(point[i+1][0])
        cv2.line(im, tuple(point[0][0]), tuple(point[i+1][0]), (0,255,0), 1)
        
        
# #扩展边界
# extends=150
# ppx1=pp[0][0]+extends
# ppy1=pp[0][1]+extends
# temp=(ppx1,ppy1)
# pp[0]=temp

# ppx2=pp[1][0]-extends
# ppy2=pp[1][1]+extends
# temp=(ppx2,ppy2)
# pp[1]=temp

# ppx3=pp[2][0]-extends
# ppy3=pp[2][1]-extends
# temp=(ppx3,ppy3)
# pp[2]=temp

# ppx4=pp[3][0]+extends
# ppy4=pp[3][1]-extends
# temp=(ppx4,ppy4)
# pp[3]=temp
# #cv2.rectangle(img, pp[0], pp[2], (0,255,0),10)#框出身份证
# imga=img[ppy4:ppy1,ppx3:ppx4]

cv2.imshow("aaa",im)
cv2.waitKey(0)
