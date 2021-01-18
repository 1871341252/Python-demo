import tkinter
from tkinter import Label,Button,END,Entry,Tk
from utils.tools import Db
import tkinter as tk

db=Db("192.168.30.248",3306,"root","123456","test")

class myWindow():
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title('登录')
        self.hide() 
        self.frame = tk.Frame(parent)
        # self.frame.pack()

    def hide(self):
        """主窗体布局"""
        global entry_name
        global entry_pwd
        label=tk.Label(self.root)
        label['text']='用户名'
        label['font']=14
        label.grid(row=0,column=0)
        entry_name=tk.Entry(self.root)
        entry_name.grid(row=0,column=1)
        label=tk.Label(self.root)
        label['text']='用户密码'
        label['font']=14
        label.grid(row=1,column=0) 
        entry_pwd=tk.Entry(self.root)
        entry_pwd.grid(row=1,column=1)        
        btn_log=tk.Button(self.root)
        btn_log['text']='登录'
        btn_log['font']=14
        btn_log['fg']='yellow'
        btn_log['bg']='green'
        btn_log['padx']=15
        btn_log['command']=self.toLogin
        btn_log.grid(row=2,column=0)
        btn_reset=tk.Button(self.root)
        btn_reset['text']='重置'
        btn_reset['font']=14
        btn_reset['padx']=15
        btn_reset['fg']='white'
        btn_reset['bg']='green'
        btn_reset['command']=self.toReset
        btn_reset.grid(row=2,column=1)
        # self.root.withdraw()

    def toLogin(self):
        name=entry_name.get()    #获取文本输入框的get方法
        pwd=entry_pwd.get()
        try:
            pwd1=db.query("select password from test_user where name =%s",(name))
            res=pwd1[0][0]
            # print(res)
            if pwd==res:
                print("恭喜您登录成功！！！")
                loginsucces = tk.Toplevel()
                loginsucces.geometry("220x120")
                loginsucces.title("登录成功")
                Label(loginsucces,text = '恭喜您登录成功！！！').pack()
                handler = lambda: self.onCloseOtherFrame(loginsucces)
                btn = tk.Button(loginsucces, text="重新登录", command=handler)
                btn.pack()
            else:
                passwordfial=tk.Toplevel()
                passwordfial.geometry("220x120")
                passwordfial.title("密码错误")
                Label(passwordfial,text = '密码错误').pack()
                print("密码错误，请重试！！！")
        except Exception as e:
            usernamefial=tk.Toplevel()
            usernamefial.geometry("220x120")
            usernamefial.title("账号错误")
            Label(usernamefial,text = '您输入的账号不存在').pack()
            print('您输入的账号不存在:{}'.format(e))
    def toReset(self):
        entry_name.delete(0,END)  #清空输入框内容使用delete方法
        entry_pwd.delete(0,END)

    def onCloseOtherFrame(self,loginsucces):
        """"""
        loginsucces.destroy()
        self.show()

    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("200x120")
    app = myWindow(root)
    root.mainloop()