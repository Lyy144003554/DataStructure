from ImageCutFounction.ImageCutFounctionALL import Graph_Simple_Cut
from ASFunction.ImageFunction import PicGet, PicGetWidth, PicGetHeight

if __name__ == '__main__':
    Ori_PATH = "PictureTest/pictest1.jpg"
    Target_PATH = "Cluster2.jpg"
    ori_image = Graph_Simple_Cut(Ori_PATH)
    target_image = Graph_Simple_Cut(Target_PATH)
    ori_image.show()
    pictest = PicGet(Target_PATH)
    width = PicGetWidth(pictest)
    height = PicGetHeight(pictest)
    wrong = 0
    all = 0
    for i in range(width):
        for j in range(height):
            if ori_image.getpixel((i, j))[0] == 255:
                all += 1
            if target_image.getpixel((i, j))[0] == 255:
                if ori_image.getpixel((i, j))[0] != 255:
                    wrong += 1
    print(wrong/all)

