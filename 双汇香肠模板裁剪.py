# # import os
# #
# # import cv2
# # import cv2 as cv
# #
# #
# # file_list = os.listdir("./sh")
# # file_path = "./sh/"
# # for i in file_list:
# #     im = cv.imread(f"{file_path+i}", 0)
# #     im = cv2.GaussianBlur(im, (5, 5), 0)
# #     ret, im = cv.threshold(im, 170, 255, cv.THRESH_OTSU)
# #     # 生成矩形结构元素
# #     kernel = cv.getStructuringElement(cv.MORPH_RECT, (30, 30))
# #     # 形态闭运算 先膨胀后腐蚀 得到矩形
# #     im = cv.morphologyEx(im, cv.MORPH_CLOSE, kernel)
# #     im = cv2.resize(im,(640,640))
# #     cv.imshow("1",im)
# #     cv.waitKey()
#
# import cv2 as cv
# import numpy as np
#
# im = cv.imread("./sh/32bmp")
# img = cv.imread("./sh/32.bmp")
# img1 = cv.imread("./sh/32.bmp")
# # cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
# im = cv.GaussianBlur(im, (31, 31), 0)
# # ret, im = cv.threshold(im, 100, 255, cv.THRESH_TRUNC)
# ret, im = cv.threshold(im, 50, 255, cv.THRESH_BINARY)
# im = cv.cvtColor(im,cv.COLOR_RGB2GRAY)
# ret, im = cv.threshold(im, 50, 255, cv.THRESH_BINARY)
# cv.imshow("test",im)
#
# # ret, im = cv.threshold(im, 150, 255, cv.THRESH_BINARY)
# # # #进行闭运算，去除图像内部噪声
# # kernel = np.ones((21,21), np.uint8)#设置卷积核
# # im = cv.morphologyEx(im, cv.MORPH_CLOSE, kernel)#闭运算
# # im=cv.morphologyEx(im, cv.MORPH_OPEN, kernel)
#
#
# # ret, im = cv.threshold(im, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# # im = cv.Canny(im, 0, 100)
# contours, image = cv.findContours(im, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 检测轮廓
# cv.drawContours(img, contours, -1, (0, 255, 0), 4)  # 画出轮廓
#
# cont_list = []
# for i in contours:
#     x,y,w,h = cv.boundingRect(i)
#     # print(x,y,w,h)
#     if 400 > w > 200:
#       cont_list.append([x,y,w,h])
# img_name = 0
# for ii in cont_list:
#     print(ii)
#     img2 = img1[int(ii[1])-50:int(ii[1])+int(ii[3]+50),int(ii[0])-200:int(ii[0])+int(ii[2])+200]
#     save_path = f"./sh_train/{str(img_name)}.png"
#     print(save_path)
#     img_name += 1
#     cv.imwrite(save_path, img2)
# # im = cv.cvtColor(im, cv.COLOR_BGR2HSV)
# # low_hsv = np.array([0,43,46])
# # high_hsv = np.array([34,255,255])
# # im = cv.inRange(im,lowerb=low_hsv,upperb=high_hsv)
# # #
# # # # ## 生成矩形结构元素
# # kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
# # # ## 形态开运算 先腐蚀后膨胀 得到矩形
# # im = cv.morphologyEx(im, cv.MORPH_OPEN, kernel)
# #
# # image, contours = cv.findContours(im, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # 检测轮廓
# # for i in image:
# #     if len(i) > 500:
# #         print(image)
# # cv.drawContours(img, image, -1, (0, 255, 0), 4)  # 画出轮廓
#
# # # # # # # 设置腐蚀和膨胀核
# # kernel = np.ones(shape=[7,7],dtype=np.uint8)  # 通过shape=[3,3]可以改变处理效果
# # # # #
# # # # # # 腐蚀，由多变少，边界容易被腐蚀,去除噪声
# # im = cv.erode(im,kernel=kernel,iterations=2)
# # # #
# # # # # # 膨胀，图像变粗
# # im = cv.dilate(im, kernel, iterations=1)
#
# # cv.dilate(im, kernel)
# cv.imshow("test",im)
# cv.imshow("test2",img)
# cv.waitKey(0)
# cv.destroyAllWindows()1

# 根据香肠模板设置裁剪图片roi自动裁剪对应图片
import os
import cv2 as cv
#13:02
img_roi_list = [
    [0, 900, 0, 500],
    [0, 900, 450, 990],
    [0, 900, 930, 1370],
    [0, 900, 1400, 1940],
    [0, 900, 1870, 2410],
    [0, 900, 2330, 2800],

    [900, 1800, 0, 500],
    [900, 1800, 430, 990],
    [900, 1800, 910, 1370],
    [900, 1800, 1380, 1940],
    [900, 1800, 1870, 2410],
    [900, 1800, 2330, 2800],

    [1800, 2700, 0, 500],
    [1800, 2700, 430, 990],
    [1800, 2700, 910, 1370],
    [1800, 2700, 1380, 1940],
    [1800, 2700, 1870, 2410],
    [1800, 2700, 2330, 2800],
]
names = 1
file_list = os.listdir("./NG")
file_path = "./NG/"
for i in file_list:
    img = cv.imread(file_path+i)
    for ii in range(len(img_roi_list)):
        im = img[img_roi_list[ii][0]:img_roi_list[ii][1], img_roi_list[ii][2]:img_roi_list[ii][3]]
        print()
        file_name = "./1/"+"3x6_5_"+str(names) + ".png"
        cv.imwrite(file_name, im)
        names += 1