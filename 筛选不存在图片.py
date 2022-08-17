# # 筛选不存在的图片或xml
# import os
# import shutil
#
# xml_list = os.listdir("Annotations")
# image_list = os.listdir("images")
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
#         file.write("./Annotations/"+x+".xml"+"\n")
# file.close()
#
# for i in open("2.txt", "r"):
#     a = i.strip()
#     os.remove(a)
#     # print(a)



import os
import shutil

xml_list = os.listdir("2")
image_list = os.listdir("2_xml")
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
        file.write("./2/" + x + ".png" + "\n")
file.close()

for i in open("2.txt", "r"):
    a = i.strip()
    # os.remove(a)
    shutil.move(a, "./1/"+a.split("/")[2])
