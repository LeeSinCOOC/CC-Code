# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:32:19 2019

@author: 陈建
func:
    用PIL将图片打开再保存
"""
import os
import glob
import shutil
from PIL import Image

jpg_list = glob.glob('*.jpg')

os.mkdir('resize_img')

j = 0
for i in jpg_list:
    img_file = Image.open(i)
    path =r"C:\Users\陈建\Desktop\test_pil"
    path_all = os.path.join(path,r'resize_img',str(j)+'.jpg')
    img_file.save(path_all)
    j += 1
