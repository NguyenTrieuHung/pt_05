'''
Write a Python program to calculate the payroll of employees in a company.
There are 2 types of employees: full-time and part-time employees
Need to have classes:
1. Employee: abstract class
- 2 atributes: firt name and last name
- 1 method to return full name
- 1 abstract method to return salary for employees
2. Full-time employee: inherited from employee class
- 1 atributes: salary.
3. Part-time employee: inherited from employee class
- 2 atributes: worked_hours and rate
4. Payroll: 
- 1 atribute: employee list
- 1 method to append employee to employee list
- 1 more method to show full name and salary for a given employee.
The program will receive employee information from the keyboard.
'''
from abc import ABC, abstractmethod, abstractclassmethod
from calendar import c
from queue import Full

class Employee(ABC):
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @abstractmethod
    def get_salary(self):
        pass

class Full_time_Employee(Employee):
    def __init__(self,first_name,last_name,salary):
        super().__init__(first_name,last_name)
        self.salary=salary
    
    def get_salary(self):
        return self.salary
    
class Part_time_Employee(Employee):
    def __init__(self,first_name,last_name,worked_hours,rate):
        super().__init__(first_name,last_name)
        self.worked_hours=worked_hours
        self.rate=rate
    
    def get_salary(self):
        return self.worked_hours*self.rate
    
class Payroll():
    def __init__(self):
        self.employees=[]
        
    def append_employee(self, employee):
        self.employees.append(employee)
            
    def show_full_name_and_salary(self):
        for employee in self.employees:
            print(employee.get_full_name())
            print(employee.get_salary())


def get_info_employee():
    full_time_obj = []
    Part_time_Employees = []
    check1 = input("Do you want to work full time or part time(F-full/P-parst)?: ")
    if check1 == 'F':
        first_name = input('First Name: ')
        last_name = input('last_name: ')
        salary = int(input('Salary:'))
        Full_time_Employees = Full_time_Employee(first_name, last_name,salary)
        full_time_obj.append(Full_time_Employees)
        return (full_time_obj)
    elif check1 == 'P':
        first_name = input('First Name: ')
        last_name = input('last_name: ')
        salary = int(input('Salary:'))
        range = int(input('Ranger:'))
        employee = Part_time_Employee(first_name, last_name,salary,range)
        Part_time_Employees.append(employee)
        return (Part_time_Employees)
    

get_info_employee()

'''
def display_info_employee(employees):
        show_full_name_and_salary(employees)

def main():
    employ = get_info_employee()
    display_info_employee(employ)
main()


pay_1 = Payroll()
full_time_1 = Full_time_Employee('Loc', 'Huynh', 2000)
pay_1.append_employee(full_time_1)
part_time_1= Part_time_Employee('Trung', 'Van', 30, 3)
pay_1.append_employee(part_time_1)
pay_1.show_full_name_and_salary()
'''
