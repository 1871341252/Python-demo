import xlrd
import time
import pymysql
from faker import Faker

class Createdata:
#    def __init__(self):
#        pass
# 连接数据库
    def open_excel(self):
        try:
            book = xlrd.open_workbook("./data/testdata.xls")  #文件名，把文件与py文件放在同一目录下
        except:
            print("open excel file failed!")
        try:
            sheet = book.sheet_by_name("Sheet1")   #execl里面的worksheet1
            return sheet
        except:
            print("locate worksheet in excel failed!")
    
    
    def insert_deta(self):
        sheet = self.open_excel()
        db = pymysql.connect(host="122.51.240.136", user="root",
                            passwd="123456",
                            db="testdata",
                            charset='utf8')
        cursor =db.cursor()
        row_num = sheet.nrows
        for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
            row_data = sheet.row_values(i)
            value = (row_data[1],row_data[2],row_data[3])
            print(i)
            sql = "INSERT INTO data(user,password,age)VALUES(%s,%s,%s)"
            cursor.execute(sql, value)  # 执行sql语句
            time.sleep(1)
            db.commit()
            print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        cursor.close()  # 关闭连接
    
run=Createdata()
run.open_excel()
run.insert_deta()
#open_excel()
#insert_deta()
'''
f=Faker('zh_CN')
for i in range(10):
    print(f.name()+'\t'+f.company())
'''