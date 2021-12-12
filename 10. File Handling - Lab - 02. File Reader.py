# 01. File Handling:
# test
try:
    file = open('D:\\03. Python\\03. Python Advanced\\13. File Handling\\01.File Handling.txt', 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")

