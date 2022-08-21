'''
Write a Python program to calculate the payroll of employees in a company.
There are 2 types of employees: full-time employees and part-time employees
Classes are required:

1. Employee: abstract class
- 2 attributes: first name and last name
- 1 method to return the full name
- 1 abstract method to return employee's salary
'''
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return  'Full name: {}\n{}'.format(self.last_name,self.first_name)

#emobj= Employee('Hung','Nguyen Trieu')

#print(f'{emobj.full_name()}')
    @abstractmethod
    def get_salary(self):
        pass


'''
2. Full-time employee: inherit from class employee
- 1 attribute: salary.
'''
class Full_time_employee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary


'''
3. Part-time employee: inherit from employee class
- 2 attributes: working hours and rate
'''
class Part_time_employee(Employee):
    def __init__(self, first_name, last_name, working_hours, rate):
        super().__init__(first_name, last_name)
        self.working_hours = working_hours
        self.rate = rate

    def get_salary(self):
        return self.working_hours * self.rate

'''
4. Payroll: 
- 1 atribute: employee list
- 1 method to append employee to employee list
- 1 more method to show full name and salary for a given employee.
'''
class Payroll:
    def __init__(self):
         self.employees = []

    def append_employee(self, employee):
        self.employees.append(employee)
        # return self.employees
            
    def display_employees(self):
        for employee in self.employees:    
            employee.get_full_name()
            employee.get_salary()
            print('-------------------')

while truel:
    def main():
        pay_roll=Payroll()
        check = input("Do you want to work full time or part time(F-full/P-parst)?: ")
        if check == 'F' or 'f':
            first_name = input('First Name: ')
            last_name = input('last_name: ')
            salary = int(input('Salary:'))
            Full_time_Employees = Full_time_Employee(first_name, last_name,salary)
            pay_roll.append(Full_time_Employees)
            return (pay_roll)
            
        elif check == 'P' of 'p':
            first_name = input('First Name: ')
            last_name = input('last_name: ')
            salary = int(input('Salary:'))
            rate = int(input('Rate::'))
            Part_time_Employees = Part_time_Employee(first_name, last_name,salary,rate)
            pay_roll.append(Part_time_Employees)
            return (pay_roll)
        else:
            print('Please input F or P to Full time or Part time')
        pay_roll.show_full_name_and_salary()


main()

''''
pay_1 = Payroll()
full_time_1 = Full_time_Employee('Loc', 'Huynh', 2000)
pay_1.append_employee(full_time_1)
part_time_1= Part_time_Employee('Trung', 'Van', 30, 3)
pay_1.append_employee(part_time_1)
pay_1.show_full_name_and_salary()
'''
