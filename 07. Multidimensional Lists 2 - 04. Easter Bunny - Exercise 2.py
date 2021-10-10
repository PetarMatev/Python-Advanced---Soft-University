# 04. Easter Bunny:
n = int(input())
matrix = [[x for x in input().split(" ")] for i in range(n)]
bunny = [[row, column] for column in range(n) for row in range(n) if matrix[row][column] == "B"]
directions = ["up", "down", "left", "right"]
r = bunny[0][0]
c = bunny[0][1]

max_eggs = 0
best_direction = None
coordinates = []

current_total = 0
current_coordinates = []

for direction in directions:
    for el in range(1, n):

        if direction == "left":
            if 0 <= c - el:
                if matrix[r][c - el] == "X":
                    break
                current_total += int(matrix[r][c - el])
                current_coordinates.append([r, c - el])

        elif direction == "right":
            if c + el < n:
                if matrix[r][c + el] == "X":
                    break
                current_total += int(matrix[r][c + el])
                current_coordinates.append([r, c + el])

        elif direction == "up":
            if 0 <= r - el:
                if matrix[r - el][c] == "X":
                    break
                current_total += int(matrix[r - el][c])
                current_coordinates.append([r - el, c])

        elif direction == "down":
            if r + el < n:
                if matrix[r + el][c] == "X":
                    break
                current_total += int(matrix[r + el][c])
                current_coordinates.append([r + el, c])

    if current_total >= max_eggs:
        max_eggs = current_total
        best_direction = direction
        coordinates = current_coordinates

    current_total = 0
    current_coordinates = []

print(best_direction)
[print(i) for i in coordinates]
print(max_eggs)
