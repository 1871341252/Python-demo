import unittest
from utils.tools import readexcle,createreport
import requests


host = "http://118.24.255.132:2333"
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")


class TestLogin(unittest.TestCase):

    def test_01_login(self):
        """登录接口测试用例"""
        url = host + datalist[0][2]
        headers = eval(datalist[0][4])
        data = eval(datalist[0][5])
        yuqi = int(datalist[0][6])
        res = requests.post(url,headers=headers,json=data)
        # 断言
        shiji = res.json()["status"]
        self.assertEqual(yuqi,shiji)

    def test_02_inspirernew(self):
        """登录接口测试用例"""
        url = host + datalist[1][2]
        headers = eval(datalist[1][4])
        data = eval(datalist[1][5])
        yuqi = int(datalist[1][6])
        res = requests.post(url,headers=headers,json=data)
        # 断言
        shiji = res.json()["status"]
        self.assertEqual(yuqi,shiji)

    def test_03_getinspirer(self):
        """登录接口测试用例"""
        url = host + datalist[2][2]
        headers = eval(datalist[2][4])
        data = datalist[2][5]
        yuqi = int(datalist[2][6])
        res = requests.get(url+"?"+data,headers=headers,json=data)
        # 断言
        shiji = res.json()["status"]
        self.assertEqual(yuqi,shiji)


# if __name__ == "__main__":
#     unittest.main(verbosity=2)