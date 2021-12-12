# 02. File Reader:
try:
    file = open('D:\\03. Python\\03. Python Advanced\\13. File Handling\\numbers.txt', 'r')
    print(sum([int(i) for i in file]))
except FileNotFoundError:
    print("File not found")
