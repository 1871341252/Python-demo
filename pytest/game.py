import random
class Game:
    def __init__(self):
        pass
    def game1(self):
        print("猜大小游戏开始咯！")
        a=random.randint(0,100)
        print("请您输入一个不大于100的正数！")
        num=0
        while True :
            num += 1
            b=int(input())
            if b<a :
                print("您猜的数太小了，再试试吧！")
            elif b>a:
                print("您猜的数太大了，再试试吧！")
            else:
                print("恭喜您猜对了！！！")
#                print("本轮幸运数字为："+str(a))
                print('本轮您猜了{}次'.format(num))
                print('本轮幸运数字为：{}'.format(a))
                exit()
    def game2(self):
        count=-1
        while True :
            count= count+1
            judge1='exit'
            judge=input()
            jige=0
            bujige=0
            error=0
            if judge == judge1 :
                print('您输入了{}个学生的成绩,及格的有{}个,不及格的有{}个,错误的有{}个'.format(count,jige,bujige,error))
                break
            else:
                print("请输入学生成绩：")
                result=int(input())
                if result>100 :
                    print("请输入正确的成绩！！！")
                    error=error+1
                elif 90<=result<=100 :
                    print("该学生的成绩为A级！")
                    jige+=1
                elif 80<=result<90 :
                    print("该学生的成绩为B级！")
                    jige+=1
                elif 70<=result<80 :
                    print("该学生的成绩为C级！")
                    jige+=1
                elif 60<=result<70 :
                    print("该学生的成绩为D级！")
                    jige+=1
                elif 0<=result<60 :
                    print("该学生的成绩不及格！")
                    bujige+=1
                else:
                    print("请输入正确的成绩！！！")
                    error=error+1
g=Game()
#g.game2()


count=-1
while True :
    count= count+1
    judge1='exit'
    judge=input()
    if judge != judge1 :
        jige=0
        bujige=0
        error=0
        print("请输入学生成绩：")
        result=int(input())
        if result>100 :
            print("请输入正确的成绩！！！")
            error=error+1
        elif 90<=result<=100 :
            print("该学生的成绩为A级！")
            jige=jige+1
        elif 80<=result<90 :
            print("该学生的成绩为B级！")
            jige=jige+1
        elif 70<=result<80 :
            print("该学生的成绩为C级！")
            jige=jige+1
        elif 60<=result<70 :
            print("该学生的成绩为D级！")
            jige=jige+1
        elif 0<=result<60 :
            print("该学生的成绩不及格！")
            bujige=bujige + 1
        else:
            print("请输入正确的成绩！！！")
            error=error+1
    else:
        print('您输入了{}个学生的成绩,及格的有{}个,不及格的有{}个,错误的有{}个'.format(count,jige,bujige,error))
        break