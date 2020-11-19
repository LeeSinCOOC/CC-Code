# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:40:57 2020

@author: CC
"""
import os
import cv2 as cv
from hyperlpr import * #hyperlpr 是开源的中文车牌检测库
import numpy
from PIL import Image, ImageDraw, ImageFont

image = ['LP/{}'.format(i) for i in os.listdir('LP')]

def cv2ImgAddText(img, text, left, top, textColor=(255, 255, 0), textSize=40):
    '''
    解决CV的中文显示问题
    '''
    if (isinstance(img, numpy.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv.cvtColor(numpy.asarray(img), cv.COLOR_RGB2BGR)


for img in image:
    im = cv.imread(img)
    pre =HyperLPR_plate_recognition(im)
    
    im = cv.rectangle(im,(pre[0][2][0],pre[0][2][1]),
                           (pre[0][2][2],pre[0][2][3]),(0,0,255),2)
    
#    font = cv.FONT_HERSHEY_PLAIN
    text = pre[0][0]
    
#    cv.putText(img,text,(pre[0][2][0],pre[0][2][1]),font,2,(0,0,255),1)
    write = cv2ImgAddText(im,text,pre[0][2][0],pre[0][2][1]-40)
    cv.imwrite(img.split('.')[0]+'LP.'+img.split('.')[1],write)
    
