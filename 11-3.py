class Employee():
    def __init__(self,f_name,l_name,salary):
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.salary = salary
    def give_raise(self,other=''):
        if other:
            self.salary += int(other)
        else:
            self.salary += 5000
        return self.salary
import unittest
class test_Employee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('zhang','san',5000)
        self.default_salary = 7000
        self.custom_salary = 10000
    def test_give_default_raise(self):
        salary = self.employee.give_raise(2000)
        self.assertEqual(salary,self.default_salary)
    def test_give_costom_salary(self):
        salary = self.employee.give_raise()
        self.assertEqual(salary,self.custom_salary)
unittest.main()
        
    
