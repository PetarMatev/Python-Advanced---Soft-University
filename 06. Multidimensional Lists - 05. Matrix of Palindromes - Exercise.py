# 04. Maximal Sum:
rows, columns = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for i in range(rows)]
sub_matrix = []
max_count = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        one = matrix[row][column]
        two = matrix[row][column + 1]
        three = matrix[row][column + 2]
        four = matrix[row + 1][column]
        five = matrix[row + 1][column + 1]
        six = matrix[row + 1][column + 2]
        seven = matrix[row + 2][column + 0]
        eight = matrix[row + 2][column + 1]
        nine = matrix[row + 2][column + 2]

        total = sum([int(i) for i in (one, two, three, four, five, six, seven, eight, nine)])

        if total >= max_count:
            max_count = total
            dummy = (one, two, three, four, five, six, seven, eight, nine)
            sub_matrix = []
            [sub_matrix.append(dummy[i]) for i in range(len(dummy))]

print(f"Sum = {max_count}")
for i in range(0, 8, 3):
    print(f"{sub_matrix[i]} {sub_matrix[i + 1]} {sub_matrix[i + 2]}")

