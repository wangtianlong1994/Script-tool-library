import os

txt_file_lists = os.listdir("labels/val")

for i in txt_file_lists:
    f = open("labels/val/"+i, "r")
    if not f.read():
        print(i)


# import os
#
# txt_file_lists = os.listdir("../new_txt")
#
# for i in txt_file_lists:
#     f = open("../new_txt/"+i, "r")
#     if not f.read():
#         print(i)