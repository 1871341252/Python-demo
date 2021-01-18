import pymysql
'''
print("hello word")
'''
for i in range(1,10):
    print(i)
r=open("user.txt","r+")
res=r.read()
print(res)
r.close()

try:
    db = pymysql.connect(host="122.51.240.136", user="root",
                         passwd="123456",
                         db="testdata",
                         charset='utf8')
except:
    print("could not connect to mysql server")
try:
    cursor = db.cursor()
    cursor.execute("delete from data where 0<user<50;")
    db.commit()
except:
    print("sql语句出现错误！")