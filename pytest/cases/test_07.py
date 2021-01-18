import unittest
import requests
from utils.tools import readexcle,createreport

host = "http://118.24.255.132:2333"
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")

class Regist(unittest.TestCase):
    def test_01_regist(self):
        url=host+datalist[3][2]
        headers=eval(datalist[3][4])
        data=eval(datalist[3][5])
        yuqi=int(datalist[3][6])
        res=requests.post(url,headers=headers,json=data)
        self.token=res.json().get("data").get("token")
        shiji=res.json().get("status")
        self.assertEqual(yuqi,shiji)

    def test_02_login(self):
        url=host+datalist[4][2]
        headers=eval(datalist[4][4])
        data=eval(datalist[4][5])
        yuqi=int(datalist[4][6])
        res=requests.post(url,headers=headers,json=data)
        shiji=res.json().get("status")
        self.assertEqual(yuqi,shiji)

