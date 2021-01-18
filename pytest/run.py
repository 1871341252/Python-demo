import unittest
from utils.HTMLTestRunner import HTMLTestRunner
import time

nowtime = time.strftime("%y-%m-%d_%H_%M_%S")
suite = unittest.TestSuite()  # 对测试套件进行实例化
tests = unittest.defaultTestLoader.discover("./cases",pattern="test_*.py")
suite.addTests(tests)  # 把用例添加到测试套件中
with open("./reports/{}的测试报告.html".format(nowtime),"wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=2,
        title="测试报告",description="执行人：浪晋")  # 运行的类
    runner.run(suite)  # 运行
