# 1. Define a class name Student and initialize attributes: name, age, email and sex. Creat a new object of that class.

class Student:
    def __init__(self, name, age, email, sex):
        self.name = name
        self.age = age
        self.email = email
        self.sex = sex

    def get_name(self):
        return self.name

#Student1 = Student('Hung', 19, 'hung@gmail.com', 'Male')
#Student2 = Student('Lan', 18, 'tuan@gmail.com', 'female')
''''
def show_all():
    print(f'Student 1- Name  :{Student1.name}')
    print(f'           age   :{Student1.age}')
    print(f'           Email :{Student1.email}')
    print(f'           Sex   :{Student1.sex}')

#Show_all()
'''

# 2. Define a class named People with no attributes and mothods. Creat a new object of that class.
class People:
    def __init__(self) -> None:
        pass

People1 = People()

#print(People)

# 3.
# 3.1 Define a class named Staff with attributes: role, deparment, salary and a method named show_details() to display all attributes.
#     department attribute is protected, salary attribute is private.
class Staff:
    def __init__(self, role, deparmente,salary):
        self.role = role
        self._deparmente = deparmente
        self.__salary = salary

    def show_details(self):
        return self.role, self._deparmente, self.__salary

    def show_deparmente(self):
        return self._deparmente

    def show_salary(self):
        return self.__salary
''''
Staff1 = Staff('Manager','CEO','2000$')
Staff2 = Staff('Quantity Surveyor', 'QS', '1000$')
'''
#print(f'Staff1: Role/Deparmente/Salary:{Staff1.show_details()}')


# 3.2 Define a class named Student with inherited from Staff class. This class has more 2 attribute: name and age.
class student_new(Staff):
    def __init__(self, role, deparmente, salary, name, age):
        super().__init__(role, deparmente, salary)
        self.name = name
        self.age = age


# 3.3 Creat a new object of Student then show all attribute of that object.


    def show_role(self):
        return self.role

    def show_name(self):
        return self.name
    
    def show_age(self):
        return self.age

    def show_all_stu():
        print(f'Student1- Name : {Stu1.show_name()}\
            Age  : {Stu1.show_age()}\
            Role : {Stu1.show_role()}\
            Deparmente: {Stu1.show_deparmente()}\
            Salary: {Stu1.show_salary()}'  )

Stu1 = student_new('aaa','bbb',100,'Toan',20)
Stu1.show_all_stu()

# 4.
# 4.1 Define a class named Geometry with 2 methods: get_area() and get_perimeter().
print('============================================== 4.1 ==============================================')
class Geometry:
    def __init__(self):
        pass

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

# 4.2 Define a class named Square which inherited from Geometry class. This class has 2 attributes are length and width. Override two methods from its parrent.
print('============================================== 4.2 ==============================================')
class Square(Geometry):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        super().__init__()

    def get_area(self):
        S = self.length * self.width
        return S

    def get_perimeter(self):
        P = 2*(self.length + self.width)
        return P

squ = Square(3,4)
print(f'Area of Square: {squ.get_area()}')
print(f'Perimeter of Square: {squ.get_perimeter()}')

# 4.3 Define a class named Circle which inherited from Geometry class. This class has 1 attribute is radius. Override 2 methods of its parrent  class.
print('============================================== 4.3 ==============================================')
class Circle(Geometry):
    def __init__(self,radius):
        self.radius = radius
        super().__init__()

    def get_area(self):
        S = self.radius * 3.14
        return S

    def get_perimeter(self):
        C = 2 * self.radius * 3.14
        return C

cir = Circle(3)
print(f'Area of Circle: {cir.get_area()}')
print(f'Perimeter of Circle: {cir.get_perimeter()}')


# 4.4 Create a new object of class Square and a new object of class Circle. Print area and primeter of those.
print('============================================== 4.4 ==============================================')

# 4.
# 4.1 Define a class named Geometry with 2 methods: get_area() and get_perimeter().


# 4.2 Define a class named Square which inherited from Geometry class. This class has 2 attributes are length and width. Override two methods from its parrent.
# 4.3 Define a class named Circle which inherited from Geometry class. This class has 1 attribute is radius. Override 2 methods of its parrent  class.
# 4.4 Create a new object of class Square and a new object of class Circle. Print area and primeter of those.
