# 修改图片名称
import os
lists = []
paths = "./23_1-4_1/"
image_list = os.listdir("./23_1-4_1")
a = 587
for i in range(len(image_list)):

    # os.rename(paths+image_list[i],(paths+"6x3_beijing_"+ str(a) + ".png"))

    os.rename(paths+image_list[i],(paths+"23_1-4_"+ str(a) + ".jpg"))
    a += 1
    # os.rename(image_path,iamge_name)


# # 修改图片名称
# import os
# lists = []
# paths = "./2/"
# pathss = "./4/"
# image_list = os.listdir("./2")
#
# for i in image_list:
#     # i_name = i.split("(")[1]
#     # i1_name = i_name.split(")")[0]
#     # i1_name = int(i1_name)-1
#     # # print(type(i1_name))
#     ina = i.split(".")[0]
#     ina = int(ina)-1
#
#     os.rename(paths+i, pathss+str(ina)+".bmp")

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