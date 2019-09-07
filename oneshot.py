import cv2
import os
import numpy as np
def get_all_files(bg_path):
    files = []

    for f in os.listdir(bg_path):
        if os.path.isfile(os.path.join(bg_path, f)):
            files.append(os.path.join(bg_path, f))
        else:
            files.extend(get_all_files(os.path.join(bg_path, f)))
    files.sort(key=lambda x: int(x[-7:-4]))#排序从小到大
    return files
files=get_all_files('./2labelpng')
for i in files:
    name=os.path.basename(i)
    im=cv2.imread(i,cv2.IMREAD_GRAYSCALE)
    # for t in range(3):
    #     print(im[t])

    #print(np.unique(im))
    size=im.shape
    for t in range(size[0]):
        for z in range(size[1]):
            if im[t][z]==38:
                im[t][z]=1
            if im[t][z]==75:
                im[t][z]=2
    print(np.unique(im))
    cv2.imwrite('./train_oneshot/'+name,im)
