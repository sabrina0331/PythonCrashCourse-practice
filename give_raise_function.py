class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.raise_salary = 5000
    def give_employee_raise(self):
        self.salary += self.raise_salary
    def update_raise(self, raise_salary):
        self.raise_salary = raise_salary
    def display_info(self):
        print(self.name +" 's origin salary is "+ str(self.salary)+" , and it raised:  "+ str(self.raise_salary))

