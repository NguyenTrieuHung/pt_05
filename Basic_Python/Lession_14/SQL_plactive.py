''' 
1. Create DB
a, Create a new database named VTI_Employees.
b, Create 2 tables:
- Table 1: Employee_Info
    + Emp_ID <Primary key>
    + Name
    + DoB
    + Email
    + MobileNumber

- Table 2: Employee_Work
    + Emp_ID <Secondary key>
    + Role
    + Department
    + Salary

2. Write the program to do following tasks:
a, Display the menu:
----------- Select Operation -------------
O_1. Display all employees information
O_2. Display employee information with specific Name
O_3. Insert a new employee
O_4. Update a specific employee with Emp_ID
O_5. Delete a specific employee with Emp_ID

b, Perform coresponding operations based on the user's choice.
'''
'''
import mysql.connector

myconn = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root")
print('Connected to MySQL Database')

cur = myconn.cursor()

cur.execute("create database VTI_Employees")

cur.execute("""
   CREATE TABLE Employee_Work(
        Emp_ID  VARCHAR(10) PRIMARY KEY,
        Name VARCHAR(50) NOT NULL,
        DoB DATE NOT NULL,
        Email VARCHAR(100) NOT NULL,
        MobileNumber INT NOT NULL
   )
""")

cur.execute("""
   CREATE TABLE Employee_Info(
        Emp_ID  VARCHAR(10) PRIMARY KEY,
        Role VARCHAR(50) NOT NULL,
        Department VARCHAR(100) NOT NULL,
        Salary INT NOT NULL
   )
""")

cur.execute("show databases")
for row in cur:
   print(row)

myconn.close()
'''
'''
Table 1: Employee_Info
    + Emp_ID <Primary key>
    + Name
    + DoB
    + Email
    + MobileNumber

- Table 2: Employee_Work
    + Emp_ID <Secondary key>
    + Role
    + Department
    + Salary

2. Write the program to do following tasks:
a, Display the menu:
----------- Select Operation -------------
O_1. Display all employees information
O_2. Display employee information with specific Name
O_3. Insert a new employee
O_4. Update a specific employee with Emp_ID
O_5. Delete a specific employee with Emp_ID

b, Perform coresponding operations based on the user's choice.
'''

from ast import While
from sqlalchemy import true


class Employee_Info:
    def __init__(self,Emp_ID, Name, DoB, Email, MobileNumber):
        self.Emp_ID = Emp_ID
        self.Name = Name
        self.DoB = DoB
        self.Email = Email
        self.MobileNumber = MobileNumber

    def get_id(self):
        return self.Emp_ID

    def get_name(self):
        return self.Name

    def get_DoB(self):
        return self.DoB
    
    def get_email(self):
        return self.Email
    
    def get_mobile(self):
        return self.MobileNumber

    def set_name(self,name):
        self.name = name

    def set_id(self,id):
        self.Emp_ID =id

    def set_id(self,id):
        self.Emp_ID =id
    
    def set_id(self,id):
        self.Emp_ID =id

    def set_id(self,id):
        self.Emp_ID =id

    def set_id(self,id):
        self.Emp_ID =id

    def set_id(self,id):
        self.Emp_ID =id


class Employee_Work(Employee_Info):
    def __init__(self, Emp_ID, Name, DoB, Email, MobileNumber, Role, Department, Salary):
        super().__init__(Emp_ID, Name, DoB, Email, MobileNumber)
        self.Role = Role
        self.Department = Department
        self.Salary = Salary

    def get_role(self):
        return self.Role

    def get_department(self):
        return self.Department

    def get_salary(self):
        return self.Salary
    
    def show_info(self):
        print('\nInfo employee:\n')
        print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'.format('ID', 'Name', 'Date of birth', 'Email', 'Mobile', 'Role', 'Deparment', 'Salary'))
        print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'.format(self.get_id(), self.get_name(), self.get_DoB(), self.get_email(), self.get_mobile(), self.get_role(), self.get_department(), self.get_salary()))
       
# emp1 = Employee_Work(101,101,101,101,101,101,101,101)
# emp2 = Employee_Work(102,102,102,102,102,102,102,102)

from sqlalchemy import true
list_employee = []
while true:
    print(f'''\n----------- Select Operation -------------
        0. Out program
        1. Display all employees information
        2. Display employee information with specific Name
        3. Insert a new employee
        4. Update a specific employee with Emp_ID
        5. Delete a specific employee with Emp_ID
        ''')
    select = input('Please Select Operation:')

    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        
        elif select == 3:
            id = input('Input ID:')
            name = input('Input Name:')
            inputDate = input("Enter the date of birth : ")
            email = input('Input Email:')
            mobileNumber = input('Input MobileNumber:')
            role = input('Input Role:')
            department = input('Input Department:')
            salary = input('Input Salary:')
            employee = Employee_Work(id, name, inputDate, email, mobileNumber, role, department, salary)
            print('Input employee successful !!!')
            list_employee.append(employee)
            
        
        elif select == 1:
            if len(list_employee) == 0:
                print('Currently no employee. Please add a new employee to the list !')
            else:
                print('---LIST EMPLOYEE---\n')
                print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'
                   .format('ID', 'Name', 'Date of birth', 'Email', 'Mobile', 'Role', 'Deparment', 'Salary'))
                print('\n')   
                for i in list_employee:
                   print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'
                   .format(i.get_id(), i.get_name(), i.get_DoB(), i.get_email(), i.get_mobile(), i.get_role(), i.get_department(), i.get_salary()))
                print('\n')
        
        elif select == 2:
            if len(list_employee) == 0:
                print('Currently no employee. Please add a new employee to the list !')
            else:
                name_input = input('Enter the name you want to search for:')
                for i in list_employee:
                    if i.get_name() == name_input:
                        i.show_info()
                        break
                print('Your name is not on the list:')
        elif select == 4:
            if len(list_employee) == 0:
                print('Currently no employee. Please add a new employee to the list !')
            else: 
                id_input = input('Enter the ID you want to fix for:')
                for i in list_employee:
                    if i.get_id() == id_input:
                        i.show_info()
                        i.name = input('Input Name:')
                        i.DoB = input("Enter the date of birth DD/MM/YYY: ")
                        i.email = input('Input Email:')
                        i.mobileNumber = input('Input MobileNumber:')
                        i.role = input('Input Role:')
                        i.department = input('Input Department:')
                        i.salary = input('Input Salary:')
                        print('Input employee successful !!!')
                        i.show_info()
                        break
                print('Your ID is not on the list:')
        
        elif select == 6:
            list = []
            for i in list_employee:
                L = "Emp_id: {} Name: {} Dob: {} Email: {} Mobile number: {} Role: {} Department: {} Salary: {} ".format(i.get_id(), i.get_name(), i.get_DoB(), i.get_email(), i.get_mobile(), i.get_role(), i.get_department(), i.get_salary())
                list.append(L)
            print(list)
            with open('text.txt','w') as file:
                file.writelines(str(list))



    else:
        print('This task is not available !!')
        print('Please input number !!')



