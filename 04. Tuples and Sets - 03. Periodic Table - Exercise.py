# 03. Periodic Table:
num = int(input())

elements = set()

for i in range(num):
    items = input().split()

    for j in items:
        elements.add(j)

[print(element) for element in elements]