import os
import time
import hashlib
"""
检查重复图片
原理：图片如果一模一样，其md5值也是一样
代码逻辑：检查图片文件夹，把每一张图片md5值加入列表中，并判断是否已经存在，如果存在则删除图片，不存在则将该图片md5加入列表
"""
# 得到图片md5值并返回
def get_md5(f):
    md5 = hashlib.md5()
    md5.update(f.read())
    f.close()
    return md5.hexdigest()

# 遍历图片文件夹，每张图片打开并传递给md5函数得到md5值，并根据md5值来判断是否是重复图片
def get_file(init_files):
    file_md5_list = []
    file_list = os.listdir(init_files)
    for i in file_list:
        path = f"{file_dir}/{i}"
        f = open(path, "rb")
        file_md5 = get_md5(f)
        if file_md5 not in file_md5_list:
            file_md5_list.append(file_md5)
        else:
            os.remove(path)


if __name__ == "__main__":
    # 文件夹地址
    file_dir = "./image"
    get_file(file_dir)

