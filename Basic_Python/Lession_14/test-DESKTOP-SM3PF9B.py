# from unicodedata import name


# class studen:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name


# stu1 = studen(1, 'hung')
# stu2 = studen(2,'toan')
# lis_stu = [stu1,stu2]

# def main():
#     print('{:<8} {:<8}'.format('ID', 'Name'))
#     for i in lis_stu:
#         print('{:<8} {:<8}'.format(i.id, i.name))
#     print("\n")


# main()
with open('text.txt') as file:
    print(file.read())