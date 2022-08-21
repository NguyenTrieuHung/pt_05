#1. Write a program to read the entire file sample.txt
# 1. Viết chương trình để đọc toàn bộ tệp sample.txt

from random import sample


def read_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

        
read_file('sample.txt')

#2. Write a program to read the first/last n lines of sample.txt file 
#   with n and the first/last line is supposed to be
# 2. Viết chương trình để đọc n dòng đầu tiên / cuối cùng của tệp sample.txt
# với n và dòng đầu tiên / cuối cùng được nhap
def read_file_first_last(filename, n, first=True):
    with open(filename, 'r') as f:
        lines = f.readlines()
        if first:
            print(f'{n} first lines:')
            print(lines[:n])
        else:
            print(f'{n} last lines:')
            print(lines[-n:])





#3. Write a program to read each line in the sample.txt file and store them in a list. 
#   Sort the lis
# 3. Viết chương trình để đọc từng dòng trong tệp sample.txt và lưu trữ chúng trong danh sách.

def read_file_line(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines.sort(key=len)
        for line in lines:
            print(line)

# read_file_line('sample.txt')

#4. Write a program that appends a line to the sample.txt file 
#   with the line as the argument coming from the keyboard. longest line.
#4. Viết chương trình nối một dòng vào tệp sample.txt
# với dòng là đối số đến từ bàn phím. dòng dài nhất.

def append_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)
        lines = f.readlines()
        print(f'File length: {len(lines)}')
        lines.sort(key=len)
        print('The longest sentence is:')
        print(lines[-1])

# text = input('Enter a text: ')
# append_file('sample.txt', text) 

#5. Write a program to count the frequency of occurrence of each word in the sample.txt file. 
#   11 U ticice.py
# 5. Viết chương trình đếm tần suất xuất hiện của từng từ trong tệp sample.txt.
# 11 U ticice.py

def word_count(filename):
    word_count = dict()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    print(word_count)

# word_count('sample.txt')

#6. Write a program that deletes a line where the line number is an argument from the keyboard.
# 6. Viết chương trình xóa một dòng mà số dòng là một đối số khỏi bàn phím.

def delete_line(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for idx, line in enumerate(lines):
            if idx != n:
                f.write(line)
# n = int(input('Enter the line number: '))
# delete_line('sample.txt', n)



#7. Write a program to store the following content in the file name sample_w.txt 
#   Remove blank line in the file.
# 7. Viết chương trình để lưu trữ nội dung sau trong tên tệp sample_w.txt
# Xóa dòng trống trong tệp.
def write_file(filename, text):
    with open(filename, 'w') as fw: 
        fw.write(text)


'''''
While CMR demonstrates extreme competence in capturing all types of data, 
here are the specific means through which it benefits your business that has started 
screen sharing 
1. Expand scope of CMR automation allows you to leverage 85% of the untapped 
and unstructured data common in your organization, which means you get enhanced resolution 
2. Greater accuracy with solid data CMR provides better capture rate with more than 
80% accuracy of consistently collecting information. CMR allows you to promote data level
'''