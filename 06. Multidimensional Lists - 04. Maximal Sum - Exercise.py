# 03. 2x2 Squares in Matrix:
rows, columns = [int(i) for i in input().split(" ")]
matrix = []

for i in range(rows):
    matrix.append([i for i in input().split(" ")])

identical_square_matrices = 0

for el in range(rows - 1):
    for ek in range(columns - 1):
        top_left = matrix[el][ek]
        top_right = matrix[el][ek + 1]
        bottom_left = matrix[el + 1][ek]
        bottom_right = matrix[el + 1][ek + 1]
        if top_left == top_right == bottom_left == bottom_right:
            identical_square_matrices += 1

print(identical_square_matrices)