'''
输入某年某月某日，判断这一天是这一年的第几天？
'''

class Year:
#    def __init__(self):
#        pass
    def judgedate(self):
        year=int(input("年:"))
        mouth=int(input("月:"))
        day=int (input("天："))

        mouths=(0,31,59,90,120,151,181,212,243,273,304,334)
        if 0<mouth<12:
            sum=mouths[mouth-1]
        else:
            print("输入的月份不正确！！！")
        sum+=day
        leap=0
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            leap=1
        if (leap==1)and(mouth>2):
            sum+=1
        print('您输入的日期是{}的第:{}天'.format(year,sum))
#run=Year()
#run.judgedate()