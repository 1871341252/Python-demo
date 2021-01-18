import random

list1=[]
N=10
while len(list1)<N :
    i=random.randint(0,100)
    list1.append(i)
print ('排列之前：',list1)
for i in range(N - 1):
    min = i
    for j in range(i + 1,N):
        if list1[min] > list1[j]:min = j
    list1[i],list1[min] = list1[min],list1[i]
print ('排列之后：',list1)