import tkinter
# from tkinter import *
from tkinter import Label,Button,END,Entry,Tk
from tools.tools import Db
from tools.loginsucess import *

db=Db("192.168.30.248",3306,"root","123456","test")

class myWindow():
    #定义构造函数，绘制窗体及控件
    def __init__(self,master=None):
        self.master=master
        self.master.wm_title('登录')
        # self.master.geometry('300x200')
        self.master.geometry('230x100')        
        self.createWidgets()  
        
    #定义绘制控件函数
    def createWidgets(self): 
        global entry_name
        global entry_pwd
        label=Label(self.master)
        label['text']='用户名'
        label['font']=14
        label.grid(row=0,column=0)
        entry_name=Entry(self.master)
        entry_name.grid(row=0,column=1)
        label=Label(self.master)
        label['text']='用户密码'
        label['font']=14
        label.grid(row=1,column=0) 
        entry_pwd=Entry(self.master)
        entry_pwd.grid(row=1,column=1)        
        btn_log=Button(self.master)
        btn_log['text']='登录'
        btn_log['font']=14
        btn_log['fg']='yellow'
        btn_log['bg']='green'
        btn_log['padx']=15
        btn_log['command']=self.toLogin
        btn_log.grid(row=2,column=0)
        btn_reset=Button(self.master)
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
            else:
                print("密码错误，请重试！！！")
        except Exception as e:
            print('您输入的账号或密码错误:{}'.format(e))
    def toReset(self):
        entry_name.delete(0,END)  #清空输入框内容使用delete方法
        entry_pwd.delete(0,END)


    # def load_main(self):
    #     # 关闭当前窗体
    #     self.destroy()
    #     # 加载新窗体
    #     if __name__ == '__main__':
    #         main_window = loginsucces.MainWindow()


    def loginsucces(self):
        label=Label(self.master)
        label['text']='用户名'
        label['font']=20
        label.grid(row=0,column=0)

#实例化一个窗体及控件组合      
root=Tk()      
UserLogWindow=myWindow(root)
root.mainloop() 
# form=tkinter.Tk()

# form.title("Python窗体")
# form.geometry('800x600')

# form.mainloop()
