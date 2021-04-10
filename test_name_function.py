import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('xinya','zhao')
        self.assertEqual(formatted_name,'Xinya Zhao')
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('xinya','zhao','w')
        self.assertEqual(formatted_name,'Xinya W Zhao')
unittest.main()