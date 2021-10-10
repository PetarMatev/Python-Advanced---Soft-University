# 04. Maximal Sum:
rows, columns = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for i in range(rows)]
max_matrix = []
max_count = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        sub_matrix = [matrix[row + x][column + y] for x in range(3) for y in range(3)]
        if sum(sub_matrix) >= max_count:
            max_count = sum(sub_matrix)
            max_matrix = sub_matrix

print(f"Sum = {max_count}")
[print(max_matrix[x], max_matrix[x + 1], max_matrix[x + 2]) for x in range(0, 8, 3)]
