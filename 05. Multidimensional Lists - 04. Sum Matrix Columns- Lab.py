# 03. Flattening Matrix:

rows = int(input())
matrix = []

for row in range(rows):
    line = [int(i) for i in input().split(", ")]
    matrix.append(line)

flattened = []
for item in matrix:
    for element in item:
        flattened.append(element)

print(flattened)
