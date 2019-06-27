# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:58:08 2019

@author: 陈建
"""

import os
import glob
import shutil
from PIL import Image

os.chdir('12')

img_list = os.listdir()
print(img_list)
for i in img_list:
    im = Image.open(i)

#    左右旋转
    out1 = im.transpose(Image.FLIP_LEFT_RIGHT)
    out1.save(i.split('.')[0]+'_FLR.'+i.split('.')[1],'jpeg')
    
#    上下旋转
    out2 = im.transpose(Image.FLIP_TOP_BOTTOM)
    out2.save(i.split('.')[0]+'_FTB.'+i.split('.')[1],'jpeg')
    

#   旋转180  
img_list = os.listdir()
print(img_list)   
for i in img_list:
    im = Image.open(i)
    out3 = im.transpose(Image.ROTATE_180)
    out3.save(i.split('.')[0]+'_R180.'+i.split('.')[1],'jpeg')    


