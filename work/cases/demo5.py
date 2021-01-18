'''
求1+2!+3!+...+20!的和。
'''
import xlrd 

n=0
t=1
num=0
for n in range(1,21):
    t *=n
    num +=t
print(num)

list=[]
n=1
while len(list)<10:
    temp=input('请输入第{}个列表内容:'.format(n))
    list.append(temp)
    n+=1
else:
    print("列表的内容已满！！！")
print(list)
list1=[str(i) for i in list]
list2='  '.join(list1)
w=open("./data/user.txt","a")
w.writelines(list2)
w.write("\n")
w.close()
r=open("./data/user.txt","r+")
res=r.read()
print(res)
r.close()

    