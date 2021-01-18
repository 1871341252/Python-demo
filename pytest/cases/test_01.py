import unittest

class TestDemo(unittest.TestCase):
    def test_01(self):
        """测试用例1"""
        a = 1 + 1
        self.assertEqual(a,2)
    def test_02(self):
        """测试用例2"""
        a = 1 + 1
        self.assertEqual(a,3,msg="这是测试失败的用例")
    def test_03(self):
        """测试用例3"""
        a = 1 + 1
        self.assertEqual(a,2)


#if __name__ == "__main__":
#    unittest.main(verbosity=2)
