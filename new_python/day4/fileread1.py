'''
filename: fileread1.py
'''
# file = open('file_example.txt', 'r', encoding='utf-8')
# print(file)
# contents = file.read()

with open('file_example.txt', 'r', encoding='utf-8') as file:
    print(file)
    contents = file.read()

print(contents)

file.close()