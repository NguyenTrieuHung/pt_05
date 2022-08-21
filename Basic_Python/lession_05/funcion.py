#1. Define a function that takes 2 values and returns its sum, division, subtraction, and multiplication (use exception for divisors)


from itertools import count
from math import sqrt

from numpy import zeros


def func1():
    x = int(input("Nhập số thứ nhất:"))
    y = int(input("Nhập số thứ hai:"))
    tong = x+y
    hieu = x-y
    tich = x*y
    thuong = x/y
    return print('tong hai so la: ',tong,
                'hieu hai so la: ', hieu,
                'tich hai so la :', tich,
                'thuong hai so la:', thuong)  



#2. Define a function to check if a number from the keyboard is a squared number,

def func2():
    x = int(input("Nhập số x ="))
    for i in range(x):
        if i*i == x:
            print('x la so chinh phuong')
            return
    print('x khong phai so chinh phuong')
        

#func2() 

#3. Define a function that accepts 3 arguments, then checks if there exists a triangle created by them. Return results.
def func3():
    x = int(input("Nhập số thứ nhất:"))
    y = int(input("Nhập số thứ hai:"))
    z = int(input("Nhập số thứ ba:"))
    if x+y>z and x+z>y and y+z>x:
        print('z,y,z la 3 canh cua mot tam giac')
    else:
        print('z,y,z khong la 3 canh cua mot tam giac')

#func3()




#4. Defines a function that accepts a string argument and returns the number of negative integers and consonants.
def func4():
    chuoi = str(input("nhập chuỗi bất kỳ:"))
    count1=0
    for i in chuoi:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count1=count1+1
    print('số nguyên âm trong chuỗi là:', count1)

#func4()


#5. Define a function that accepts a number (n) and returns the first n numbers of the Fibonacci sequence.

def fibonacci(n):
    n0=0
    n1=1
    count1=0
    if n<=0:
        print('khong co day fibonacci thoa man')
    elif n==1:
        print('0,1,1')
    else:
        while count1<n:
            print(n0)
            nn = n0 + n1
            # update values
            n0 = n1
            n1 = nn
            count1 += 1

fibonacci(15)
'''''
print("dãy số fibonacci: ")
sb = ""
n=9
for i in range(0,n):
    sb = sb + str(fibonacci(i)) + ", ";
print(sb)

fibonacci(9)




print("dãy số fibonacci: ");
sb = "";
for i in range(0,:
    sb = sb + str(func5(i)) + ", ";
print(sb)

func5()
'''
''''
def Fibonacci(n):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif n == 1:
        print("Fibonacci sequence upto", n,":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

Fibonacci(10)
'''




#6. Define a function that accepts a radius argument and returns the area and perimeter

def calculate_circle(radius):
    area = radius * radius * 3.14
    peri = 2 * radius * 3.14
    return area, peri