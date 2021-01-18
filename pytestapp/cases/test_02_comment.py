import unittest
import requests
from utils.tools import readexcle,createreport,Db

db=Db("192.168.50.11",3312,"root","szgr123","gre_study")
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")
host="http://test.geron-e.com"


class TestComment(unittest.TestCase):
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

    def test_01_comment(self):
        """评论接口测试"""
        global commentId
        global g_refId
        url = host + datalist[1][2]
        headers= eval(datalist[1][4])
        values= eval(datalist[1][5])
        headers.update(sessionId=self.token)
        res=requests.get(url,headers=headers,data=values)
        commentId=db.query("SELECT id FROM gre_video_comment WHERE accountId = 95442 ORDER BY createAt DESC LIMIT 1;")
        g_refId=res.json().get("data").get("refId")
        self.assertEqual("ok",res.json().get("state"))
        
    def test_02_collect(self):  
        """收藏接口测试"""
        url = host + datalist[2][2]
        headers= eval(datalist[2][4])
        values= eval(datalist[2][5])
        headers.update(sessionId=self.token)
        res=requests.get(url,headers=headers,data=values)
        self.assertEqual("ok",res.json().get("state"))

# run=TestComment()
# run.test_01_comment()
# run.test_01_collect


# if __name__ == "__main__":
#     unittest.main(verbosity=1)
