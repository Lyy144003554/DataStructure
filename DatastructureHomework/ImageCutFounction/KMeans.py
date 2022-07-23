import numpy as np
from PIL import Image
from  ASFunction.ImageFunction import PicGetWidth, PicGetHeight, PicGet
from sklearn.cluster import KMeans


def TransMatrix(PATH):
    x = Image.open(PATH)
    pictest = PicGet(PATH)
    width = PicGetWidth(pictest)
    height = PicGetHeight(pictest)
    imagedata = []
    for i in range(width):
        for j in range(height):
            r, g, b = x.getpixel((i, j))
            imagedata.append([r / 256.0, g / 256.0, b / 256.0])
    return np.asarray(imagedata), width, height


def ClusterLabel(PATH):
    data, width, height = TransMatrix(PATH)
    k = int(input("Please type the aim number of cluster"))
    label = KMeans(n_clusters=k).fit_predict(data)
    label = label.reshape([width, height])
    return [label, k]
