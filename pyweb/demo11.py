class Employee:
    '所有员工的基类'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def ad(self):
        print(self.name)
        print(self.salary)
   
#   def displayCount(self):
#   print ("Total Employee %d"  % Employee.empCount)
 
    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)
 
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.ad()
emp2.ad()
print ("Total Employee %d" % Employee.empCount)
print(emp1.__dict__)

# Person=Employee("张山",2000)
# Person.ad()