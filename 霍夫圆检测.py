import cv2 as cv
import numpy as np


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

    # 霍夫圈变换
    # 参数分别为：image, method, dp, minDist, param1, param2, minRadius, maxRadius
    # 其中：image为灰度图像，method使用的方法为霍夫梯度法，minDist两个圆中心的最小距离
    circles = cv.HoughCircles(gray_img, cv.HOUGH_GRADIENT, 1, 100, param1=50, param2=30, minRadius=300, maxRadius=400)

    # 对数据进行取整
    circles = np.uint16(np.around(circles))
    x = circles[0][0][0]
    y = circles[0][0][1]
    r = circles[0][0][2]
    # 绘制圆外圈
    # 参数分别为：圆心、半径、颜色、线框宽度
    # cv.circle(img, (x, y), r, (0, 0, 255), 2)
    # 绘制圆心
    # cv.circle(img, (x, y), 2, (255, 0, 0), 2)
    zero = x - r
    one = y - r
    tow = x + r
    three = y + r
    print(zero, one, tow, three)
    im = image[one:three, zero:tow]
    print(im.shape)
    cv.imshow("img", im)


# 读取图片信息
img = cv.imread("./1.bmp")

# 检测圆并根据圆心裁剪图片
circles = detect_circle(img)

cv.waitKey(0)
