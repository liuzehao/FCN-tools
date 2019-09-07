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
files=get_all_files('./validation')
for i in files:
    im=cv2.imread(i)
    print(np.unique(im))