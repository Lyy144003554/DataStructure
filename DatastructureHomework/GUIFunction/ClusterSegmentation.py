from tkinter import *
from Cluster1Panel import Cluster1_GUI_Init
from Cluster2Panel import Cluster2_GUI_Init

'''
The cluster function panel for choosing the classification
Version 1.0
2022.07.23 Made by R.e.
'''


class GUICluster(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
        self.root = master

    def createWidget(self):
        self.infoLabel1 = Label(self, text="The cluster function used two methods")
        self.infoLabel1.pack()
        self.infoLabel2 = Label(self, text="1 - Using the average pixel value as threshold")
        self.infoLabel2.pack()
        self.infoLabel3 = Label(self, text="2 - Using the average pixel distance as threshold")
        self.infoLabel3.pack()
        self.btnMode1 = Button(self, text="Function1", command=self.function1)
        self.btnMode1.pack()
        self.btnMode2 = Button(self, text="Function2", command=self.function2)
        self.btnMode2.pack()

    def function1(self):
        self.root.destroy()
        newroot = Tk()
        Cluster1_GUI_Init(newroot)

    def function2(self):
        self.root.destroy()
        newroot = Tk()
        Cluster2_GUI_Init(newroot)


def Cluster_GUI_Init(root):
    root.geometry("500x135+100+100")
    root.title("A GUI for easily test the image-cutting function")
    app = GUICluster(master=root)
    root.mainloop()




