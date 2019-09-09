import cv2
import os
files=["gt_6","gt_5","pred_5","pred_6"]
for i in files:
    filename=i
    img=cv2.imread("./"+filename+".png")
    img=img*50
    cv2.imwrite("./"+filename+"_color"+".png",img)
#cv2.imshow("im",img)
#cv2.waitKey(0)
