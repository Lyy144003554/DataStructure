from ImageCutFounction.ImageCutFounctionALL import Cluster_KMeans_Cut, Graph_Mask_Cut, Semantic_Learning_Cut

PATH = "PictureTest/pictest4.png"
originpath = "PictureTest/FoldingTest.jpg"
aimpath = "PictureTest/FoldingAim.jpg"
if __name__ == '__main__':
    Semantic_Learning_Cut(originpath, aimpath)