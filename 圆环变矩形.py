import cv2
import numpy as np
from PIL import Image
import math


def get_huan_by_circle(img, circle_center, radius, radius_width):
    black_img = np.zeros((radius_width, int(2 * radius * math.pi), 3), dtype='uint8')
    for row in range(0, black_img.shape[0]):
        for col in range(0, black_img.shape[1]):
            theta = math.pi * 2 / black_img.shape[1] * (col + 1)  # +origin_theta
            rho = radius + row - 1
            p_x = int(circle_center[0] + rho * math.sin(theta) + 0.5) - 1
            p_y = int(circle_center[1] - rho * math.cos(theta) + 0.5) - 1

            black_img[row, col, :] = img[p_y, p_x, :]
    return black_img


img = cv2.imread('img/6_6.bmp')

# 根据霍夫圆得到的圆心以及半径以及截取半径之外厚度得到圆环展开后的矩形图片
img = get_huan_by_circle(img, (809, 867), 450, 50)

# 得到展开后的长宽像素
sum_rows = img.shape[0]
sum_cols = img.shape[1]
print(sum_rows, sum_cols)

for_num = sum_cols // 640 if sum_cols % 640 == False else sum_cols // 640 + 1
# # 图片从中间截断
img_size = 0
for i in range(1, for_num+1):
    locals()[f'part{i}'] = img[0:sum_rows, img_size:i*640]
    img_size += 640

# 新建640大小背景图
imgs = np.zeros((640, 640, 3), np.uint8)

# 反转颜色
imgs[0:,0:] = [255,255,255]
# # # 得到图片居中值
# # left_center = int((640 - (sum_cols // 2))/2-1)
# # up_center = int(640//sum_rows/2-1)
# # # 图片进行居中上下拼接
imgs[0:sum_rows, 0:640] = part1
imgs[sum_rows*2:sum_rows*3, 0:640] = part2
imgs[sum_rows*4:sum_rows*5, 0:640] = part3
imgs[sum_rows*6:sum_rows*7, 0:640] = part4
imgs[sum_rows*8:sum_rows*9, 0:sum_cols-((sum_cols//640)*640)] = part5

# # print(imgs.shape)
#
# cv2.imshow("1", part1)
# cv2.imshow("2", part2)
# cv2.imshow("3", part3)
# cv2.imshow("4", part4)
# cv2.imshow("5", part5)
print(img.shape)
cv2.imshow("6", imgs)
cv2.waitKey(0)

