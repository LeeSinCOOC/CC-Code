import os
import configparser
import shutil
import random
from tqdm import *

'''
VOC数据集制作脚本
'''

config = configparser.ConfigParser()
config.read('config')

sourceimgs = config['Images']['path']
xmls = config['XMLs']['path']
train_percent = float(config['split']['train_percent'])
val_percent = float(config['split']['val_percent'])

def mkdir():
    print('*' * 20)
    os.makedirs('VOC2007/Annotations')
    os.makedirs('VOC2007/ImageSets/Main')
    os.makedirs('VOC2007/JPEGImages')
    print('VOC2007文件夹创建成功')
    print('*' * 20)

def copyimg(sourceimgs):
    print('*' * 20)
    images = os.listdir(sourceimgs)
    for i in tqdm(images):
        path = os.path.join(sourceimgs,i)
        shutil.copyfile(path,os.path.join('VOC2007/JPEGImages',i))
    print('图片复制完成')
    print('*' * 20)

def copyxml(xmls):
    print('*' * 20)
    xml = os.listdir(xmls)
    for i in tqdm(xml):
        path = os.path.join(xmls,i)
        shutil.copyfile(path,os.path.join('VOC2007/Annotations',i))
    print('标注文件复制完成')
    print('*' * 20)

def split():
    print('*'*20)
    xmlfilepath = 'VOC2007/Annotations'
    txtsavepath = 'VOC2007/ImageSets/Main'
    total_xml = os.listdir(xmlfilepath)

    num = len(total_xml)
    list = range(num)
    tr = int(num * train_percent)
    tv = int(tr * val_percent)
    trainval = random.sample(list, tr)
    val = random.sample(trainval,tv)

    ftrainval = open('VOC2007/ImageSets/Main/trainval.txt', 'w')
    ftest = open('VOC2007/ImageSets/Main/test.txt', 'w')
    ftrain = open('VOC2007/ImageSets/Main/train.txt', 'w')
    fval = open('VOC2007/ImageSets/Main/val.txt', 'w')

    for i in tqdm(list):
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in val:
                fval.write(name)
            else:
                ftrain.write(name)
        else:
            ftest.write(name)

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()
    print('数据集划分完成')
    print('*' * 20)



if __name__ == "__main__":
    mkdir()
    copyimg(sourceimgs)
    copyxml(xmls)
    split()

'''
#config
[Images]
path = P:/Pig/raccoon/images
[XMLs]
path = P:/Pig/raccoon/annotations

[split]
train_percent = 0.8
val_percent = 0.2



