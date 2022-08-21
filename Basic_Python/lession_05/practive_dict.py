
''' 1. From two lists, create a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
'''
print('#1====')
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
D=dict(zip(keys,values))
print(D)

print('#1====')
# Way 2
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# empty dictionary
res_dict = dict()
for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)


'''2. Frome two dictionaries, merge into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''
print('#2====')
from itertools import chain
from collections import defaultdict
from unicodedata import name
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = defaultdict(list)
for k, v in chain(dict1.items(), dict2.items()):
    dict3[k].append(v)

for k, v in dict3.items():
    print(k, v)

result = dict(dict2, **dict1)
print(result)

'''3. Print the value of key 'physics' from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}Q
'''
print('#3====')
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['physics'])


'''4. Initialize dictionary with default values 
Given:
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Expected output:
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 
'Emma': {'designation': 'Developer', 'salary': 8000}}
'''
print('#4====')
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
newdict={key:defaults for key in employees}
print(newdict)

'''5. Create a dictionary by extracting the keys from a given dictionary
Given:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
Keys to extract
keys = ["name", "salary"]
Expected output:
{'name': 'Kelly', 'salary': 8000}
'''
print('#5====')
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
ND={key:sample_dict[key] for key in keys}
print(ND)


'''6. Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
Keys to remove
keys = ["name", "salary"]
Expected output:
{'city': 'New york', 'age': 25}
'''

print('#6========')
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)    

print('#66========')
# way 2
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
sample_dict = {k:sample_dict[k] for k in sample_dict.keys()-keys}
print(sample_dict)

'''7. Check if value 200 exists in the following dictionary.
Given:
sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:
200 present in a dict
'''
print('#7========')
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
     print("200 present in a dict")
        
'''8. Rename a key city to a location in the following dictionary
Given:
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''
print('#8========')
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location']=sample_dict.pop("city")
print(sample_dict)




'''9. Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
'''
print('#9========')
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(sample_dict.get(65))


'''10. Change Brad’s salary to 8500 in the following dictionary.
Given:
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
Expected output:
{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
'''

