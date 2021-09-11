# 06. Balanced Parentheses:

text = ([i for i in input()])

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

stack = []

for i in text:
    if i in open_list:
        stack.append(i)
    elif i in close_list:
        position = close_list.index(i)
        if len(stack) > 0 and open_list[position] == stack[len(stack) - 1]:
            stack.pop()
        else:
            break

if len(stack) == 0:
    print("YES")
else:
    print("NO")
