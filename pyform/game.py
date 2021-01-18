import random
class Game:
    def __init__(self):
        pass
    def game1(self):
        print("猜大小游戏开始咯！")
        a=random.randint(0,100)
        print("请您输入一个不大于100的正数！")
        num=0
        while True :
            num += 1
            b=int(input())
            if b<a :
                print("您猜的数太小了，再试试吧！")
            elif b>a:
                print("您猜的数太大了，再试试吧！")
            else:
                print("恭喜您猜对了！！！")
#                print("本轮幸运数字为："+str(a))
                print('本轮您猜了{}次'.format(num))
                print('本轮幸运数字为：{}'.format(a))
                exit()
# game=Game()
# game.game1()