import os

txt_file_lists = os.listdir("labels/val")

for i in txt_file_lists:
    f = open("labels/val/"+i, "r")
    if not f.read():
        print(i)