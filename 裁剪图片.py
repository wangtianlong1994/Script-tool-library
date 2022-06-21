# 裁剪动力电池初始数据 使其只显示中间电池使用

import cv2
import os

img_paths = "./image/"
dir_list = os.listdir("./image")
for i in dir_list:
    im = cv2.imread(img_paths+i)
    print(i)
    # 正极截图尺寸
    # im = im[150:950,400:1200]
    # 负极截图尺寸
    # im = im[170:930,420:1180]
    # 天海正向
    im = im[340:980,570:1210]
    # 天海反向
    # im = im[340:980,430:1070]

    save_path = f"./scr_img/{i}"
    cv2.imwrite(save_path, im)
