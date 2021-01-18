import unittest
import requests
from utils.tools import readexcle,createreport,Db
from utils.request_tools import requestsUtils
#利用封装的request工具类来实现
request=requestsUtils()
host = "http://118.24.255.132:2333"
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")
db=Db("118.24.255.132","testgoup","1qaz!QAZ","ljtestdb")

class TestInspirer(unittest.TestCase):
    @classmethod
    def setUpClass(cls,token):
        cls.requests=requests.Session()
        url = host + datalist[0][2]
        headers = eval(datalist[0][4])
        judge_headers = eval(datalist[0][4])
        data={"username":"hahah","password":"1234567890"}
        res= request.post_main(url,headers,data,judge_headers)
        cls.token=res.json()["data"]["token"]
        print(cls.token)

    @classmethod
    def tearDownClass(cls):
        print("测试结束！")

    def test_01_inspirernew(self):
        """测试发表灵感接口"""
        url = host + datalist[1][2]
        headers = eval(datalist[1][4])
        judge_headers = eval(datalist[1][4])
        headers.update(token=self.token)
        data = eval(datalist[1][5])
        global iid
        # res = self.requests.post(url,headers=headers,json=data)
        res= request.post_main(url,headers,data,judge_headers)
        iid=db.query("SELECT id FROM t_inspirer WHERE uid=1333365113 ORDER BY createtime DESC LIMIT 1;")[0][0]
        # print(iid)
        # 断言
        self.assertEqual(200,res.json().get("status"))

    def test_02_inspirerupdate(self):
        """修改测试发表灵感接口"""
        url = host + datalist[5][2]
        headers = eval(datalist[5][4])
        judge_headers = eval(datalist[5][4])
        headers.update(token=self.token)
        data = {"content":"1111111111","iid":iid}
        # res = self.requests.post(url,headers=headers,json=data)
        res= request.post_main(url,headers,data,judge_headers)
        self.assertEqual(200,res.json().get("status"))

    def test_03_inspirerdelete(self):
        """删除测试发表灵感接口"""
        url = host + datalist[6][2]
        headers = eval(datalist[6][4])
        judge_headers = eval(datalist[6][4])
        headers.update(token=self.token)
        data = {"iid":iid}
        # res = self.requests.post(url,headers=headers,json=data)
        res= request.post_main(url,headers,data,judge_headers)
        self.assertEqual(200,res.json().get("status"))

if __name__ == "__main__":
    unittest.main(verbosity=2)