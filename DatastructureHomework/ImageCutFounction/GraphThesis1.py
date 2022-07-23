from ASFunction.ImageFunction import PicGetWidth
from ASFunction.ImageFunction import PicGetHeight
from ASFunction.GraphFunction import Graph


def GraphThesis1(x, pic, g, threshold):
    """
    Test of the graphthesis
    Version 1.0
    2022.07.20 Made by R.e.
    :param x: Target image must in the type of ImageIO
    :param pic: Use as size estimation
    :param g: Graph
    :param threshold: Man-made parameter
    :return: None
    """
    width = PicGetWidth(pic)
    height = PicGetHeight(pic)
    catgeory = 0
    for i in range((width - 1)):
        for j in range((height - 1)):
            vertexnum1 = i * width + j
            vertexnum2 = i * width + j + 1
            vertexnum3 = (i + 1) * width + j
            vertexnum4 = (i + 1) * width + j + 1
            if (g.cost(vertexnum1, vertexnum2) > threshold or g.cost(vertexnum1, vertexnum3) > threshold or g.cost(
                    vertexnum1, vertexnum4) > threshold):
                '''
                If the pixel have some common then put black
                '''
                x.putpixel((i, j), (255, 255, 255))
                catgeory += 1
            else:
                '''
                If the pixel have some common then put red
                '''
                x.putpixel((i, j), (0, 0, 0))
            if (g.cost(vertexnum1, vertexnum2) > threshold and g.cost(vertexnum1, vertexnum3) > threshold and g.cost(
                    vertexnum1, vertexnum4) > threshold):
                catgeory += 1
    x.save("Graph1.png")
    return x
