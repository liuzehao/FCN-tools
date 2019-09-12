import cv2
import os
import numpy as np
from numba import jit
def get_all_files(bg_path):
    files = []

    for f in os.listdir(bg_path):
        if os.path.isfile(os.path.join(bg_path, f)):
            files.append(os.path.join(bg_path, f))
        else:
            files.extend(get_all_files(os.path.join(bg_path, f)))
    files.sort(key=lambda x: int(x[-6:-4]))#排序从小到大
    return files
@jit
def change(img):
    for t in range(img.shape[0]):
        for z in range(img.shape[1]):
            if img[t][z]==38:
                img[t][z]=1
            elif img[t][z]==75:
                img[t][z]=2
            else:
                img[t][z]=0
    return img

def changeimg(files):
    for i in files:
        print(i)
        name=os.path.basename(i)
        im=cv2.imread(i,cv2.IMREAD_GRAYSCALE)
        img_list = im.tolist()
        img = np.asarray(img_list)
        img=change(img)
        cv2.imwrite('./training/'+name,img)
files=get_all_files('./2labelpng')
changeimg(files)