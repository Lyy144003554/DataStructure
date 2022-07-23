from tkinter import *

from GUIFunction.ClusterSegmentation import Cluster_GUI_Init
from GUIFunction.GraphSegmentation import Graph_GUI_Init
from GUIFunction.SemanticSegmentation import Senmantic_GUI_Init

def to_Cluster(root):
    root.destroy()
    newroot = Tk()
    Cluster_GUI_Init(newroot)

def to_Graph(root):
    root.destroy()
    newroot = Tk()
    Graph_GUI_Init(newroot)

def to_Senmantic(root):
    root.destroy()
    newroot = Tk()
    Senmantic_GUI_Init(newroot)

