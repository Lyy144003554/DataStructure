from tkinter import *
from Graph1Panel import Graph1_GUI_Init
from Graph2Panel import Graph2_GUI_Init


'''
The graph function panel for choosing the classification
Version 1.0
2022.07.23 Made by R.e.
'''


class GUIGraph(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
        self.root = master

    def createWidget(self):
        self.infoLabel1 = Label(self, text="The graph function used two methods")
        self.infoLabel1.pack()
        self.infoLabel2 = Label(self, text="1 - Using the Edge-feature to cut the picture which gain the border")
        self.infoLabel2.pack()
        self.infoLabel2 = Label(self, text="2 - Using the Minimal-cost to cut the picture which is not totally correct")
        self.infoLabel2.pack()
        self.btnMode1 = Button(self, text="Function1", command=self.function1)
        self.btnMode1.pack()
        self.btnMode2 = Button(self, text="Function2", command=self.function2)
        self.btnMode2.pack()
        # self.xVariable = tkinter.StringVar()  # #设定一个字符串类型的变量
        # self.sb = tkinter.Spinbox(self, from_=0, to=100, increment=1, textvariable=self.xVariable, command=self.xFunc)
        # self.sb.pack()

    def function1(self):
        self.root.destroy()
        newroot = Tk()
        Graph1_GUI_Init(newroot)

    def function2(self):
        self.root.destroy()
        newroot = Tk()
        Graph2_GUI_Init(newroot)


def Graph_GUI_Init(root):
    root.geometry("500x135+100+100")
    root.title("A GUI for easily test the image-cutting function")
    app = GUIGraph(master=root)
    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    Graph_GUI_Init(root)
