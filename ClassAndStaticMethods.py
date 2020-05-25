import sys


class Employee:

    num_of_emps = 0
    raise_amount = 1.04  # Class Variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class Method using a Decorator
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp_1 = Employee('Rashmi', 'Chotalia', 50000)
emp_2 = Employee('Joe', 'Bloggs', 60000)

Employee.set_raise_amount(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(sys.path)
