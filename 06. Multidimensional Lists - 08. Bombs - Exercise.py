# 07. Snake Moves:
r, c = [int(i) for i in input().split()]
matrix = [[0 for i in range(c)] for j in range(r)]
snake = input()

current_index = 0
for row in range(r):
    for column in range(c):
        if row % 2 != 0:
            matrix[row][c - 1 - column] = snake[current_index]
        else:
            matrix[row][column] = snake[current_index]
        current_index += 1
        if current_index == len(snake):
            current_index = 0

[print("".join(list(map(str, current_row)))) for current_row in matrix]