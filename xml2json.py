import xml.etree.ElementTree as ET
import json
import os
import re
import numpy as np

def coss_multi(v1, v2):
    """
    计算两个向量的叉乘
    :param v1:
    :param v2:
    :return:
    """
    return v1[0]*v2[1] - v1[1]*v2[0]
def polygon_area(polygon):
    """
    计算多边形的面积，支持非凸情况
    :param polygon: 多边形顶点，已经进行顺次逆时针排序
    :return: 该多边形的面积
    """
    n = len(polygon)
 
    if n < 3:
        return 0
 
    vectors = np.zeros((n, 2))
    for i in range(0, n):
        vectors[i, :] = polygon[i, :] - polygon[0, :]
 
    area = 0
    for i in range(1, n):
        area = area + coss_multi(vectors[i-1, :], vectors[i, :]) / 2
 
    return abs(area)
def get(root, name):
    vars = root.findall(name)
    return vars

def get_and_check(root, name, length):
    vars = root.findall(name)
    if len(vars) == 0:
        raise NotImplementedError('Can not find %s in %s.'%(name, root.tag))
    if length > 0 and len(vars) != length:
        raise NotImplementedError('The size of %s is supposed to be %d, but is %d.'%(name, length, len(vars)))
    if length == 1:
        vars = vars[0]
    return vars
def parseXML(xmlname):
    tree = ET.parse(xmlname)
    root = tree.getroot()

    filename = root.findall('filename')[0].text
    width = root.findall('size')[0].findall('width')[0].text
    height = root.findall('size')[0].findall('height')[0].text
    polygon = root.findall('polygon')
    for i in polygon:
        break

    print(width)


    return

def parseMain(dir,json_file):
    dic = {}
    dic['info'] = {"description":"parse-xml-coco"}
    dic['images'] = []
    dic['annotations'] = []
    dic["categories"] = [{"id":1,"name":"pig_body"},{"id":2,"name":"pig_head"}]

    for i,xmlname in enumerate(os.listdir(dir),start=1):
        print('正在处理：{}######{}'.format(i,xmlname))
        tree = ET.parse(os.path.join(dir,xmlname))
        root = tree.getroot()
        filename = root.findall('filename')[0].text
        width = root.findall('size')[0].findall('width')[0].text
        height = root.findall('size')[0].findall('height')[0].text

      
        dic['images'].append({
            'id':i,
            "width":width,
            "height":height,
            "file_name":filename
        })
        
        polygon = root.findall('polygon')
        for j,ploy in enumerate(polygon,start=1):
            print('正在处理：{}'.format(j))
            id = j
            iscrowd=0
            image_id=i
            category_id = 1 if ploy.attrib['label'] == '猪' else 2

            # 分割points
            poins = ploy.attrib['points']
            segmentation = [ float(i) for i in re.split(r'[,;]\s*',poins)[:-1]]

            xmin = min(segmentation[::2])
            xmax = max(segmentation[::2])
            ymin = min(segmentation[1:-1:2])
            ymax = max(segmentation[1:-1:2])
            w = xmax - xmin
            h = ymax - ymin

            

            # 多点面积计算
            area_list = []
            for p in range(len(segmentation))[::2]:
                area_list.append([segmentation[p],segmentation[p+1]])
            point_array = np.asarray(area_list)
            area = polygon_area(point_array)
            bbox = [xmin,ymin,w,h]

            # segmentation    
            dic['annotations'].append({
            'id':id,
            "iscrowd":iscrowd,
            "image_id":image_id,
            "category_id":category_id,
            'segmentation':segmentation,
            'bbox':bbox,
            'area':area,
        })

    with open(json_file,'w') as f:
        json.dump(dic,f,indent=4)
    

if __name__ == "__main__":
    json_file = 'train.json'
    dir = 'xmldir'

    parseMain(dir,json_file)
