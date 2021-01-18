import unittest
import requests
from utils.tools import readexcle,createreport,Db

db=Db("192.168.50.11",3312,"root","szgr123","gre_study")
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")
host="http://test.geron-e.com"


class TestLogin(unittest.TestCase):
    def test_01_login(self):
        """登录接口测试"""
        # username='13429922055'
        # password='888888'
        # values={
        #     "username":"13429922055",
        #     "password":"888888"
        # }
        url = host + datalist[0][2]
        headers=eval(datalist[0][4])
        values=eval(datalist[0][5])
        print(values)
        res=requests.post(url,headers=headers,data=values)
        # resl=res.content.decode('utf-8')
        # print(resl)
        # resl=res.json()
        # print(resl)
        # sessionId=resl.get("data")
        # print(sessionId)
        self.assertEqual("ok",res.json().get("state"))
    
# run=TestLogin()
# run.test_01_login()

# if __name__ == "__main__":
#     username='13429922055'
#     password='888888'
#     test_01_login(username,password)

