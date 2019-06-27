# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:59:00 2019

@author: 陈建
"""
'''
windows和Linux采用了不同的路径分隔符
“/”和"\"。我最喜欢的方法是os.path.join方法，提高了我们代码可移植性。比如下面代码:
os.path.join("python", "django", "some.py")
'''

#查找某个目录下的全部txt文件并删除
import os
'''
os.rename()
os.remove()
'''
os.listdir('chen')
for filename in os.listdir('jian'):
    if filename endswith('.txt'):
        os.remove(os.path.join('basedir',filename))
        
#使用os.walk()遍历一个文件夹子目录查找所有txt文件并删除
for foldName, subfolders, filenames in os.walk('tutorial'):        

    
#利用shutil模块复制和移动文件
'''
shutil.copy()用来复制文件，第一个参数是需要复制的文件，第二个参数可以是文件夹，
也可以是个文件名。如果是文件夹，新文件将存储在新文件夹里，文件名不变。如果是文件名，
则新文件直接以文件名命名。shutil.copyfile()与shutil.copy()类似，只不过2个参数都
必需是文件名。
'''
# 复制文件夹. olddir和newdir都只能是目录，且newdir必须不存在
shutil.copytree("老目录", "新目录")

# 移动文件（目录）
shutil.move("老位置", "新位置") 

#利用glob模块快速查找当前文件夹文件
'''
glob支持三个匹配符：”*”, “?”, “[]”。”*”匹配0个或多个字符；”?”匹配单个字符；”[]”匹配指定范围内的字符.
'''
>>> import os
>>> os.getcwd()
'C:\\Users\\MissEnka\\Python'
>>> import glob
>>> glob.glob('*.txt')
['LICENSE.txt', 'list.txt', 'NEWS.txt']
>>> glob.glob('tutorial/.txt')
[]
>>> glob.glob('tutorial/*.txt')
['tutorial\\new.txt']

