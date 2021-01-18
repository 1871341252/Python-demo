# from utils.out_time import Outtime

# time=Outtime()
# now_time=time.get_current_time()
# print(now_time)

import tkinter

def goPush():
    win2=tkinter.Toplevel()
    win2.geometry('400x50')
    tkinter.Label(win2,text="If you have prepared as Help describes select Go otherwise select Go Back").pack()
    tkinter.Button(win2,text="Go",command=bounceProg).pack(side=tkinter.RIGHT,padx=5)
    tkinter.Button(win2, text="Go Back", command=win2.destroy).pack(side=tkinter.RIGHT)

def bounceProg():
    d=1
    print(d)
root=tkinter.Tk()
root.geometry('500x100')
tkinter.Button(text='Go', command=goPush).pack(side=tkinter.RIGHT,ipadx=50)
root.mainloop()
