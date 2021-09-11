# 03. Record Unique Names:
number = int(input())
data = set()
for i in range(number):
    command_name = input()
    data.add(command_name)

[print(name) for name in data]
