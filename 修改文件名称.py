# 修改图片名称
# import os
# lists = []
# paths = "./12.16灰枣黄皮图片/"
# image_list = os.listdir("./12.16灰枣黄皮图片")
# a = 7095
# for i in range(len(image_list)):
#     os.rename(paths+image_list[i],(paths+"Jujube_21"+str(a)+".bmp"))
#     a += 1
#     # os.rename(image_path,iamge_name)

# 修改图片名称（去除名称内空格）
import os
paths = "./xml/"
image_list = os.listdir("./xml")
# print(image_list)
for i in image_list:
    c = i.split(".")[0]
    if " " in c:
        c = c.replace(" ", "")
        os.rename(paths+i,paths+c+".xml")

    # os.rename(image_path,iamge_name)