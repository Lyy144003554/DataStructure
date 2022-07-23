import tkinter as tk
from tkinter import *
import tkinter.filedialog
from ASFunction.ImageFunction import PicGet, PicGetWidth, PicGetHeight
from PIL import Image, ImageTk
from ImageCutFounction.ImageCutFounctionALL import Semantic_Learning_Cut


class GUI_Init(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.path1 = tk.StringVar()
        self.path2 = tk.StringVar()
        self.entry1 = tk.Entry(self, state='readonly', text=self.path1, width=100)
        self.entry1.pack()
        self.entry2 = tk.Entry(self, state='readonly', text=self.path2, width=100)
        self.entry2.pack()
        self.buttonSelImage1 = tk.Button(self, text='Choose the learning and testing picture', command=self.ImageGet)
        self.buttonSelImage1.pack()
        self.lableShowImage = tk.Label(self)
        self.lableShowImage.pack()
        self.root = master
        self.mainloop()

    def ImageGet(self):
        imagepath1 = tkinter.filedialog.askopenfilename()
        self.path1.set(imagepath1)
        imagepath2 = tkinter.filedialog.askopenfilename()
        self.path2.set(imagepath2)
        PATH1 = self.entry1.get()
        PATH2 = self.entry2.get()
        pictest = PicGet(PATH2)
        width = PicGetWidth(pictest)
        height = PicGetHeight(pictest)
        Semantic_Learning_Cut(PATH2, PATH1)
        x = Image.open("Semantic.jpg")
        img = ImageTk.PhotoImage(x.resize((int(width / (height / 200)), 200)))
        self.lableShowImage.config(image=img)
        self.lableShowImage.image = img

def Semantic_GUI_Init(root):
    root.title("Using the Minimal-cost to cut the picture which is not totally correct")
    root.geometry("500x270+100+100")
    GUI_Init(root)
