import os
import sys
import unittest

# 查看当前运行环境所在路径

curr_file = os.path.abspath(__file__)
curr_dir = os.path.dirname(curr_file)
project_root = os.path.dirname(curr_dir)

# 在python搜索路径里添加项目所在路径

sys.path.insert(0, project_root)

from src.my_greeter import MyGreeter

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()
        print('Test started!')

    @classmethod # 1101：添加本方法以表示测试结束（如有必要释放资源等）
    def tearDownClass(cls):
        print('Test ended!')

    def test_init(self):
            self.assertIsInstance(self._my_greeter, MyGreeter)

    def test_greeting(self):
        self.assertTrue(len(self._my_greeter.greeting())>0)

    def test_exception(self): # 1101：添加本方法以捕获任何未知错误
        try:
            return self._my_greeter.greeting()
        except Exception:
             print('unexpected error')

if __name__ == '__main__':
    unittest.main()