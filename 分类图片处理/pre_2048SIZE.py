# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 11:40:15 2019

@author: CC
"""

import os
import PIL

os.chdir('0')
img_list = os.listdir()

print(img_list)

for i in img_list:
    im = PIL.Image.open(i)
    img_w = im.size[0]
    img_h = im.size[1]
    temp = int((img_w - img_h)/2)
    new_img = im.crop([temp,0,img_w-temp,img_h])
    new_img = new_img.resize((2048,2048),PIL.Image.ANTIALIAS)
    new_img.save("mini_"+i)