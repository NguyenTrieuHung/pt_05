import json

def load_json(file):
    with open(file,'r',encoding='utf-8') as f:
        json_ob=json.load(f)
    return json_ob

def write_json(file,ob):
    with open(file,'w') as f:
        json.dump(ob,f)

# 1. Write a program to read file sample.json. Display all distance and name of locations.
# 1. Viết chương trình đọc tệp sample.json. Hiển thị tất cả khoảng cách và tên của các vị trí.
print("#1-------------------------------")
def display(object):
    print("distance: ",object['distance'])
    print("name: ",object['name'])
    print("latitude: ",object["geocodes"]['main']['latitude'])
    print("longitude: ",object["geocodes"]['main']['longitude'])
    print("\n")

json_ob=load_json('sample.json')
val1 = json_ob['results']
for val2 in val1:
    display(val2)

# 2. Write a program to:_
# - Define a python object (dictionary) containing fields: date, location, gps (lat, lon), weather, population.
# - Store a python object (dictionary) into a json file name sample_w.json.
# 2. Viết chương trình để:
# - Xác định một đối tượng python (từ điển) chứa các trường: 
#   ngày tháng, vị trí, gps (vĩ độ, kinh độ), thời tiết, dân số.
# - Lưu trữ một đối tượng python (từ điển) vào một tên tệp json sample_w.json.
print("\n#2-------------------------------")
py_ob={
    'date':'22-05-2001',
    'location': 'binh giang, hai duong',
    'gps':{
        'x':12345,
        'y':67890,
    },
    'weather':'storm',
    'population':892001
}

write_json('sample_w.json',py_ob)




# 3. Write a program to to create a new json file from an existing json file (sample_w.json)
# 3. Viết chương trình để tạo tệp json mới từ tệp json hiện có (sample_w.json)
print("\n#3-------------------------------")
json_ob=load_json('sample_w.json')
write_json('sample_w2.json',json_ob)


# 4. Write a program to add new 3 users into existing json file (users.json):
# 4. Viết chương trình để thêm 3 người dùng mới vào tệp json hiện có (users.json):

'''
users.json
[
    {
        'name': 'John',
        'email': 'john@example.com',
        'age': 18,
        'address': 'John Street'
    },
    {
        'name': 'Su',
        'email': 'su@example.com',
        'age': 18,
        'address': 'Su Street'
    }
]
'''
print("\n#4-------------------------------")
check='y'

class user2():
    def __init__(self,name,age,email,add):
        self.name=name
        self.email=email
        self.age=age
        self.address=add
users=[]

while(check=='y'):
    print("Enter user infor:")
    user1=dict()
    user1['name']=input("Enter user name: ")
    user1['email']=input("Enter user email: ")
    user1['age']=int(input("Enter age of user: "))
    user1['address']=input("Enter address's user: ")
    users.append(user1)
    check=input("Do you want to continue(y/n): ")

write_json('users.json',users)

# 5. Write a program to delete users which have age is 18 from users.json file.
# 5. Viết chương trình xóa người dùng có độ tuổi 18 khỏi tệp users.json.
age=int(input("Enter age which you want to delete: "))
json_ob=load_json('users.json')
for v in json_ob:
    if v['age']==age:
        json_ob.remove(v)
write_json('users.json',json_ob)