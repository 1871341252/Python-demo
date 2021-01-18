import unittest
import requests
from utils.tools import readexcle,createreport
from utils.api import requestsUtils
import json

host = "http://118.24.255.132:2333"
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")
request= requestsUtils()

class TestLogin(unittest.TestCase):

    def test_01_login(self):
        """登录接口测试用例"""
        row = 0
        res=request.post1(row)
        # 断言
        self.assertEqual(200,res.json().get("status"))

    def test_02_getinspirer(self):
        """获取灵感列表用例"""
        # headers = eval(datalist[5][10])
        # print(headers)
        row = 2
        res=request.get1(row)
        # print(res.json())
        # 断言
        self.assertEqual(200,res.json().get("status"))

    

if __name__ == "__main__":
    unittest.main(verbosity=2)