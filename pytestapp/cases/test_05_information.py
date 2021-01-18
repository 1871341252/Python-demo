import unittest
import requests
from utils.tools import readexcle,createreport,Db

db=Db("192.168.50.11",3312,"root","szgr123","gre_study")
datalist=  readexcle("./data/个人中心接口测试用例.xlsx","Cases")
host="http://192.168.50.11"

class TestExam(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requests=requests.Session()
        url ="http://test.geron-e.com:8095/api/app/login"
        headers= eval(datalist[0][4])
        values= eval(datalist[0][5])
        res=cls.requests.post(url,headers=headers,data=values)
        resl=res.json()
        cls.token=resl.get("data")
        print(resl.get("data"))

    @classmethod
    def tearDownClass(cls):
        print("测试结束！")
    
    def test_01_getBaseInfo(self):
        """个人中心接口测试"""
        url=host + datalist[1][2]
        headers= eval(datalist[1][4])
        headers.update(sessionId=self.token)
        res=requests.get(url,headers=headers)
        # print(res.json())
        self.assertEqual("ok",res.json().get("state"))

    def test_02_getExtInfo(self):
        """扩展信息接口测试"""
        url=host + datalist[2][2]
        headers= eval(datalist[2][4])
        headers.update(sessionId=self.token)
        res=requests.get(url,headers=headers)
        # print(res.json())
        self.assertEqual("ok",res.json().get("state"))

    def test_03_hand(self):
        """修改密码接口测试"""
        url=host + datalist[3][2]
        headers= eval(datalist[3][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[3][5])
        res=requests.post(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))
