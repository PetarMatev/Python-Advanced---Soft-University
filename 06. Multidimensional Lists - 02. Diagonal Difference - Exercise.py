# 02. Diagonal Difference:
n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(i) for i in input().split()])

primary_diagonal = 0
secondary_diagonal = 0


for el in range(n):
    primary_diagonal += matrix[n - n + el][n - n + el]
    secondary_diagonal += matrix[n - n + el][n - 1 - el]

absolute_difference = abs(primary_diagonal - secondary_diagonal)
print(absolute_difference)