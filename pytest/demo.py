count=1
while True :
    count= count+1
    judge1='exit'
    judge=input()
    if judge == judge1 :
        break
    else:
        print("请输入学生成绩：")
        result=int(input())
        if result>100 :
            print("请输入正确的成绩！！！")
        elif 90<=result<=100 :
            print("该学生的成绩为A级！")
        elif 80<=result<90 :
            print("该学生的成绩为B级！")
        elif 70<=result<80 :
            print("该学生的成绩为C级！")
        elif 60<=result<70 :
            print("该学生的成绩为D级！")
        elif 0<=result<60 :
            print("该学生的成绩不及格！")
        else:
            print("请输入正确的成绩！！！")