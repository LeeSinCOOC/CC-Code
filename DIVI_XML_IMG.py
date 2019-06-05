# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:13:12 2019

@author: 陈建
function:
    将xml文件分离出来存放在15行注释文件夹内
"""
import os
from glob import glob
import shutil
xml_list = glob('*xml')
print(len(xml_list))

try:
    os.makedirs('xml')
except:
    print('已存在')
    
for i in xml_list:
    shutil.move(i,'xml')
