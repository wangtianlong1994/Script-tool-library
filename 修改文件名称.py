# 修改图片名称
import os
lists = []
paths = "./image/"
image_list = os.listdir("./image")
a = 689
for i in range(len(image_list)):
    os.rename(paths+image_list[i],(paths+str(a)+".bmp"))
    a += 1
    # os.rename(image_path,iamge_name)

# # 修改图片名称（去除名称内空格）
# import os
# paths = "./1/"
# image_list = os.listdir("./1")
# # print(image_list)
# for i in image_list:
#     c = i.split(".")[0]
#     if " " in c:
#         c = c.replace(" ", "")
#         os.rename(paths+i,paths+c+".bmp")

#     # os.rename(image_path,iamge_name)