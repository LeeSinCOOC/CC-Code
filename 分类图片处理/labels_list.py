# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:56:15 2019

@author: 陈建
"""

import os
class_names_to_ids = {'0': 0, 
                      '1': 1,
                      '2': 2,
                      '3': 3,
                      '4': 4,
                      '5': 5,
                      '6': 6,
                      '7': 7,
                      '8': 8,
                      '9': 9,
                      '10': 10,
                      '11': 11,
                      '12': 12,
                      }
data_dir = os.getcwd()
output_path = 'list.txt'
fd = open(output_path, 'a+')
for class_name in class_names_to_ids.keys():
    images_list = os.listdir(os.path.join(data_dir,class_name))
    for image_name in images_list:
        fd.write('{}/{} {}\n'.format(class_name, image_name, class_names_to_ids[class_name]))
fd.close()
