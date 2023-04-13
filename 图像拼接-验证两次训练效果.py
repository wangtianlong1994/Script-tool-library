import os
import cv2

old = "exp4/"
new = "exp6/"
old_imgs = os.listdir(old)

for i in old_imgs:
    old_im = cv2.imread(old+i)
    new_im = cv2.imread(new+i)
    imgs = cv2.hconcat([old_im, new_im])

    cv2.imwrite("./1/"+i, imgs)
