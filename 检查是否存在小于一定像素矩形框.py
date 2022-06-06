# 根据矩形顶点坐标计算矩形像素大小，并判断小于一定尺寸将xml与bmp文件分别复制出，查看是否有异常边缘框

import os
import xml.etree.ElementTree as ET
import shutil
cls_name = "鸟琢"
for i in os.listdir("/home/zxzn/D/数据/骏枣/第三次修改/"+cls_name):
    root = ET.parse("/home/zxzn/D/数据/骏枣/第三次修改/"+cls_name+"/"+i).getroot()
    objects = root.findall('object')
    for obj in objects:
        bbox = obj.find('bndbox')
        lab_name = obj.find('name').text
        xmin = float(bbox.find('xmin').text.strip())
        ymin = float(bbox.find('ymin').text.strip())
        xmax = float(bbox.find('xmax').text.strip())
        ymax = float(bbox.find('ymax').text.strip())
        w, d = int(ymax-ymin), int(xmax-xmin)
        if w*d < 20000:
            shutil.copy("/home/zxzn/D/数据/骏枣/第三次修改/"+cls_name+"/"+i, "Annotations/"+i)
            shutil.copy("/home/zxzn/D/数据/骏枣/第二次修改/"+cls_name+"/images/"+i.split(".")[0]+".bmp", "images/"+i.split(".")[0]+".bmp")

            f = open("1.txt","a+")
            f.write(f"查找到异形矩形框,来自{cls_name}类,文件名为{i},异常类名为{lab_name}\n")
            f.close()
            break

