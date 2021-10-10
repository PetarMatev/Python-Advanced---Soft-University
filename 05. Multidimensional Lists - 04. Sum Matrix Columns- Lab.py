# 04. Sum Matrix Columns:

rows, columns = [int(i) for i in input().split(", ")]
matrix = []

for row in range(rows):
    line = [int(i) for i in input().split()]
    matrix.append(line)

for el in range(columns):
    sum_matrix_column = 0
    for ek in range(rows):
        item_in_a_column = matrix[ek][el]
        sum_matrix_column += item_in_a_column
    print(sum_matrix_column)


