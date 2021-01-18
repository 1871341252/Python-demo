import unittest
import requests
from utils.tools import readexcle,createreport,Db

host = "http://118.24.255.132:2333"
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")
db=Db("118.24.255.132","testgoup","1qaz!QAZ","ljtestdb")

class TestInspirer(unittest.TestCase):
    def setUp(self):
        self.requests=requests.Session()
        url=host+"/login"
        headers={"Content-Type":"application/json"}
        data={"username":"hahah","password":"1234567890"}
        res=self.requests.post(url,headers=headers,json=data)
        self.token=res.json()["data"]["token"]

    def tearDown(self):
        print("测试结束！")


    def test_01_inspirernew(self):
        """测试发表灵感接口"""
        url = host + datalist[1][2]
        headers = eval(datalist[1][4])
        headers.update(token=self.token)
        data = eval(datalist[1][5])
        global iid
        res = self.requests.post(url,headers=headers,json=data)
        iid=db.query("SELECT id FROM t_inspirer WHERE uid=1333365113 ORDER BY createtime DESC LIMIT 1;")[0][0]
        # 断言
        self.assertEqual(200,res.json().get("status"))
    def test_02_inspirerupdate(self):
        """修改测试发表灵感接口"""
        url = host + datalist[5][2]
        headers = eval(datalist[5][4])
        headers.update(token=self.token)
        data = {"content":"1111111111","iid":iid}
        res = self.requests.post(url,headers=headers,json=data)
        self.assertEqual(200,res.json().get("status"))

    def test_03_inspirerdelete(self):
        """删除测试发表灵感接口"""
        url = host + datalist[6][2]
        headers = eval(datalist[6][4])
        headers.update(token=self.token)
        data = {"iid":iid}
        res = self.requests.post(url,headers=headers,json=data)
        self.assertEqual(200,res.json().get("status"))

if __name__ == "__main__":
    unittest.main()
    

'''
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
'''
