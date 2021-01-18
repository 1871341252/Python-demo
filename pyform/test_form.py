import tkinter
from tkinter import Label,Button,END,Entry,Tk,PhotoImage,Menu,Text
from PIL import Image,ImageTk
import os
import random
from utils.tools import Db
import tkinter as tk
from fun.menu import UserMenu
from utils.log import logging

menu1=UserMenu()
db=Db("192.168.30.248",3306,"root","123456","test")

class myWindow():
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title('登录')
        self.loginui() 
        self.frame = tk.Frame(parent)
        # self.frame.pack()

    def loginui(self):
        """主窗体页面"""
        global entry_name
        global entry_pwd
        label=tk.Label(self.root)
        label['text']='用户名'
        label['font']=14
        label.grid(row=0,column=0,padx=60,pady=50)
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
        # btn_log['fg']='yellow'
        btn_log['fg']='white'
        btn_log['bg']='green'
        btn_log['padx']=15
        btn_log['command']=self.toLogin
        # btn_log['command']=login.toLogin(entry_name,entry_pwd)
        btn_log.grid(row=2,column=0,padx=60,pady=50)
        btn_reset=tk.Button(self.root)
        btn_reset['text']='重置'
        btn_reset['font']=14
        btn_reset['padx']=15
        btn_reset['fg']='white'
        btn_reset['bg']='green'
        btn_reset['command']=self.toReset
        btn_reset.grid(row=2,column=1)
        btn_reset=tk.Button(self.root)
        btn_reset['text']='注册'
        btn_reset['font']=14
        btn_reset['padx']=15
        btn_reset['fg']='white'
        btn_reset['bg']='green'
        btn_reset['command']=self.regist
        btn_reset.grid(row=3,column=0)
        btn_reset=tk.Button(self.root)
        btn_reset['text']='修改密码'
        btn_reset['font']=14
        btn_reset['padx']=15
        btn_reset['fg']='white'
        btn_reset['bg']='green'
        btn_reset['command']=self.updateui
        btn_reset.grid(row=3,column=1)

    def toLogin(self):
        """登录窗体页面"""
        global number
        global number1
        global loginsucces
        name=entry_name.get()    #获取文本输入框的get方法
        pwd=entry_pwd.get()
        try:
            pwd1=db.query("select password from test_user where name =%s",(name))
            res=pwd1[0][0]
            # print(res)
            if pwd==res:
                print("恭喜您登录成功！！！")
                loginsucces = tk.Toplevel()
                loginsucces.geometry("600x600")
                loginsucces.title("登录成功")
                # menu1=UserMenu(loginsucces)
                menu=Menu(loginsucces)
                loginsucces.config(menu=menu)
                file1=Menu(menu)
                file1.add_command(label="Save")
                file1.add_command(label="Exit",command=menu1.exit)
                menu.add_cascade(label='File',menu=file1)

                edit=Menu(menu)
                edit.add_command(label="Undo")
                edit.add_command(label="Show Image",command=self.showImg)
                menu.add_cascade(label='Edit',menu=edit)

                user=Menu(menu)
                user.add_command(label="update",command=self.update_user_ui)
                
                # user.add_command(label="userinfo",command=self.show_userinfo)
                menu.add_cascade(label='User',menu=user)

                data_number=tk.StringVar()
                Entry(loginsucces,textvariable=data_number).grid(row=1,column=0)
                number1=Entry(loginsucces,textvariable=data_number)
                number=random.randint(0,100)
                print(number)
                Button(loginsucces, text="确定", command=self.game).grid(row=1,column=1)

                dataText=Text(loginsucces,width=67, height=60)
                dataText.grid(row=2, column=0)
                # dataText.pack()
                
            else:
                loginfial=tk.Toplevel()
                loginfial.geometry("220x120")
                loginfial.title("密码错误")
                Label(loginfial,text = '密码错误').pack()
                Button(loginfial, text="返回",command=loginfial.destroy).pack()
                print("密码错误，请重试！！！")
        except Exception as e:
            loginfial1=tk.Toplevel()
            loginfial1.geometry("220x120")
            loginfial1.title("密码错误")
            Label(loginfial1,text = '您输入的账号或密码错误').pack()
            Button(loginfial1, text="返回",command=loginfial1.destroy).pack()
            logging.info('您输入的账号或密码错误:{}'.format(e))
            # print('您输入的账号或密码错误:{}'.format(e))

    def updateui(self):
        """修改密码窗体页面"""
        global password_protection 
        global newpwd
        global name1
        name1=entry_name.get()
        # print(name1)
        try:
            # name3=db.query("select name from test_user where name =%s",(name1))
            # name_res=name3[0][0]
            # print(name_res)
            if name1 is '':
                updatefial=tk.Toplevel()
                updatefial.geometry("220x120")
                updatefial.title("错误提示")
                Label(updatefial,text = '用户名为空').pack()
                Button(updatefial, text="返回",command=updatefial.destroy).pack()
            else:
                name3=db.query("select name from test_user where name =%s",(name1))
                if name3 is ():
                    updatefial1=tk.Toplevel()
                    updatefial1.geometry("220x120")
                    updatefial1.title("错误提示")
                    Label(updatefial1,text = '用户名不存在').pack()
                    Button(updatefial1, text="返回",command=updatefial1.destroy).pack()
                else:
                    updatepwd=tk.Toplevel()
                    updatepwd.geometry("220x120")
                    updatepwd.title("修改密码")
                    Label(updatepwd,text = '密保').grid(row=1,column=0)
                    password_protection1=tk.StringVar()
                    Entry(updatepwd,textvariable=password_protection1).grid(row=1,column=1)
                    password_protection=Entry(updatepwd,textvariable=password_protection1)
                    Label(updatepwd,text = '新密码').grid(row=2,column=0)
                    new_password=tk.StringVar()
                    Entry(updatepwd,textvariable=new_password).grid(row=2,column=1)
                    newpwd=Entry(updatepwd,textvariable=new_password)
                    Button(updatepwd, text="确认修改", command=self.update).grid(row=3,column=0)
                    Button(updatepwd, text="返回",command=updatepwd.destroy).pack()
        except Exception as e:
            updatefial=tk.Toplevel()
            updatefial.geometry("220x120")
            updatefial.title("错误提示")
            Label(updatefial,text = '用户名为空').pack()
            Button(updatefial, text="返回",command=updatefial.destroy).pack()
            logging.info('用户名为空{}'.format(e))
            # print('用户名为空{}'.format(e))

    def update(self):
        """修改密码"""
        pw1=db.query("select passwords from test_user where name =%s",(name1))
        print(pw1)
        name_res=pw1[0][0]
        print(name_res)
        pw=password_protection.get()
        print(pw)
        np=newpwd.get()
        if password_protection is '':
            updatefial=tk.Toplevel()
            updatefial.geometry("220x120")
            updatefial.title("错误提示")
            Label(updatefial,text = '密保为空').pack()
            Button(updatefial, text="返回",command=updatefial.destroy).pack()
        else:
            if name_res==pw:
                # print(name_res)
                if np is '':
                    updatefial1=tk.Toplevel()
                    updatefial1.geometry("220x120")
                    updatefial1.title("错误提示")
                    Label(updatefial1,text = '新密码为空').pack()
                    Button(updatefial1, text="返回",command=updatefial1.destroy).pack()
                else:
                    value=(name1,np)
                    db.commit("UPDATE test_user SET password=%s WHERE name='%s'",(value))
                    updatesuccess=tk.Toplevel()
                    updatesuccess.geometry("220x120")
                    updatesuccess.title("密码修改成功")
                    Label(updatesuccess,text = '恭喜您！密码修改成功').pack()
                    handler = lambda: self.onCloseUpdateFrame(updatesuccess)
                    btn = tk.Button(updatesuccess, text="重新登录", command=handler)
                    btn.pack() 
                    Button(updatesuccess, text="返回",command=updatesuccess.destroy).pack()     
            else:
                updatefial=tk.Toplevel()
                updatefial.geometry("220x120")
                updatefial.title("错误提示")
                Label(updatefial,text = '密保错误,无法修改密码').pack() 
                Button(updatefial, text="返回",command=updatefial.destroy).pack()
    
    def toReset(self):
        """重置方法"""
        entry_name.delete(0,END)  #清空输入框内容使用delete方法
        entry_pwd.delete(0,END)
    
    def regist(self):
        """注册窗体页面"""
        try:
            name=entry_name.get()    #获取文本输入框的get方法
            pwd=entry_pwd.get()
            if name is '':
                insertnull=tk.Toplevel()
                insertnull.geometry("220x120")
                insertnull.title("注册失败")
                Label(insertnull,text = '用户名或密码为空').pack()
                Button(insertnull, text="返回",command=insertnull.destroy).pack()
            else:
                name2=db.query("select name from test_user where name =%s",(name))
                # print(name2)
                if name2 is ():
                    # name_res=name2[0][0]
                    # print(name)
                    # print(pwd)
                    # print(name_res)
                    if pwd is '':
                        insertnull=tk.Toplevel()
                        insertnull.geometry("220x120")
                        insertnull.title("注册失败")
                        Label(insertnull,text = '密码为空').pack()
                        Button(insertnull, text="返回",command=insertnull.destroy).pack()
                        print("密码为空")
                    else:
                        value=(name,pwd)
                        db.commit("INSERT INTO test_user ( NAME, PASSWORD ) VALUES(%s,%s)",value)
                        insertsucces=tk.Toplevel()
                        insertsucces.geometry("220x120")
                        insertsucces.title("注册成功")
                        Label(insertsucces,text = '恭喜您注册成功').pack()
                        print("恭喜您注册成功")
                        handler = lambda: self.onCloseRegisterFrame(insertsucces)
                        btn = tk.Button(insertsucces, text="登录", command=handler)
                        btn.pack()
                        Button(insertsucces, text="返回",command=insertsucces.destroy).pack()
                else:
                    inserts=tk.Toplevel()
                    inserts.geometry("220x120")
                    inserts.title("注册失败")
                    Label(inserts,text = '用户已注册').pack()
                    Button(inserts, text="返回",command=inserts.destroy).pack()
                    print("用户已注册")

        except Exception as e:
            insertnull=tk.Toplevel()
            insertnull.geometry("220x120")
            insertnull.title("注册失败")
            Label(insertnull,text = '用户名或密码为空').pack()
            Button(insertnull, text="返回",command=insertnull.destroy).pack()
            logging.info('用户名或密码为空{}'.format(e))
            # print('用户名或密码为空{}'.format(e))

    def update_user_ui(self):
        """修改个人资料界面"""
        global user_password
        global username
        global sex
        global age
        global phone
        global pwd3
        update_user_ui1=tk.Toplevel()
        update_user_ui1.geometry("300x350")
        update_user_ui1.title("修改个人资料")
        Label(update_user_ui1,text = '用户名').grid(row=1,column=0,padx=10,pady=10)
        name2=tk.StringVar()
        Entry(update_user_ui1,textvariable=name2).grid(row=1,column=1)
        username=Entry(update_user_ui1,textvariable=name2)
        Label(update_user_ui1,text = '密码').grid(row=2,column=0,padx=10,pady=10)
        password=tk.StringVar()
        Entry(update_user_ui1,textvariable=password).grid(row=2,column=1)
        user_password=Entry(update_user_ui1,textvariable=password)
        Label(update_user_ui1,text = '性别').grid(row=3,column=0,padx=10,pady=10)
        sex1=tk.StringVar()
        Entry(update_user_ui1,textvariable=sex1).grid(row=3,column=1)
        sex=Entry(update_user_ui1,textvariable=sex1)
        Label(update_user_ui1,text = '年龄').grid(row=4,column=0,padx=10,pady=10)
        age1=tk.StringVar()
        Entry(update_user_ui1,textvariable=age1).grid(row=4,column=1)
        age=Entry(update_user_ui1,textvariable=age1)
        Label(update_user_ui1,text = '电话号码').grid(row=5,column=0,padx=10,pady=10)
        phone1=tk.StringVar()
        Entry(update_user_ui1,textvariable=phone1).grid(row=5,column=1)
        phone=Entry(update_user_ui1,textvariable=phone1)
        Label(update_user_ui1,text = '密保').grid(row=6,column=0,padx=10,pady=10)
        pwd2=tk.StringVar()
        Entry(update_user_ui1,textvariable=pwd2).grid(row=6,column=1)
        pwd3=Entry(update_user_ui1,textvariable=pwd2)
        Button(update_user_ui1, text="确认修改", command=self.update_user).grid(row=7,column=0,padx=10,pady=35)
        Button(update_user_ui1, text="个人信息", command=self.show_userinfo).grid(row=7,column=1,padx=10,pady=35)
        Button(update_user_ui1, text="取消修改", command=update_user_ui1.destroy).grid(row=7,column=2,padx=10,pady=35)

    def update_user(self):
        """修改个人信息"""
        user_name=username.get()
        user_password1=user_password.get()
        res1=sex.get()
        res2=age.get()
        res3=phone.get()
        res4=pwd3.get()
        # print(res1)
        # print(res2)
        # print(res3)
        # print(res)
        try:
            if user_name is '' or user_password1 is '':
                update_user_fial=tk.Toplevel()
                update_user_fial.geometry("220x120")
                update_user_fial.title("错误提示")
                Label(update_user_fial,text = '用户名或密码为空').pack()
                Button(update_user_fial, text="返回",command=update_user_fial.destroy).pack()
            else:
                name4=db.query("select name from test_user where name =%s",(user_name))
                if name4 is ():
                    update_user_fial1=tk.Toplevel()
                    update_user_fial1.geometry("220x120")
                    update_user_fial1.title("错误提示")
                    Label(update_user_fial1,text = '用户名不存在').pack()
                    Button(update_user_fial1, text="返回",command=update_user_fial1.destroy).pack()
                else:
                    password3=db.query("select password from test_user where name =%s",(user_name)) 
                    res=password3[0][0]
                    if user_password1==res:
                        db.commit("UPDATE test_user SET sex=%s,age=%s,phone=%s,passwords=%s WHERE name=%s",(res1,res2,res3,res4,user_name))
                        update_user_success=tk.Toplevel()
                        update_user_success.geometry("220x120")
                        update_user_success.title("修改个人信息")
                        Label(update_user_success,text = '修改个人信息成功').pack()
                        Button(update_user_success, text="返回",command=update_user_success.destroy).pack()
                        print("修改个人信息成功")    
                    else:
                        update_user_fial4=tk.Toplevel()
                        update_user_fial4.geometry("220x120")
                        update_user_fial4.title("错误提示")
                        Label(update_user_fial4,text = '密码错误').pack()
                        Button(update_user_fial4, text="返回",command=update_user_fial4.destroy).pack()
        except Exception as e:
            updatefial=tk.Toplevel()
            updatefial.geometry("220x120")
            updatefial.title("错误提示")
            Label(updatefial,text = '用户名为空').pack()
            Button(updatefial, text="返回",command=updatefial.destroy).pack()
            logging.info('用户名为空{}'.format(e))
            # print('用户名为空{}'.format(e))

    def show_userinfo(self):
        """查看个人信息"""
        username4=username.get()
        password4=user_password.get()
        try:
            if username4 is '' or password4 is '':
                update_user_fial=tk.Toplevel()
                update_user_fial.geometry("220x120")
                update_user_fial.title("错误提示")
                Label(update_user_fial,text = '用户名或密码为空').pack()
                Button(update_user_fial, text="返回",command=update_user_fial.destroy).pack()
            else:
                name4=db.query("select name from test_user where name =%s",(username4))
                if name4 is ():
                    update_user_fial1=tk.Toplevel()
                    update_user_fial1.geometry("220x120")
                    update_user_fial1.title("错误提示")
                    Label(update_user_fial1,text = '用户名不存在').pack()
                    Button(update_user_fial1, text="返回",command=update_user_fial1.destroy).pack()
                else:
                    password3=db.query("select password from test_user where name =%s",(username4)) 
                    res=password3[0][0]
                    if password4==res:
                        userinfo=db.query("select * from test_user where name =%s",(username4))
                        userinfolist=[] 
                        for i in userinfo:
                            userinfolist.append(i)
                            # print(userinfolist)
                        update_user_success=tk.Toplevel()
                        update_user_success.geometry("220x120")
                        update_user_success.title("个人信息")
                        Label(update_user_success,text = '用户名：{}'.format(userinfolist[0][2])).pack()
                        Label(update_user_success,text = '密码：{}'.format(userinfolist[0][3])).pack()
                        Label(update_user_success,text = '性别：{}'.format(userinfolist[0][4])).pack() 
                        Label(update_user_success,text = '年龄：{}'.format(userinfolist[0][5])).pack()
                        Label(update_user_success,text = '手机号：{}'.format(userinfolist[0][6])).pack()      
                    else:
                        update_user_fial4=tk.Toplevel()
                        update_user_fial4.geometry("220x120")
                        update_user_fial4.title("错误提示")
                        Label(update_user_fial4,text = '密码错误').pack()
                        Button(update_user_fial4, text="返回",command=update_user_fial4.destroy).pack()
        except Exception as e:
            updatefial=tk.Toplevel()
            updatefial.geometry("220x120")
            updatefial.title("错误提示")
            Label(updatefial,text = '用户名为空').pack()
            logging.info('用户名为空{}'.format(e))
            # print('用户名为空{}'.format(e))
        

    def onCloseLoginFrame(self,loginsucces):
        """"""
        loginsucces.destroy()
        self.show()

    def onCloseUpdateFrame(self,updatesuccess):
        """"""
        updatesuccess.destroy()
        self.show()

    def onCloseRegisterFrame(self,insertsucces):
        """"""
        insertsucces.destroy()
        self.show()

    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

    def showImg(self):
        """图片展示"""
        global show_img
        global ImageTk
        show_img=tk.Toplevel()
        show_img.geometry("1300x700")
        show_img.title("图片展示")
        load=Image.open("bg.gif")
        render=ImageTk.PhotoImage(load)
        img=Label(show_img,image=render)
        img.image=render
        img.place(x=0,y=0)
    
    def game(self):
        """猜数字游戏"""
        data=number1.get()
        try:
            number3=int(data)
            if number>number3:
                number_small=tk.Toplevel()
                number_small.geometry("220x120")
                number_small.title("错误提示")
                Label(number_small,text = '您猜的数字小了哟').pack()
                Button(number_small, text="返回",command=number_small.destroy).pack()
            elif number<number3:
                number_largr=tk.Toplevel()
                number_largr.geometry("220x120")
                number_largr.title("错误提示")
                Label(number_largr,text = '您猜的数字大了哟').pack()
                Button(number_largr, text="返回",command=number_largr.destroy).pack()
            else:
                number_success=tk.Toplevel()
                number_success.geometry("220x120")
                number_success.title("错误提示")
                Label(number_success,text = '恭喜您猜对了哟').pack()
                Button(number_success, text="返回",command=number_success.destroy).pack()
        except Exception as e:
            number_fial=tk.Toplevel()
            number_fial.geometry("220x120")
            number_fial.title("错误提示")
            Label(number_fial,text = '请输入数字').pack()
            Button(number_fial, text="返回",command=number_fial.destroy).pack()
            logging.info('请输入数字:{}'.format(e))
            print('请输入数字:{}'.format(e))     

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = myWindow(root)
    root.mainloop()