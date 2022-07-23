from tkinter import *
from SemanticPanel import Semantic_GUI_Init

'''
The cluster function panel for choosing the classification
Version 1.0
2022.07.23 Made by R.e.
'''


class GUISemantic(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
        self.root = master

    def createWidget(self):
        self.infoLabel1 = Label(self, text="The semantic function can gain a special place by leaning the aiming image")
        self.infoLabel1.pack()
        self.infoLabel2 = Label(self, text="You should input a feature image first")
        self.infoLabel2.pack()
        self.infoLabel2 = Label(self, text="This will help you to locate the aiming position")
        self.infoLabel2.pack()
        self.btnMode1 = Button(self, text="I known", command=self.function)
        self.btnMode1.pack()

    def function(self):
        self.root.destroy()
        newroot = Tk()
        Semantic_GUI_Init(newroot)


def Senmantic_GUI_Init(root):
    root.geometry("500x105+100+100")
    root.title("A GUI for easily test the image-cutting function")
    app = GUISemantic(master=root)
    root.mainloop()

