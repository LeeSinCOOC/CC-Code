# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:17:40 2019

@author: 陈建
"""

import os
from PIL import Image

os.chdir('12')

img_list = os.listdir()
print(len(img_list))


for i in img_list:
    if (os.path.getsize(i)//1024//1024) > 3: #大于3M就打开再保存
        im = Image.open(i)
        im.save(i,'jpeg')