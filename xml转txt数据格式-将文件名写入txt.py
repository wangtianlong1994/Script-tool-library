# import xml.etree.ElementTree as ET
# import pickle
# import os
# from os import listdir, getcwd
# from os.path import join
#
# sets = ['train','val']
# # classes = ["AoXian","HeiBan","GanTiao","LieKou","HaoZao","NiaoZhuo","LanZao","ShuZao"]
# # classes = ["AoXian","HeiBan","GanTiao","LieKou","HaoZao","NiaoZhuo","LanZao","ShuZao","PoPi"]
# # classes = ["AoXian","HeiBan","GanTiao","LieKou","HaoZao","NiaoZhuo","LanZao","ShuZao","PoPi","HeiLie"]
# # classes = ['BianXing', 'HeiBan', 'GanTiao', 'HuangPi', 'HaoZao', 'XiaoNiao', 'DaNiao', 'LanZao', 'LieKou', 'ShuZao']
# # classes = ['BianXing', 'HeiBan', 'GanTiao', 'HuangPi', 'HaoZao', 'XiaoNiao', 'DaNiao', 'LanZao', 'LieKou', 'ShuZao', 'FengBan']
# # classes = ['BianXing', 'HeiBan', 'GanTiao', 'HaoZao', 'XiaoNiao', 'DaNiao', 'LanZao', 'LieKou', 'ShuZao', 'FengBan']
# # classes = ["BianXing","HeiBan","GanTiao","LieKou","HaoZao","NiaoZhuo","LanZao","ShuZao","PoPi",'FengBan']
# # classes = ["BianXing","HeiBan","GanTiao","LieKou","HaoZao","NiaoZhuo","LanZao","ShuZao"]
# # classes = ["AoKeng", "HuaShang"]
# # classes = ["label", "cuobiao", "jietou", "posun", "loubai"]
# # classes = ["Dian", "Kuai", "Xian"]
# # classes = ["Dian", "Kuai","Xian", "HanDian"]
# # classes = ["Hao", "Qing","Zhong", "Yan"]
# # classes = ["yewei", "yellow", "ng"]
# # classes = ["yewei", "blue", "ng"]
# # classes = ["xiangchang", "yiwu", "zhangbao", "jiya"]
# # classes = ["feisi","weiyi","kailie","zhenghan","hankuan","wuhan","fanhan","fanduan","left"]
# # classes = ["huashang"]
# classes = ["aokeng"]
#

import xml.etree.ElementTree as ET
import os


classes = ["label", "cuobiao", "jietou", "posun", "loubai"]

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    if not str(x).split(".")[0] == "0":
        print(x, y, w, h)
    elif not str(y).split(".")[0] == "0":
        print(x, y, w, h)
    elif not str(w).split(".")[0] == "0":
        print(x, y, w, h)
    elif not str(h).split(".")[0] == "0":
        print(x, y, w, h)
    return (x, y, w, h)


def convert_annotation(image_id, convert_name):
    in_file = open(convert_name + '_xml/%s.xml' % (image_id))
    out_file = open('data/labels/%s/%s.txt' % (convert_name, image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text

        if cls not in classes and int(difficult) == 1:
            continue

        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)

        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')



convert_name = "val"
img_list = os.listdir(convert_name)
if not os.path.exists('data/labels/%s' % convert_name):
    os.makedirs('data/labels/%s' % convert_name)
list_file = open('data/%s.txt' % (convert_name), 'w')
for imgs in img_list:
    image_id = imgs.split(".")[0]
    list_file.write('data/images/%s/%s\n' % (convert_name,imgs))
    convert_annotation(image_id, convert_name)
list_file.close()



