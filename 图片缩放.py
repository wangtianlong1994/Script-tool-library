import os
from PIL import Image

imgs = os.listdir("img")

for i in imgs:
    print(i)
    im = Image.open("img/"+i)
    (x,y) = im.size #read image size
    x_s = 640 #define standard width
    y_s = 640 #calc height based on standard width
    out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality

    out.save("640/"+i.split(".")[0]+".bmp")

# import os
# from PIL import Image
# # open an image file (.jpg or.png) you have in the working folder
# imgs = os.listdir("savepath")
# for i in imgs:
#     im1 = Image.open("savepath/"+i)
#     im2 = im1.point(lambda p: p * 1.2)
#     im2.save("1/"+i)
