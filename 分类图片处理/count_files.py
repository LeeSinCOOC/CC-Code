# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:31:16 2019

@author: 陈建
"""
import os


dirs = os.listdir()
count = 0

for i in dirs:
    if os.path.isdir(i):
        count += len(os.listdir(i))
    else:
        pass
print(count)