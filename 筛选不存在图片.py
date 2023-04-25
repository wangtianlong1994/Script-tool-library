# # 筛选不存在的图片或xml
# import os
# import shutil
#
# xml_list = os.listdir("val_xml")
# image_list = os.listdir("val")
# lists = []
# for image in image_list:
#     i = image.split('.')
#     i = i[0]
#     lists.append(i)
# file = open("2.txt", "w+")
# for xml in xml_list:
#     x = xml.split('.')
#     x = x[0]
#     if x not in lists:
#         file.write("./val_xml/"+x+".xml"+"\n")
# file.close()
#
# for i in open("2.txt", "r"):
#     a = i.strip()
#     os.remove(a)
#     # print(a)



import os
import shutil

xml_list = os.listdir("2450_6_nei_mei_3")
image_list = os.listdir("2450_6_nei_mei_3_xml")
lists = []
for image in image_list:
    i = image.split('.')

    i = i[0]
    lists.append(i)
file = open("2.txt", "w+")
for xml in xml_list:
    x = xml.split('.')
    x = x[0]
    if x not in lists:
        file.write("./2450_6_nei_mei_3/" + x + ".png" + "\n")
file.close()

for i in open("2.txt", "r"):

    a = i.strip()
    # os.remove(a)
    print(a.split("/")[2])
    shutil.move(a, "./1/"+a.split("/")[2])
