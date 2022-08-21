def get_info_employee():
    employees = []
    check = 'y'
    while check == 'y':
        first_name = input('First Name: ')
        last_name = input('last_name: ')
        employee = employee(first_name, last_name)
        check = input("Do you want to continue(y/n): ")
        employees.append(employee)
    return (employees)

def display_info_employee(students):
    for i in range(len(students)):
        print(f'------ {i+1} ------')
        display_info_employee(students[i])

def main():
    stud = get_info_employee()
    display_info_employee(stud)
# main()