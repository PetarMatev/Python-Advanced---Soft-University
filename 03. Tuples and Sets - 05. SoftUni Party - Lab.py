# 05. SoftUni Party:
num_of_guests = int(input())
attending = set()

for i in range(num_of_guests):
    attending.add(input())

while True:
    command = input()
    if command == "END":
        break
    name = command
    if name in attending:
        attending.remove(name)

print(len(attending))
attending = sorted(attending)
[print(name) for name in attending if name[0].isdigit()]
[print(name) for name in attending if name[0].isalpha()]
