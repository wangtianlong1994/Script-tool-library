# 筛选不存在的图片或xml
import os
import shutil

xml_list = os.listdir("1_2_xml")
image_list = os.listdir("1_2")
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
        file.write("./1_2_xml/"+x+".xml"+"\n")
file.close()

for i in open("2.txt", "r"):
    a = i.strip()
    os.remove(a)
    # print(a)



# import os
# import shutil
#
# xml_list = os.listdir("6_5")
# image_list = os.listdir("6_5_xml")
# lists = []
# for image in image_list:
#     i = image.split('.')
#
#     i = i[0]
#     lists.append(i)
# file = open("2.txt", "w+")
# for xml in xml_list:
#     x = xml.split('.')
#     x = x[0]
#     if x not in lists:
#         file.write("./6_5/" + x + ".jpg" + "\n")
# file.close()
#
# for i in open("2.txt", "r"):
#     a = i.strip()
#     os.remove(a)
# #     # shutil.move(a, "./1/"+a.split("/")[2])
