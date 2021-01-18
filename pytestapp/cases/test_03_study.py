import unittest
import requests
from utils.tools import readexcle,createreport,Db

db=Db("192.168.50.11",3312,"root","szgr123","gre_study")
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")
host="http://test.geron-e.com"

class TestStudy(unittest.TestCase):
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

    def test_01_findEffectOrder(self):
        """我的课程接口测试"""
        global g_planId
        global g_kurseId
        url=host + datalist[3][2]
        headers= eval(datalist[3][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[3][5])
        res=requests.get(url,headers=headers,data=values)
        g_planId=res.json()['data'][1]['id']
        g_kurseId=res.json()['data'][1]['kurseId']
        self.assertEqual("ok",res.json().get("state"))

    def test_02_course(self):
        """学习计划接口测试"""
        url=host + datalist[4][2]
        headers= eval(datalist[4][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[4][5])
        res=requests.get(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))

    def test_03_articleList(self):
        """图文列表接口测试"""
        global g_lessonId1
        url=host + datalist[5][2]
        headers= eval(datalist[5][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[5][5])
        res=requests.get(url,headers=headers,data=values)
        g_lessonId1=res.json()['data'][0]['lessonId']
        self.assertEqual("ok",res.json().get("state"))

    def test_04_videoList(self):
        """视频列表接口测试"""
        global g_lessonId2
        url=host + datalist[6][2]
        headers= eval(datalist[6][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[6][5])
        res=requests.get(url,headers=headers,data=values)
        g_lessonId2=res.json()['data'][0]['videoList'][0]['lessonId']
        self.assertEqual("ok",res.json().get("state"))

    def test_05_articleDetail(self):
        """图文详情接口测试"""
        url=host + datalist[7][2]
        headers= eval(datalist[7][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[7][5])
        res=requests.get(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))

    def test_06_videoDetail(self):
        """视频详情接口测试"""
        url=host + datalist[8][2]
        headers= eval(datalist[8][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[8][5])
        res=requests.get(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))
    
    def test_07_brushExercises(self):
        """刷题练习接口测试"""
        url=host + datalist[9][2]
        headers= eval(datalist[9][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[9][5])
        res=requests.get(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))

    def test_08_brushErrorTopic(self):
        """刷错题接口测试"""
        url=host + datalist[10][2]
        headers= eval(datalist[10][4])
        headers.update(sessionId=self.token)
        values=eval(datalist[10][5])
        res=requests.get(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))

    
# if __name__ == "__main__":
#     unittest.main(verbosity=2)