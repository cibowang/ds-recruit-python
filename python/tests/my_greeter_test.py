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
        try:
            cls._my_greeter = MyGreeter()
        except AttributeError as e:
            print(e)
        else:
            print('Test started!')

    @classmethod # 此处添加本方法以表示测试结束（如有必要释放资源等）
    def tearDownClass(cls):
        print('Test ended!')

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter) # 此处配合测试可以更改class对象

    def test_greeting(self):
            self.assertTrue((self._my_greeter.greeting is not None)) # 此处更改为条件判断式进行测试

if __name__ == '__main__':
    unittest.main()