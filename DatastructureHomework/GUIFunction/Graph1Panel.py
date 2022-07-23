import tkinter as tk
from tkinter import *
import tkinter.filedialog
from ASFunction.ImageFunction import PicGet, PicGetWidth, PicGetHeight
from PIL import Image, ImageTk
from ImageCutFounction.ImageCutFounctionALL import Graph_Simple_Cut


class GUI_Init(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.path = tk.StringVar()
        self.entry = tk.Entry(self, state='readonly', text=self.path, width=100)
        self.entry.pack()
        self.buttonSelImage = tk.Button(self, text='Choose the picture', command=self.ImageGet)
        self.buttonSelImage.pack()
        self.lableShowImage = tk.Label(self)
        self.lableShowImage.pack()
        self.mainloop()

    def ImageGet(self):
        imagepath = tkinter.filedialog.askopenfilename()
        self.path.set(imagepath)
        PATH = self.entry.get()
        pictest = PicGet(PATH)
        width = PicGetWidth(pictest)
        height = PicGetHeight(pictest)
        Graph_Simple_Cut(PATH)
        x = Image.open("Graph1.png")
        img = ImageTk.PhotoImage(x.resize((int(width / (height / 200)), 200)))
        self.lableShowImage.config(image=img)
        self.lableShowImage.image = img


def Graph1_GUI_Init(root):

    root.title("Using the Edge-feature to cut the picture which gain the border")
    root.geometry("500x270+100+100")
    GUI_Init(root)
