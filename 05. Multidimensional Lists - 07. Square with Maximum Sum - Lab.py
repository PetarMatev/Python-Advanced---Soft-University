# 07. Square with Maximum Sum:
rows, columns = [int(i) for i in input().split(", ")]
matrix = []
for i in range(rows):
    line = [int(i) for i in input().split(", ")]
    matrix.append(line)

biggest_sum = 0
sub_matrix = []

for row in range(rows - 1):
    for column in range(columns - 1):
        top_left = matrix[row][column]
        top_right = matrix[row][column + 1]
        bottom_left = matrix[row + 1][column]
        bottom_right = matrix[row + 1][column + 1]

        total = sum([top_left, top_right, bottom_left, bottom_right])

        if total > biggest_sum:
            biggest_sum = total
            sub_matrix = top_left, top_right, bottom_left, bottom_right

print(sub_matrix[0], sub_matrix[1])
print(sub_matrix[2], sub_matrix[3])
print(biggest_sum)
