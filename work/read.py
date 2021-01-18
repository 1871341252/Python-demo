# f=open("C://work//data//read.txt","r",encoding='UTF-8')#读取文件
# str=f.readline()
# print(str)

# f=open("C://work//data//read.txt","w",encoding='UTF-8')#写入文件
# str=f.write(" 用在树上的生活方式体现个体的超越性，保持婞直却又不拘泥于所谓“遗世独立”的单向度形象。这便是卡尔维诺为我们提供的理想期望范式。生活在树上——始终热爱大地——升上天空。")


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # for j in range(0,n):
        #     if arr[j-1]>arr[j] :
        #         arr[j-1],arr[j]=arr[j],arr[j-1]

arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print('排序后的数组:{}'.format(arr))
for i in range(len(arr)):
    print("%d" % arr[i])
