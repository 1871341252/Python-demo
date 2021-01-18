'''
列表的合并,去重及排序
'''
import time

list1=[1,2,3,4,7,9,8]
list2=[3,4,5,6,10,11]
list1.extend(list2) #合并
print(list1)
#list2.sort(key=list2.index)
#print(list1)
list3=list(set(list1))  #去重并排序
print(list3)
list3.sort() #正序
print(list3)
list3.sort(reverse=True) #倒序  reverse反向
print(list3)

for i in list3:
    #time.sleep(1)
    print(i)

a=0
num=0
while a<100 :
    a+=1
    num=num+a
print(num)

'''
def loop_merge_sort(l1, l2):
    tem = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tem.append(l1[0])
            del l1[0]
        else:
            tem.append(l2[0]),
            del l2[0]
    return tem
'''
l1 = [1,3,5,9,8,2,68,12,35]
l2 = [5,6,8,7,2,65,12,45,36]
#listed = loop_merge_sort(l1, l2)
#print(listed)
l1.extend(l2)
print(l1)