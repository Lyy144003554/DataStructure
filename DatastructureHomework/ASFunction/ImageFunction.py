import cv2 as cv


'''
Founction test of gaining the picture
Version 1.0
2022.07.17 Made by R.e.
'''


def PicGet(path):
    pictest = cv.imread(path, flags=1)
    return pictest


'''
Founction test of the picture information
Version 1.0
2022.07.17 Made by R.e.
'''


def PicInfo(pic):
    print('Type of the picture is:', type(pic))
    print('Dimension of the picture is:{0}'.format(pic.ndim))
    print('Size of the picture is:{0}'.format(pic.size))
    # size = height * width * dimension
    print('Maximum RGB value is:{0}'.format(pic.max()))
    print('Minimum RGB value is:{0}'.format(pic.min()))


'''
Founction test of the picture width and height
Version 1.0
2022.07.18 Made by R.e.
'''


def PicGetWidth(x):
    return x.shape[1]


def PicGetHeight(x):
    return x.shape[0]


'''
Founction test of the Gray Process
Version 2.0
2022.07.19 Made by R.e.
'''


def GrayChanged(x, pic):
    width = PicGetWidth(pic)
    height = PicGetHeight(pic)
    maxgray = 0
    mingray = 100
    w1 = 0.2989
    w2 = 0.5870
    w3 = 0.1140
    for i in range(width):
        for j in range(height):
            r = x.getpixel((i, j))[0]
            g = x.getpixel((i, j))[1]
            b = x.getpixel((i, j))[2]
            gray = r * w1 + g * w2 + b * w3
            if gray > maxgray:
                maxgray = gray
            if gray < mingray:
                mingray = gray
            x.putpixel((i, j), (int(gray), int(gray), int(gray)))
    return [x, maxgray, mingray]


def GetPixelChange(x, i, j):
    row = x.getpixel((i + 1, j))[0] - x.getpixel((i, j))[0]
    column = x.getpixel((i + 1, j))[0] - x.getpixel((i, j))[0]
    bias = x.getpixel((i + 1, j + 1))[0] - x.getpixel((i, j))[0]
    return [row, column, bias]


'''
Basic ImageToGraph function
Version 1.0
2022.07.19 Made by R.e.
'''


def ImageToGraph1(x, pic, g, threshold):
    """
    :param x: Target image must in the type of ImageIO
    :param pic: Use as size estimation
    :param g: Graph
    :param threshold: Man-made parameter
    :return: None
    """
    width = PicGetWidth(pic)
    height = PicGetHeight(pic)
    for i in range(width):
        for j in range(height):
            vertexnum = i * width + j
            g.addVertex(vertexnum)

    for i in range(width - 1):
        for j in range(height - 1):
            row = GetPixelChange(x, i, j)[0]
            column = GetPixelChange(x, i, j)[1]
            bias = GetPixelChange(x, i, j)[2]
            '''
                vertexnum1 — vertexnum2
                    |            |
                    |            |
                    |            |
                vertexnum3 — vertexnum4
            '''
            vertexnum1 = i * width + j
            vertexnum2 = i * width + j + 1
            vertexnum3 = (i + 1) * width + j
            vertexnum4 = (i + 1) * width + j + 1
            '''
            Set a threshold and modified the graph
            '''
            g.addEdge(vertexnum1, vertexnum2, abs(row)) if abs(row) > threshold else g.addEdge(vertexnum1, vertexnum2, 0)
            g.addEdge(vertexnum1, vertexnum3, abs(column)) if abs(column) > threshold else g.addEdge(vertexnum1, vertexnum3, 0)
            g.addEdge(vertexnum1, vertexnum4, abs(bias)) if abs(bias) > threshold else g.addEdge(vertexnum1, vertexnum4, 0)


'''
ImageToGraph function with no threshold
Version 1.0
2022.07.21 Made by R.e.
'''


def ImageToGraph2(x, pic, g):
    """
    :param x: Target image must in the type of ImageIO
    :param pic: Use as size estimation
    :param g: Graph
    :param threshold: Man-made parameter
    :return: None
    """
    width = PicGetWidth(pic)
    height = PicGetHeight(pic)
    for i in range(width):
        for j in range(height):
            vertexnum = i * width + j
            g.addVertex(vertexnum)

    for i in range(width - 1):
        for j in range(height - 1):
            row = GetPixelChange(x, i, j)[0]
            column = GetPixelChange(x, i, j)[1]
            bias = GetPixelChange(x, i, j)[2]
            '''
                vertexnum1 — vertexnum2
                    |            |
                    |            |
                    |            |
                vertexnum3 — vertexnum4
            '''
            vertexnum1 = i * width + j
            vertexnum2 = i * width + j + 1
            vertexnum3 = (i + 1) * width + j
            vertexnum4 = (i + 1) * width + j + 1
            '''
            Set a threshold and modified the graph
            '''
            g.addEdge(vertexnum1, vertexnum2, abs(row))
            g.addEdge(vertexnum1, vertexnum3, abs(column))
            g.addEdge(vertexnum1, vertexnum4, abs(bias))
