# 05. Primary Diagonal:

size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

sum_diagonal = 0
for i in range(size):
    sum_diagonal += matrix[size - i - 1][size - i - 1]
print(sum_diagonal)

