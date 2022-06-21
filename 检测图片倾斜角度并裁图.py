import os
import cv2 as cv
import numpy as np

def det_angle(img):
    # 图片灰度
    imgs = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 自适应二值化（必须用灰度图像）
    ret, imgs = cv.threshold(imgs, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # 生成矩形结构元素
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (150, 150))
    # 形态闭运算 先膨胀后腐蚀 得到矩形
    imgs = cv.morphologyEx(imgs, cv.MORPH_CLOSE, kernel)
    # 轮廓检测
    contours, grade = cv.findContours(imgs, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 检测轮廓
    # 查找最小矩形轮廓所有点集
    cont = min(contours, key=cv.contourArea)
    # 最小轮廓矩形和旋转角度
    c = cv.minAreaRect(cont)
    # 判断角度是否不等于0同时大于或者小于0，得到需要旋转的角度
    ange = c[2]
    if ange != 0.0:
        if ange < 0:
            ange += 90
        else:
            ange -= 90
    # 得到矩形四角坐标并转换成向量
    box = np.int0(cv.boxPoints(c))
    # 画出轮廓
    img = cv.drawContours(img, [box], -1, (0, 0, 255), 5)
    # 得到原始图片w,h
    rows, clos = img.shape[:2]
    # 根据图片中心点和旋转角度进行图片旋转
    img_angle = cv.getRotationMatrix2D((clos/2, rows/2), ange, 1)
    # 填充旋转后图片缺失部分
    img = cv.warpAffine(img, img_angle,(clos, rows))

    cv.imshow("det_angle", img)


file_list = os.listdir("./1")
file_path = "./1/"
for i in file_list:
    img = cv.imread(file_path+i)  #读取图片位置
    det_angle(img)
    cv.waitKey(0)
