"""
适用于 数据整体新增其他类。

小部分数据手动标注后，训练模型推理其余数据；

但是由于只训练小部分数据，导致其他类识别异常；

将推理出的数据txt文件只保留新增类矩形框数据；

然后将该矩形框数据写入到初始xml数据中；

由此完成了在初始数据上直接增加新框功能，无需全部数据重新标注增加矩形框。

步骤：
# 1.先把小批量数据新增类标注出来

# 2.使用该数据训练模型

# 3.推理初始数据图片并保存txt数据

# 4.剔除txt中非新增类数据-剔除

# 5.将初始xml数据中标注框合并到txt中-合并

# 6.合并后txt文件重新生成xml数据

# 7.xml新增类完成，重新训练模型
"""
import os

# 剔除txt中非新增类数据
txt_paths = "./new_txt/"
new_paths = "./txt/"
txt_dirs = os.listdir(txt_paths)

for i in txt_dirs:
    f = open(f"{txt_paths+i}", "r+")
    ff = open(f"{new_paths+i}", "a+")
    for ii in f.readlines():
        if "left" in ii.split(",")[4]:
            ff.write(f"{ii.split(' ')[0]}\n")

    f.close()
    ff.close()




