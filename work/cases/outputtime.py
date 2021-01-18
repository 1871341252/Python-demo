'''
暂停一秒输出，并格式化当前时间。 
'''
import time
import random

class Time:
    def __init__(self,m,n):
        self.m=m
        self.n=n
    def testtime(self):
        s=random.randint(self.m,self.n)
        print(s)
        t=0
        while t<s:
            print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

            time.sleep(1)

            print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

            time.sleep(1)

            t+=1
#run=Time(0,100)
#run.testtime()