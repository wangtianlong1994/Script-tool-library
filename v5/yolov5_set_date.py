# # # # 说明 txt文件最后一行不能有空行
# # # #

import os, shutil

f_train_img = open("train.txt", "r")
file_list_train_img = f_train_img.read()
f_train_img.close()
fl_train_img = file_list_train_img.split("\n")
os.mkdir("images/train")
for i in fl_train_img:
    if i:
        shutil.move("images/"+i.split("/")[2], "images/train/"+i.split("/")[2])

f_val_img = open("val.txt", "r")
file_list_val_img = f_val_img.read()
f_val_img.close()
fl_val_img = file_list_val_img.split("\n")
os.mkdir("images/val")
for ii in fl_val_img:
    if ii:
        shutil.move("images/"+ii.split("/")[2], "images/val/"+ii.split("/")[2])

f_train_txt = open("train_labels.txt", "r")
file_list_train_txt = f_train_txt.read()
f_train_txt.close()
fl_train_txt = file_list_train_txt.split("\n")
os.mkdir("labels/train")
for iii in fl_train_txt:
    if iii:
        shutil.move("labels/"+iii.split("/")[2], "labels/train/"+iii.split("/")[2])

f_val_txt = open("val_labels.txt", "r")
file_list_val_txt = f_val_txt.read()
f_val_txt.close()
fl_val_txt = file_list_val_txt.split("\n")
os.mkdir("labels/val")
for iiii in fl_val_txt:
    if iiii:
       shutil.move("labels/"+iiii.split("/")[2], "labels/val/"+iiii.split("/")[2])








