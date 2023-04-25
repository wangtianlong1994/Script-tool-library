import os
import cv2 as cv
import numpy as np
from PIL import Image

def detect_circle(image):
    '''
     作用：圆形检测
     参数：需要检测圆的图片
     返回：检测出圆形的信息
    '''
    # 均值偏移滤波降噪处理
    mean_filter_img = cv.pyrMeanShiftFiltering(image, 10, 100)

    # 图像灰度处理
    gray_img = cv.cvtColor(mean_filter_img, cv.COLOR_BGR2GRAY)
    # ret, im = cv.threshold(gray_img, 110, 255, cv.THRESH_TRUNC)

    # im = cv2.GaussianBlur(im, (5, 5), 0)
    # im = cv.medianBlur(gray_img,5)
    # ret, im = cv.threshold(im, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    # cv.imshow("img", im)
    # 霍夫圈变换0
    # 参数分别为：image, method, dp, minDist, param1, param2, minRadius, maxRadius
    # 其中：image为灰度图像，method使用的方法为霍夫梯度法，minDist两个圆中心的最小距离
    circles = cv.HoughCircles(gray_img, cv.HOUGH_GRADIENT, 2, 30, param1=100, param2=100, minRadius=150, maxRadius=420)
    #
    # # circles = cv.HoughCircles(gray_img, cv.HOUGH_GRADIENT, 1, 10, param1=10, param2=30, minRadius=100, maxRadius=200)
    # # 对数据进行取整
    circles = np.uint16(np.around(circles))

    x = circles[0][0][0]
    y = circles[0][0][1]
    r = circles[0][0][2]
    print(x, y, r)
    # # # 绘制圆外圈
    # # # 参数分别为：圆心、半径、颜色、线框宽度
    rw = 435 - r
    r += rw
    # cv.circle(image, (x, y), r, (0, 0, 255), 2)
    # # 绘制圆心
    # cv.circle(image, (x, y), 2, (255, 0, 0), 2)
    zero = x - r
    one = y - r
    tow = x + r
    three = y + r
    # #
    img = image[one:three, zero:tow]




    # img = cv.resize(im, (1280,1280))
    # cv.imshow("1", img)
    return img

# img = cv.imread("./1.bmp")
# detect_circle(img)
# cv.waitKey()

# 读取图片信息
img_files = os.listdir("./6")
img_path = "./6/"
for i in img_files:
    img = cv.imread(f"{img_path+i}")
    # 检测圆并根据圆心裁剪图片
    # img = detect_circle(img)

    # # 增加图片亮度
    # imgs = np.zeros(img.shape, img.dtype)
    # img = cv.convertScaleAbs(img, imgs, 2.0, 0)

    # 向左90度
    # img = np.rot90(img)
    # img = np.rot90(img)
    # img = np.rot90(img)
    cv.imwrite(f"./chaochuang_6_4/{i.split('.')[0]}.jpg", img)
    # cv.imwrite(f"./NG/{i}", img)


