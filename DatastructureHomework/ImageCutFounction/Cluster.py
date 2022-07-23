from ASFunction.ImageFunction import PicGetHeight
from ASFunction.ImageFunction import PicGetWidth

"""
Basic Cluster founction (tested)
Version 3.0
2022.07.21 Made by R.e.
"""


def Cluster(x, pic, max, min):
    """
    :param x: Target image must in the type of ImageIO
    :param pic: Use as size estimation
    :param max: The max of gray to set a scpoe
    :param min: The min of gray to set a scpoe
    :return: None
    """
    width = PicGetWidth(pic)
    height = PicGetHeight(pic)
    clusternum = int(input("Please type the aim number of cluster"))
    thresholdlist = []
    colorlist = []
    for i in range(clusternum):
        thresholdlist.append(int(min+(i/clusternum)*(max-min)))
    print(thresholdlist)
    '''
    The color is changed refer to thresholdlist
    '''
    for i in range((width - 1)):
        for j in range((height - 1)):
            for k in range(clusternum-1):
                if x.getpixel((i, j))[0] <= thresholdlist[0]:
                    x.putpixel((i, j), (0, 0, 0))
                if x.getpixel((i, j))[0] >= thresholdlist[clusternum-1]:
                    x.putpixel((i, j), (255, 255, 255))
                if thresholdlist[k] < x.getpixel((i, j))[0] < thresholdlist[k+1]:
                    x.putpixel((i, j), (int(((k+1)/clusternum)*255), int(((clusternum-k+1)/clusternum)*255), 0))
                    colorlist.append(int(((k+1)/clusternum)*255))
                    colorlist.append(int(((clusternum-k+1)/clusternum)*255))
                    colorlist.append(0)
    for i in range((width - 1)):
        for j in range((height - 1)):
            r = x.getpixel((i, j))[0]
            g = x.getpixel((i, j))[1]
            b = x.getpixel((i, j))[2]
            if r == 0 and g == 0 and b == 0:
                x.putpixel((i, j), (colorlist[len(colorlist)-3], colorlist[len(colorlist)-2], colorlist[len(colorlist)-1]))
    x.save("Cluster1.jpg")
