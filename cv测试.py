import os
import cv2
import copy
import numpy


def cv_demo(im):
    # 对图像进行局部直方图均衡化
    # im = cv2.GaussianBlur(im,(5,5),0)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(50, 50))  # 对图像进行分割，10*10
    im = clahe.apply(im)  # 进行直方图均衡化

    # im = cv2.equalizeHist(im)


    ret, im = cv2.threshold(im, 130, 255, cv2.THRESH_TRUNC)
    # ret, im = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # im = cv2.GaussianBlur(im, (5, 5), 0)
    im = cv2.medianBlur(im,5)
    # image, contours = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 检测轮廓
    # im = cv2.drawContours(im, image, -1, (0, 255, 0), 1)  # 画出轮廓
    # return im
    im = cv2.resize(im, (640,640))
    cv2.imshow("cv", im)
#
im = cv2.imread("./9.bmp", 0)
cv_demo(im)
cv2.waitKey(0)
#
#
# if __name__ == "__main__":
#     file_list = os.listdir("./zangwu")
#     file_path = "./zangwu/"
#     for i in file_list:
#
#         im = cv2.imread(f"{file_path+i}", 0)
#         ims = copy.deepcopy(im)
#         im = cv_demo(im)
#
#
#         img = numpy.c_[im,ims]
#         cv2.imwrite(f"./image/{i}", img)
#
# import cv2 as cv
# import numpy as np
#
# def close_demo(image):
#     ret, image = cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#     kernel = cv.getStructuringElement(cv.MORPH_RECT, (150, 150))
#     image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
#
#     contours, grade = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 检测轮廓
#     # 最小轮廓所有点集
#     cont = min(contours, key=cv.contourArea)
#     # 最小轮廓矩形
#     c = cv.minAreaRect(cont)
#
#     ange = c[2]
#     if ange != 0.0:
#         if ange < 0:
#             ange += 90
#         else:
#             ange -= 90
#
#     box = np.int0(cv.boxPoints(c))
#     print(box)
#     g = cv.imread("./3.bmp")
#     cv.drawContours(g, [box], -1, (0, 0, 255), 5)  # 画出轮廓
#     rows, clos = g.shape[:2]
#     print(rows, clos)
#     M = cv.getRotationMatrix2D((clos/2, rows/2), ange, 1)
#     re_im = cv.warpAffine(g,M,(clos, rows))
#
#     cv.imshow("close_demo", re_im)
#
# src = cv.imread("./3.bmp", 0)  #读取图片位置
# close_demo(src)
# cv.waitKey(0)

