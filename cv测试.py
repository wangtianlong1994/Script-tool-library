import os
import cv2
import copy
import numpy


def cv_demo(im):
    # 对图像进行局部直方图均衡化
    # im = cv2.GaussianBlur(im,(5,5),0)
    # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5, 5))  # 对图像进行分割，10*10
    # im = clahe.apply(im)  # 进行直方图均衡化

    # im = cv2.equalizeHist(im)

    # # 图像归一化
    # fi = im / 255.0
    # # 伽马变换
    # gamma = 0.6
    # im = numpy.power(fi, gamma)

    ret, im = cv2.threshold(im, 110, 255, cv2.THRESH_TRUNC)

    # im = cv2.GaussianBlur(im, (5, 5), 0)
    im = cv2.medianBlur(im,5)
    ret, im = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # image, contours = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 检测轮廓
    # im = cv2.drawContours(im, image, -1, (0, 255, 0), 1)  # 画出轮廓
    # return im
    im = cv2.resize(im, (640, 640))
    cv2.imshow("cv", im)
#
im = cv2.imread("img/3.bmp", 0)
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
#
#
# import cv2
# import numpy as np
#
# image = cv2.imread('img/1.bmp')
# cv2.imshow("original image", image)
#
# # 灰度图
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # 转换为浮点数类型数组
# gray = np.float32(gray)

# # NORM_MINMAX，最常用的一种方法，数组的数值会被缩放到一个指定的范围，比如本例中的 0~1
# dst = np.zeros(gray.shape, dtype=np.float32)
# # 这里alpha=1, beta=0也是ok的
# cv2.normalize(gray, dst=dst, alpha=1, beta=0, norm_type=cv2.NORM_MINMAX)
# # 显示原图时，需要将像素值 re-scale 到 0~255
# cv2.imshow("NORM_MINMAX", np.uint8(dst * 255))
#
# # NORM_INF，无穷范数，每个值除以最大值来进行无穷范数归一化
# dst = np.zeros(gray.shape, dtype=np.float32)
# cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_INF)
# # 归一化后最大值就是1，所以也是*255
# cv2.imshow("NORM_INF", np.uint8(dst * 255))

# # NORM_L1，1范数，每个值除以它们的和来进行归一化
# dst = np.zeros(gray.shape, dtype=np.float32)
# cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L1)
# # 归一化后范围是 0~1，但最大值不是1，所以这里乘以一个足够大的数，你也可以取其它值，不一定是下面这个数。注意到 np.uint8 的最大值是255，因此 re-scale 的范围也是 0~255
# cv2.imshow("NORM_L1", np.uint8(dst * 20000000))
#
# # NORM_L2，2范数，每个值除以该向量的模长，归一化为单位向量
# dst = np.zeros(gray.shape, dtype=np.float32)
# cv2.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv2.NORM_L2)
# # 与NORM_L1类似
# cv2.imshow("NORM_L2", np.uint8(dst * 30000))
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

