
#1 Create a list named my_list with items which have different data types and length at least 5
print("#1==== Create a list named my_list with items which have different data types and length at least 5")
my_list=['mot','hai','ba',4,5]
print(my_list)


print('#2====Print all items of my_list in single line')
for i in (my_list):
    print (i)


print('#3==== Count the number of each items in my_list')
count=0
for i in my_list:
    count=count+1
    print(i,count)


print('#4==== Reverse the order of the item in my_list')
my_list.reverse()
print(my_list)

print('#5==== Square the numeric items of items in my_list then print result:')
for i in my_list:
    if type(i) is int:
         print(i**2)


print('#6==== Add some single values and iterable values to my_list:')
my_list.append(2000)
print(my_list)
my_list.extend([1900,1800])
print(my_list)

print('#7==== Remove values at the end and at the second position of my_list')
my_list.pop()
my_list.pop(1)
print(my_list)

print('#8==== Display those items from my_list that are divisible by 5')
for i in my_list:
    if type(i) is int:
        if i %5==0:
             print(i)


print('#9==== Calculate the sum of all numeric items in my_list')
sum =0
for i in my_list:
    if type(i) is int:
        sum=sum+i
print("sum of all numeric items in my_list is:", sum)

print('#10==== Create a list named my_list_str from all string item in my_list, then uppercase them')
my_list_str=[]
for i in my_list:
    if type(i) is str:
         my_list_str.append(i.upper())
print(my_list_str)

print('#11==== Create a new list named my_list_nume from all numeric items in my_list, then sort them'
 )
my_list_num=[]
for i in my_list:
    if type(i) is int:
        my_list_num.append(i)
my_list_num.sort()
print(my_list_num)

print('#12==== Find the maximum/ minimum values of my_list_num')
max=my_list_num[0]
min=my_list_num[0]
for i in my_list_num:
    if i<min:
        min=i
    if i > max:
        max=i
print("max in my_list_num :",max)
print("min in my_list_num :",min)
    


#13 Remove duplicate values from my_list_num, if have

#14 Display odd and even number of my_list_num
