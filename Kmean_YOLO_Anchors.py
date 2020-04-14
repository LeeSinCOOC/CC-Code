# _*_ coding: utf-8 _*_
import numpy as np
import glob
import xml.etree.ElementTree as ET

'''
使用kmeans聚类算法对自己的数据集进行anchor聚类
使用方法：1.更改ANNOTATIONS_PATH为自己的xml文件路径
         2.更改CLUSTERS为自己想要聚类的类别数
'''
ANNOTATIONS_PATH = "/home/administrator/MX_Obj_Det/dark/darknet-master/VOCdevkit/VOC2007/Annotations"
CLUSTERS = 9

def iou(box, clusters):
    """
    Calculates the Intersection over Union (IoU) between a box and k clusters.
    :param box: tuple or array, shifted to the origin (i. e. width and height)
    :param clusters: numpy array of shape (k, 2) where k is the number of clusters
    :return: numpy array of shape (k, 0) where k is the number of clusters
    """
    x = np.minimum(clusters[:, 0], box[0])
    y = np.minimum(clusters[:, 1], box[1])
    if np.count_nonzero(x == 0) > 0 or np.count_nonzero(y == 0) > 0:
        raise ValueError("Box has no area")

    intersection = x * y
    box_area = box[0] * box[1]
    cluster_area = clusters[:, 0] * clusters[:, 1]

    iou_ = intersection / (box_area + cluster_area - intersection)

    return iou_


def avg_iou(boxes, clusters):
    """
    Calculates the average Intersection over Union (IoU) between a numpy array of boxes and k clusters.
    :param boxes: numpy array of shape (r, 2), where r is the number of rows
    :param clusters: numpy array of shape (k, 2) where k is the number of clusters
    :return: average IoU as a single float
    """
    return np.mean([np.max(iou(boxes[i], clusters)) for i in range(boxes.shape[0])])


def translate_boxes(boxes):
    """
    Translates all the boxes to the origin.
    :param boxes: numpy array of shape (r, 4)
    :return: numpy array of shape (r, 2)
    """
    new_boxes = boxes.copy()
    for row in range(new_boxes.shape[0]):
        new_boxes[row][2] = np.abs(new_boxes[row][2] - new_boxes[row][0])
        new_boxes[row][3] = np.abs(new_boxes[row][3] - new_boxes[row][1])
    return np.delete(new_boxes, [0, 1], axis=1)


def kmeans(boxes, k, dist=np.median):
    """
    Calculates k-means clustering with the Intersection over Union (IoU) metric.
    :param boxes: numpy array of shape (r, 2), where r is the number of rows
    :param k: number of clusters
    :param dist: distance function
    :return: numpy array of shape (k, 2)
    """
    rows = boxes.shape[0]

    distances = np.empty((rows, k))
    last_clusters = np.zeros((rows,))

    np.random.seed()

    # the Forgy method will fail if the whole array contains the same rows
    clusters = boxes[np.random.choice(rows, k, replace=False)]

    while True:
        for row in range(rows):
            distances[row] = 1 - iou(boxes[row], clusters)

        nearest_clusters = np.argmin(distances, axis=1)

        if (last_clusters == nearest_clusters).all():
            break

        for cluster in range(k):
            clusters[cluster] = dist(boxes[nearest_clusters == cluster], axis=0)

        last_clusters = nearest_clusters

    return clusters


def load_dataset(path):
	dataset = []
	for xml_file in glob.glob("{}/*xml".format(path)):
		# print(xml_file)
		tree = ET.parse(xml_file)

		height = int(tree.findtext("./size/height"))
		width = int(tree.findtext("./size/width"))

		for obj in tree.iter("object"):
			xmin = int(float(obj.findtext("bndbox/xmin"))) / width
			ymin = int(float(obj.findtext("bndbox/ymin"))) / height
			xmax = int(float(obj.findtext("bndbox/xmax"))) / width
			ymax = int(float(obj.findtext("bndbox/ymax"))) / height

			dataset.append([xmax - xmin, ymax - ymin])

	return np.array(dataset)


data = load_dataset(ANNOTATIONS_PATH)
print('Data shape is {}'.format(data.shape))
out = kmeans(data, k=CLUSTERS)

yolov3clusters = [[10,13],[16,30],[33,23],[30,61],[62,45],[59,119],[116,90],[156,198],[373,326]]
yolov3out= np.array(yolov3clusters)/416.0

print("Self data Accuracy: {:.2f}%".format(avg_iou(data, out) * 100))
print("Yolov3 Accuracy: {:.2f}%".format(avg_iou(data, yolov3out) * 100))

# 生成resize到416对应的anchor
print("Boxes:\n {}-{}".format(out[:, 0]*416, out[:, 1]*416))
# print("Boxes:\n {}".format(out))


yolov3_out_clusters = [[int(i),int(j)] for i,j in zip(out[:, 0]*416, out[:, 1]*416)]
print('\n' +  '*'*10 + "生成的Anchors:" + '*'*10 + '\n' +
      str(yolov3_out_clusters) + '\n' )


ratios = np.around(out[:, 0] / out[:, 1], decimals=2).tolist()
print("Ratios:\n {}".format(sorted(ratios)))
