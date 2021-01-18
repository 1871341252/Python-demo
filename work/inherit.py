class Student:
    #父类
    # name=''
    # age=0
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def students(self):
        print('我叫{}，今年{}岁'.format(self.name,self.age))

class Preson(Student):
    #继承父类
    # speak=''
    def __init__(self,n,a,s):
        Student.__init__(self,n,a)
        self.speak=s

    def presons(self):
        #重写父类的方法
        print('我叫{}，今年{}岁,我要说的是:{}'.format(self.name,self.age,self.speak))

run=Preson('zhangshan',20,'Python继承')
run.students()
run.presons()
