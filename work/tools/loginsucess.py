import tkinter
# from tkinter import *
from tkinter import Label,Button,END,Entry,Tk
from tools.tools import Db

class myWindow1():
    #定义构造函数，绘制窗体及控件
    def __init__(self,master=None):
        self.master=master
        self.master.wm_title('登录成功')
        # self.master.geometry('300x200')
        self.master.geometry('230x100')        
        self.createWidgets()  

    def loginsucces(self):
        label=Label(self.master)
        label['text']='登录成功'
        label['font']=20
        label.grid(row=0,column=0)