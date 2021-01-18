import random

print("开始录入信息")
num=int(input("请输入参加的人数！"))
A={}
for i in range(num):
    preson=input("请输入名字:")
    gift=input("请输入礼物：")
    print('-'*50)
    A[preson]=gift
P1=list(A.keys())
G1=list(A.values())
m=0
B={}
while m<len(P1) :
    pre=P1[m]
    gift1 =B[pre]
    gift2 =random.choice(G1)
    if gift1 ==gift2 :
        B[pre]=gift2
        G1.remove(gift2)
    else:
        m -=1
    m+=1
print("礼物交换之前：",A)
print("礼物交换之后：",B)

