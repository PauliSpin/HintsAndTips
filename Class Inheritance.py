# Define a class called Employee which has
# FirstName, LastName and Pay attributes only.
#
# Define Developer as a subclass of Employee.
# Developer will inherit FirstName, LastName and Pay
# but it also has Language.
#


class Employee(object):
    def __init__(self, FirstName, LastName, pay):
        self.FirstName = FirstName
        self.LastName = LastName
        self.pay = pay


class Developer(Employee):
    def __init__(self, FirstName, LastName, pay, language):
        super().__init__(FirstName, LastName, pay)
        self.language = language


emp_1 = Employee('Clark', 'Kent', 50000)
emp_2 = Developer('Bruce', 'Wayne', 60000, 'Python')

print(
    f'Employee 1: FirstName = {emp_1.FirstName},\nLastName = {emp_1.LastName}')

print()
print(
    f'Employee 2: FirstName = {emp_2.FirstName},\nLastName = {emp_2.LastName},\nLanguage = {emp_2.language}')
