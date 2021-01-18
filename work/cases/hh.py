print("测试成功!!!!")


list1=[]
n=1
while len(list1)<3:
    temp=input('请输入第{}个列表内容:'.format(n))
    list1.append(temp)
    n+=1
else:
    print("列表的内容已满！！！")
list3=list(set(list1))
#print(list3)
list3.sort(reverse=True) #倒序  reverse反向
print(list3)