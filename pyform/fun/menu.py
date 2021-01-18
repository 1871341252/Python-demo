import tkinter
from tkinter import Label,Button,END,Entry,Tk,PhotoImage,Menu
from PIL import Image,ImageTk
from utils.tools import Db
import tkinter as tk

class UserMenu:
    def __init__(self):
        pass
    # def showImg(self,loginsucces):
    #     load=Image.open("bg.gif")
    #     render=ImageTk.PhotoImage(load)
    #     img=Label(loginsucces,image=render)
    #     img.image=render
    #     img.place(x=0,y=0)

    def exit(self):
        exit()

    def quit1(self,arge):
        arge.destroy