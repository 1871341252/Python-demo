import random
import xlrd

def randomlist():
    list1=[]
    list2=[0]
    while len(list1)<10 :
        i=random.randint(0,100)
        list1.append(i)
        list1.sort()
    print(list1)
    print(list1+list2)
    list1.extend(list2)
    print(list1)
    for i in range(len(list1)):
        print(list1[i])
    #w=open("list.txt","a")
    #w.writelines(list1)
    #w.write("\n")
    #w.close()
def test():
    randomlist()
test()
