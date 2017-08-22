#coding:utf-8
from PIL import Image
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

img1 = Image.open("aa.png").convert('L')
img2 = Image.open("bb.png").convert('L')
region = (65,718,324,832)

#裁切图片
cropImg1 = img1.crop(region)
cropImg2 = img2.crop(region)
x,y = cropImg1.size
print x,y
#反相
img1 = array(cropImg1)
img2 = img1 - array(cropImg2)


#保存裁切后的图片
cropImg1.save('crop1.jpg')
cropImg2.save('crop2.jpg')

for i in range(x):
    for j in range(y):
        #print img2[j,i],j,i
        if img2[j,i] >= 230:   #255白色
            img2[j,i] = 0

img3 = Image.fromarray(img2)
img3.save("fanxiang.jpg")

pixCount = [0] * x
for i in range(x):
    for j in range(y):
        if img2[j,i] > 100:
            pixCount[i] = pixCount[i] + 1
print pixCount



for i in range(x):
    if i > 61 and pixCount[i] > 20:
        print i
        endx = i
        break
        



img=np.array(pixCount)

plt.bar(range(len(pixCount)), pixCount)
#plt.show()





