import unittest
from give_raise_function import Employee
class TestSalary(unittest.TestCase):
    def test_give_default_raise(self):
        user1 = Employee('Sabrina', 2000)
        user1.display_info()  
        user1.give_employee_raise()
        user1.display_info()  
    def test_not_default_raise(self):
        user2 = Employee("ZXY", 6000)
        user2.display_info()
        user2.update_raise(3000)
        user2.give_employee_raise()
        user2.display_info()

unittest.main()