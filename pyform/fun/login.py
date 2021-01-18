import tkinter
from tkinter import Label,Button,END,Entry,Tk
import tkinter as tk
from utils.tools import Db

db=Db("192.168.30.248",3306,"root","123456","test")

# class Login:
#     def __init__(self):
#         self.root = parent
#         self.frame = tk.Frame(parent)
#     def toLogin(self,entry_name,entry_pwd):
#         """登录窗体页面"""
#         name=entry_name.get()    #获取文本输入框的get方法
#         pwd=entry_pwd.get()
#         try:
#             pwd1=db.query("select password from test_user where name =%s",(name))
#             res=pwd1[0][0]
#             # print(res)
#             if pwd==res:
#                 print("恭喜您登录成功！！！")
#                 loginsucces = tk.Toplevel()
#                 loginsucces.geometry("220x120")
#                 loginsucces.title("登录成功")
#                 userinfo=db.query("select * from test_user where name =%s",(name))
#                 print(userinfo)
#                 user_list=[]
#                 for i in userinfo:
#                     for j in i:
#                         print(j)
#                         user_list.append(j)
#                 Label(loginsucces,text = user_list).pack()
#                 handler = lambda: self.onCloseLoginFrame(loginsucces)
#                 btn = tk.Button(loginsucces, text="重新登录", command=handler)
#                 btn.pack()
#             else:
#                 loginfial=tk.Toplevel()
#                 loginfial.geometry("220x120")
#                 loginfial.title("密码错误")
#                 Label(loginfial,text = '密码错误').pack()
#                 print("密码错误，请重试！！！")
#         except Exception as e:
#             loginfial1=tk.Toplevel()
#             loginfial1.geometry("220x120")
#             loginfial1.title("密码错误")
#             Label(loginfial1,text = '您输入的账号或密码错误').pack()
#             print('您输入的账号或密码错误:{}'.format(e))
#     def onCloseLoginFrame(self,loginsucces):
#         """"""
#         loginsucces.destroy()
#         self.show()

#     def show(self):
#         """"""
#         self.root.update()
#         self.root.deiconify()