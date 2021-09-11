# 01. Reverse Numbers with a Stack:

text = input().split()
stack = []

for i in range(len(text)):
    item = text.pop()
    stack.append(item)

print(*stack)

