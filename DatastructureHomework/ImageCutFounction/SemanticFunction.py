import numpy as np
from PIL import Image
from ASFunction.ImageFunction import PicGet, PicGetWidth, PicGetHeight, GrayChanged

'''
The semanticFunction function
Version 1.0
2022.07.23 Made by R.e.
'''


def GetMax(colorlist):
    """
    Get the max num in the list for pooling
    :param colorlist: The list
    :return: the max value and the index
    """
    max = 0
    index = 0
    for i in range(len(colorlist)):
        if colorlist[i] > max:
            max = colorlist[i]
            index = i + 1
    return [int(max), index]


def ImagePooling(mp, PATH):
    """
    A simple Folding process
    :param mp: Means the multiplying power
    :param x: The original image
    :return: A new image which is modified
    """
    pictest = PicGet(PATH)
    width = PicGetWidth(pictest)
    height = PicGetHeight(pictest)
    x = Image.open(PATH)
    newimage = Image.new("RGB", (int(width / mp + 1), int(height / mp + 1)))
    featurelist1 = []
    featurelist2 = []
    featurelist3 = []
    for i in range(0, int(width / mp) * mp, mp):
        for j in range(0, int(height / mp) * mp, mp):
            '''
                num1 — num2
                 |       |
                 |       |
                num3 — num4
            '''
            colorlist1 = []
            colorlist1.append(x.getpixel((i, j))[0])
            colorlist1.append(x.getpixel((i + 1, j))[0])
            colorlist1.append(x.getpixel((i, j + 1))[0])
            colorlist1.append(x.getpixel((i + 1, j + 1))[0])
            featurelist1.append(GetMax(colorlist1)[1])
            colormax1 = GetMax(colorlist1)[0]
            colorlist2 = []
            colorlist2.append(x.getpixel((i, j))[1])
            colorlist2.append(x.getpixel((i + 1, j))[1])
            colorlist2.append(x.getpixel((i, j + 1))[1])
            colorlist2.append(x.getpixel((i + 1, j + 1))[1])
            featurelist2.append(GetMax(colorlist1)[1])
            colormax2 = GetMax(colorlist2)[0]
            colorlist3 = []
            colorlist3.append(x.getpixel((i, j))[2])
            colorlist3.append(x.getpixel((i + 1, j))[2])
            colorlist3.append(x.getpixel((i, j + 1))[2])
            colorlist3.append(x.getpixel((i + 1, j + 1))[2])
            featurelist3.append(GetMax(colorlist3)[1])
            colormax3 = GetMax(colorlist2)[0]
            newimage.putpixel((0, 0), (colormax1, colormax2, colormax3)) if i == 0 and j == 0 else newimage.putpixel(
                (int(i / mp), int(j / mp)), (colormax1, colormax2, colormax3))
    featurematrix1 = np.asarray(featurelist1)
    featurematrix1 = featurematrix1.reshape([int(width / mp), int(height / mp)])
    featurematrix2 = np.asarray(featurelist2)
    featurematrix2 = featurematrix2.reshape([int(width / mp), int(height / mp)])
    featurematrix3 = np.asarray(featurelist3)
    featurematrix3 = featurematrix3.reshape([int(width / mp), int(height / mp)])
    newimage.save("save.png")
    return [newimage, featurematrix1, featurematrix2, featurematrix3]


def SemanticImage(PATH1, PATH2):
    """
    A Folding test
    :param PATH1: Used to test
    :param PATH2: Used to emerge a feature matrix
    :return:
    """
    # Leaning process
    mp = int(input("enter the size"))
    rmatrix = ImagePooling(mp, PATH2)[1]
    gmatrix = ImagePooling(mp, PATH2)[2]
    bmatrix = ImagePooling(mp, PATH2)[3]
    matrix = rmatrix + gmatrix + bmatrix  # Feature matrix
    featurewidth = matrix.shape[0]
    featureheight = matrix.shape[1]
    # Testing process
    maxposition = 0
    maxpositionx = 0
    maxpositiony = 0
    x = Image.open(PATH1)
    pictest = PicGet(PATH1)
    x = GrayChanged(x, pictest)[0]
    width = PicGetWidth(pictest)
    height = PicGetHeight(pictest)
    colormatrix = []
    for i in range(width - featurewidth):
        for j in range(height - featureheight):
            for includx in range(i, i + featurewidth):
                for includy in range(j, j + featureheight):
                    colormatrix.append(x.getpixel((includx, includy))[0])
            colormatrix = np.asarray(colormatrix)
            colormatrix = colormatrix.reshape(featurewidth, featureheight)
            value = colormatrix * matrix
            sum = 0
            for valuenum in range(len(value)):
                sum += value[0][valuenum]
            if sum > maxposition:
                maxposition = sum
                maxpositionx = i
                maxpositiony = j
            sum = 0
            colormatrix = []
            value = []
    for i in range(width):
        for j in range(height):
            None if i in range(maxpositionx - featureheight * (int(mp / 2) - 1),
                               maxpositionx + featurewidth * int(mp / 2)) \
                    and j in range(maxpositiony - featureheight * (int(mp / 2) - 1),
                                   maxpositiony + featureheight * int(mp / 2)) else \
                x.putpixel((i, j), (0, 0, 0))
    x.save("Semantic.jpg")