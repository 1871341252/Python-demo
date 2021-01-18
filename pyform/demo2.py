import tkinter as tk
from tkinter import Label,Button,END,Entry,Tk

global res1
root=tk.Tk()
root.title("测试")
root.geometry('500x350+300+200')
Label(text="啊哈哈",bg='green',fg='red',width='10',height='5').place(x=100,y=100)
Button(text="退出测试",bg='green',fg='red',command=root.destroy).place(x=200,y=0)
res=tk.StringVar()
Entry(root,textvariable=res).place(x=0,y=0)
res1=Entry(root,textvariable=res)
root.mainloop()

