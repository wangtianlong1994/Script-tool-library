# 将动力电池4096分割成1280
import os
import cv2 as cv
#  13: 02 y1,y2,x1,x2
img_roi_list = [
    [0, 1200, 300, 1580],
    [0, 1200, 1400, 2680],
    [0, 1200, 2500, 3780],
]

file_list = os.listdir("./val")
file_path = "./val/"
for i in file_list:
    img = cv.imread(file_path+i)
    for ii in range(len(img_roi_list)):
        im = img[img_roi_list[ii][0]:img_roi_list[ii][1], img_roi_list[ii][2]:img_roi_list[ii][3]]
        # print(ii)
        file_name = "./1/"+i.split(".")[0]+"-"+str(ii) + ".jpg"
        cv.imwrite(file_name, im)
