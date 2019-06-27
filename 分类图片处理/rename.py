# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:03:38 2019

@author: 陈建
"""
import os
from PIL import Image

os.chdir('12')

img_list = os.listdir()
print(len(img_list))

base_path = os.getcwd()

n = 0
for i in img_list:
    os.rename(os.path.join(base_path,i),os.path.join(base_path,'12_'+str(n)+'.jpg')) 
    if n % 100 == 0:
        print(str(n)+':ok')
    n += 1