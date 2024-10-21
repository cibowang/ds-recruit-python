import unittest
import os
import sys
from unittest.mock import patch 

# 查看当前运行环境所在目录：/home/cibo/Git1/ds-recruit
print(sys.path)

curr_file = os.path.abspath(__file__)
curr_dir = os.path.dirname(curr_file)
project_root = os.path.dirname(curr_dir)

# 搜索路径里加入了project_root：/home/cibo/Git1/ds-recruit/python
sys.path.insert(0, project_root)



from src.my_greeter import MyGreeter


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter)

    def test_greeting(self):
        result = MyGreeter.greeting(self)
        if not result is None and len(result) > 0:
            self.assertTrue(len(self._my_greeter.greeting()))

    @patch('src.my_greeter.datetime.datetime')  
    def test_greeting_morning(self, mock_datetime):  
        mock_datetime.now.return_value.hour = 7  # 模拟早上7点  
        self.assertEqual(self._my_greeter.greeting(), "Good morning")  
 
    @patch('src.my_greeter.datetime.datetime')  
    def test_greeting_afternoon(self, mock_datetime):  
        mock_datetime.now.return_value.hour = 13  # 模拟下午1点  
        self.assertEqual(self._my_greeter.greeting(), "Good afternoon")  
 
    @patch('src.my_greeter.datetime.datetime')  
    def test_greeting_evening(self, mock_datetime):  
        mock_datetime.now.return_value.hour = 19  # 模拟晚上7点  
        self.assertEqual(self._my_greeter.greeting(), "Good evening")

    @patch('src.my_greeter.datetime.datetime')  
    def test_greeting_boundary_morning(self, mock_datetime):  
        mock_datetime.now.return_value.hour = 11  # 模拟11点59分  
        self.assertEqual(self._my_greeter.greeting(), "Good morning")  
 
    @patch('src.my_greeter.datetime.datetime')  
    def test_greeting_boundary_afternoon(self, mock_datetime):  
        mock_datetime.now.return_value.hour = 12  # 模拟12点  
        self.assertEqual(self._my_greeter.greeting(), "Good afternoon")

if __name__ == '__main__':
    unittest.main()