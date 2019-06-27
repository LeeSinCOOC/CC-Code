# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:54:41 2019

@author: 陈建
func:
    将图片未标记的废弃数据进行提取
"""

import os 
import glob
import shutil


xml_list = glob.glob('*.xml')
num_list = [i[:-4] for i in xml_list]

jpg_list = glob.glob('*.jpg')

try:
    os.mkdir('discard')
except:
    print('已存在文件夹')
    
for i in jpg_list:
    if i[:-4] in num_list:
        pass
    else:
        shutil.copy(i,'discard')

