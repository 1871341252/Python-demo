'''
打印九九乘法表
'''

for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print(" ")

'''
num=0
for i in range(1,201):
    num=num+i
print('结果为:{}'.format(num))

j=1
res=1
while res:
    print('请输入{}个数字！'.format(j))
    y=int(input())
    square=y*y
    j+=1
    if square<50:
        res=False
        print('计算结果为：{}'.format(square))
    else:
        res=True
        print('计算结果为：{}'.format(square))
'''