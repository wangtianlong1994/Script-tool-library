# 将初始xml数据中标注框合并到txt中
import os
import xml.etree.ElementTree as ET

xml_paths = "./Annotations/"
xml_dirs = os.listdir(xml_paths)
txt_paths = "./txt/"

for i in xml_dirs:
    s = i.split(".")[0]+".txt"
    in_file = open(xml_paths+i, encoding="UTF-8")
    out_file = open(txt_paths+s, 'a+')

    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        xmlbox = obj.find('bndbox')
        b = (xmlbox.find('xmin').text, xmlbox.find('xmax').text, xmlbox.find('ymin').text, xmlbox.find('ymax').text)
        out_file.write((",").join([str(a) for a in b]) + ","+cls+"\n")