# # 说明 txt文件最后一行不能有空行
# #
# #train image
# import os, shutil
#
# f = open("train.txt", "r")
# file_list = f.read()
# f.close()
#
# fl = file_list.split("\n")
# os.mkdir("images/train")
# for i in fl:
#     print(i.split("/")[1])
#     shutil.move("images/"+i.split("/")[2], "images/train/"+i.split("/")[2])
#
#
# # val image
# import os, shutil
# #
# f = open("val.txt", "r")
# file_list = f.read()
# f.close()
#
# fl = file_list.split("\n")
# os.mkdir("images/val")
# for i in fl:
#     print(i.split("/")[1])
#     shutil.move("images/"+i.split("/")[2], "images/val/"+i.split("/")[2])

# # train labels
# import os, shutil
# #
# f = open("train_labels.txt", "r")
# file_list = f.read()
# f.close()
#
# fl = file_list.split("\n")
# os.mkdir("labels/train")
# for i in fl:
#     print(i.split("/")[1])
#     shutil.move("labels/"+i.split("/")[2], "labels/train/"+i.split("/")[2])

#
# #val labels
# import os, shutil
#
# f = open("val_labels.txt", "r")
# file_list = f.read()
# f.close()
#
# fl = file_list.split("\n")
# os.mkdir("labels/val")
# for i in fl:
#     print(i.split("/")[1])
#     shutil.move("labels/"+i.split("/")[2], "labels/val/"+i.split("/")[2])