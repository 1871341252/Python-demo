import unittest
import requests
from utils.tools import readexcle,createreport,Db

db=Db("192.168.50.11",3312,"root","szgr123","gre_study")
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")
host="http://test.geron-e.com"

class TestExam(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requests=requests.Session()
        url = host + datalist[0][2]
        headers= eval(datalist[0][4])
        values= eval(datalist[0][5])
        res=cls.requests.post(url,headers=headers,data=values)
        resl=res.json()
        cls.token=resl.get("data")
        print(resl.get("data"))

    @classmethod
    def tearDownClass(cls):
        print("测试结束！")
    
    def test_01_findUnfinishedList(self):
        """未考考试列表接口测试"""
        global g_batchId
        url=host + datalist[11][2]
        headers= eval(datalist[11][4])
        headers.update(sessionId=self.token)
        # values=eval(datalist[11][5])
        res=requests.get(url,headers=headers)
        g_batchId=res.json()['data'][0]['batchId']
        self.assertEqual("ok",res.json().get("state"))

    def test_02_findFinishedPage(self):
        """已考考试列表接口测试"""
        url=host + datalist[12][2]
        headers= eval(datalist[12][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[12][5])
        res=requests.get(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))

    def test_03_enter(self):
        """进入考试接口测试"""
        global g_examPaperId
        url=host + datalist[13][2]
        headers= eval(datalist[13][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[13][5])
        res=requests.get(url,headers=headers,data=values)
        g_examPaperId=res.json()['data']['examPaperId']
        # print(g_examPaperId)
        self.assertEqual("ok",res.json().get("state"))

    def test_04_findPaper(self):
        """获取试卷接口测试"""
        url=host + datalist[14][2]
        headers= eval(datalist[14][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[14][5])
        res=requests.get(url,headers=headers,data=values)
        # print(res.json())
        self.assertEqual("ok",res.json().get("state"))

    def test_05_viewPaper(self):
        """查看试卷接口测试"""
        global g_subjectId
        url=host + datalist[15][2]
        headers= eval(datalist[15][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[15][5])
        res=requests.get(url,headers=headers,data=values)
        g_subjectId=res.json()['data']['subjects']['multiChoices'][0]['subjectId']
        # print(g_subjectId)
        self.assertEqual("ok",res.json().get("state"))

    def test_06_answer(self):
        """提交答案接口测试"""
        url=host + datalist[16][2]
        headers= eval(datalist[16][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[16][5])
        res=requests.post(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))

    def test_07_hand(self):
        """交卷接口测试"""
        url=host + datalist[17][2]
        headers= eval(datalist[17][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[17][5])
        res=requests.post(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))


