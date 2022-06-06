import os
import cv2
import copy
import numpy


def cv_demo(im):
    # 对图像进行局部直方图均衡化
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(10, 10))  # 对图像进行分割，10*10
    im = clahe.apply(im)  # 进行直方图均衡化
    # im = cv2.medianBlur(im,3)
    # im = cv2.equalizeHist(im)
    # im = cv2.GaussianBlur(im,(5,5),0)

    # ret, im = cv2.threshold(im, 120, 255, cv2.THRESH_TRUNC)
    # ret, im = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # im = cv2.GaussianBlur(im, (5, 5), 0)
    # image, contours = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 检测轮廓
    # im = cv2.drawContours(im, image, -1, (0, 255, 0), 1)  # 画出轮廓

    return im




if __name__ == "__main__":
    file_list = os.listdir("./zangwu")
    file_path = "./zangwu/"
    for i in file_list:

        im = cv2.imread(f"{file_path+i}", 0)
        ims = copy.deepcopy(im)
        im = cv_demo(im)


        img = numpy.c_[im,ims]
        cv2.imwrite(f"./image/{i}", img)