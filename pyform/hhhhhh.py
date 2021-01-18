import tkinter
from tkinter import Label,Button,END,Entry,Tk,Image
from PIL import Image,ImageTk
from utils.tools import Db
import tkinter as tk

db=Db("192.168.30.248",3306,"root","123456","test")

class myWindow():
    #定义构造函数，绘制窗体及控件
    def __init__(self,parent):
        self.root = parent
        self.root.title('登录')
        # self.master=master
        # self.master.wm_title('登录')
        # self.master.geometry('300x200')
        self.root.geometry('400x400')        
        self.createWidgets() 
        self.frame = tk.Frame(parent)
        self.canvas_root=tkinter.Canvas(self.root,width=400,height=400)
        self.im_root=self.get_image('bg.gif',400,400)
        self.canvas_root.create_image(400,400,image=self.im_root)
        self.canvas_root.pack()
        # self.frame.pack() 
        
    #定义绘制控件函数
    def createWidgets(self): 
        global entry_name
        global entry_pwd
        label=Label(self.root)
        label['text']='用户名'
        label['font']=14
        label.grid(row=0,column=0)
        entry_name=Entry(self.root)
        entry_name.grid(row=0,column=1)
        label=Label(self.root)
        label['text']='用户密码'
        label['font']=14
        label.grid(row=1,column=0) 
        entry_pwd=Entry(self.root)
        entry_pwd.grid(row=1,column=1)        
        btn_log=Button(self.root)
        btn_log['text']='登录'
        btn_log['font']=14
        btn_log['fg']='yellow'
        btn_log['bg']='green'
        btn_log['padx']=15
        btn_log['command']=self.toLogin
        btn_log.grid(row=2,column=0)
        btn_reset=Button(self.root)
        btn_reset['text']='重置'
        btn_reset['font']=14
        btn_reset['padx']=15
        btn_reset['fg']='white'
        btn_reset['bg']='green'
        btn_reset['command']=self.toReset
        # btn_reset.grid(row=2,column=1)
        btn_reset.grid(row=2,column=1)
        
        
        
    #定义点击按钮回调函数  
    def toLogin(self):
        name=entry_name.get()    #获取文本输入框的get方法
        pwd=entry_pwd.get()
        try:
            pwd1=db.query("select password from test_user where name =%s",(name))
            res=pwd1[0][0]
            # print(res)
            if pwd==res:
                print("恭喜您登录成功！！！")
                label=Label(self.root)
                label['text']='用户名'
                label['font']=20
                label.grid(row=0,column=0)
                handler = lambda: self.onCloseOtherFrame(Label)
                btn = tk.Button(label, text="重新登录", command=handler)
                btn.pack()
            else:
                print("密码错误，请重试！！！")
        except Exception as e:
            print('您输入的账号或密码错误:{}'.format(e))
    def toReset(self):
        entry_name.delete(0,END)  #清空输入框内容使用delete方法
        entry_pwd.delete(0,END)

    def onCloseOtherFrame(self, Label):
        """"""
        Label.destroy()
        self.show()

    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

    def get_image(self,filename,width,height):
        im=Image.open(filename).size(width,height)
        return ImageTk.PhotoImage(im)

    # def loginsucces(self):
    #     label=Label(self.root)
    #     label['text']='用户名'
    #     label['font']=20
    #     label.grid(row=0,column=0)

#实例化一个窗体及控件组合      
# root=Tk()      
# UserLogWindow=myWindow(root)
# root.mainloop() 
if __name__ == "__main__":
    root = tk.Tk()
    app = myWindow(root)
    root.mainloop()

