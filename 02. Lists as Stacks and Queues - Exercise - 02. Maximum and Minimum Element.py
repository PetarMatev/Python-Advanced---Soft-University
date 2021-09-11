# 02. Maximum and Minimum Element:
stack = []
num = int(input())

for i in range(num):
    command = input().split()
    lefty = int(command[0])
    if lefty == 1 and len(command) > 1:
        stack.append(int(command[1]))
    if lefty == 2:
        if len(stack) >= 1:
            stack.pop()
    if lefty == 3:
        print(max(stack))
    if lefty == 4:
        print(min(stack))

print(*stack[::-1])

