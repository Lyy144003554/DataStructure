from PIL import Image
from ASFunction.ImageFunction import GrayChanged, ImageToGraph1, PicGet, PicGetWidth, PicGetHeight
from ASFunction.GraphFunction import Graph
from ImageCutFounction.GraphThesis1 import GraphThesis1
from ImageCutFounction.GraphThesis2 import TestMST, putpixelMST
from ImageCutFounction.KMeans import ClusterLabel
from ImageCutFounction.Cluster import Cluster
from ImageCutFounction.SemanticFunction import SemanticImage


'''
The pixel cluster function is tested over
Version 1.0
2022.07.19 Made by R.e.
'''


def Cluster_Pixel_Cut(PATH):
    pictest = PicGet(PATH)  # Picture Init
    x = Image.open(PATH)  # Image Init
    maxgray = GrayChanged(x, pictest)[1]
    mingray = GrayChanged(x, pictest)[2]
    Cluster(x, pictest, maxgray, mingray)  # Test the cluster function


'''
The kmeans cluster function is tested over
Version 2.0
2022.07.22 Made by R.e.
'''


def Cluster_KMeans_Cut(PATH):
    pictest = PicGet(PATH)  # Picture Init
    width = PicGetWidth(pictest)
    height= PicGetHeight(pictest)
    label, clusternum = ClusterLabel(PATH)
    thresholdlist = []
    x = Image.new("RGB", (width, height))
    for i in range(width):
        for j in range(height):
            if int(256 / (label[i][j] + 1)) not in thresholdlist:
                thresholdlist.append(int(256 / (label[i][j] + 1)))
    for i in range(width):
        for j in range(height):
            for k in range(len(thresholdlist)):
                if int(256 / (label[i][j] + 1)) == thresholdlist[k]:
                    r = int(((k+1)/clusternum)*255)
                    g = int(((clusternum-k+1)/clusternum)*255)
                    b = 0
                x.putpixel((i, j), (r, g, b))
    x.save("Cluster2.png")

'''
The GraphThesis1 function is tested over
Version 1.0
2022.07.20 Made by R.e.
'''


def Graph_Simple_Cut(PATH):
    pictest = PicGet(PATH)  # Picture Init
    x = Image.open(PATH)  # Image Init
    g = Graph()  # Graph Init
    threshold = 40  # Threshold Init
    ImageToGraph1(x, pictest, g, threshold)
    out = GraphThesis1(x, pictest, g, threshold)
    return out


'''
The GraphThesis function is tested over(emerge a mask)
Version 2.0
2022.07.22 Made by R.e.
'''


def Graph_Mask_Cut(PATH):
    pictest = PicGet(PATH)  # Picture Init
    x = Image.open(PATH)  # Image Init
    x = GrayChanged(x, pictest)[0]  # Gray Init
    g = Graph()  # Graph Init
    width = PicGetWidth(pictest)
    height = PicGetHeight(pictest)
    ImageToGraph1(x, pictest, g, 20)
    for i in range(width):
        treelist = TestMST(g, pictest, width*i, 1, 0)[0]
        putpixelMST(pictest, x, treelist)
    for i in range(width):
        for j in range(height):
            if x.getpixel((i, j))[0] != 0 and x.getpixel((i, j))[1] != 0 and x.getpixel((i, j))[2] != 0:
                x.putpixel((i, j), (0, 255, 0))
    x.save("Graph2.png")


'''
The Semantic Function function is tested over
Version 1.0
2022.07.22 Made by R.e.
'''


def Semantic_Learning_Cut(PATH1, PATH2):
    SemanticImage(PATH1, PATH2)

