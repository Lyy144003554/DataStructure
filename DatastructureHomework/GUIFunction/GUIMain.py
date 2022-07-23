import tkinter
from tkinter import *
from PanelChange import to_Cluster, to_Graph, to_Senmantic

'''
The main GUI panel for choosing the classification
Version 1.0
2022.07.23 Made by R.e.
'''


class GUIMain(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
        self.root = master

    def createWidget(self):
        self.infoLabel = Label(self, text="You can choose different functions of the image cutting with the following buttons")
        self.infoLabel.pack()
        self.btnMode1 = Button(self, text="Cluster-Segmentation", command=self.mode1Enter)
        self.btnMode1.pack()
        self.btnMode2 = Button(self, text="Grapth-thesis-Segmentation", command=self.mode2Enter)
        self.btnMode2.pack()
        self.btnMode3 = Button(self, text="Semantic-Segmentation", command=self.mode3Enter)
        self.btnMode3.pack()
        self.xVariable = tkinter.StringVar()  # #设定一个字符串类型的变量
        # self.sb = tkinter.Spinbox(self, from_=0, to=100, increment=1, textvariable=self.xVariable, command=self.xFunc)
        # self.sb.pack()

    def mode1Enter(self):
        to_Cluster(root)
        pass

    def mode2Enter(self):
        to_Graph(root)
        pass

    def mode3Enter(self):
        to_Senmantic(root)
        pass


def Main_GUI_Init(root):
    root.geometry("500x120+100+100")
    root.title("A GUI for easily test the image-cutting function")
    app = GUIMain(master=root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    Main_GUI_Init(root)
