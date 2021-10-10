# 02. Matrix Modification:
matrix = [[int(i) for i in input().split()] for row_ in range(int(input()))]
while True:
    command = input()
    if command == "END":
        break
    info = command.split(" ")
    text, row, col, value = info

    if text == "Add":
        if 0 <= int(row) <= (len(matrix) - 1) and 0 <= int(col) <= (len(matrix) - 1):
            matrix[int(row)][int(col)] += int(value)
        else:
            print(f"Invalid coordinates")
    elif text == "Subtract":
        if 0 <= int(row) <= (len(matrix) - 1) and 0 <= int(col) <= (len(matrix) - 1):
            matrix[int(row)][int(col)] -= int(value)
        else:
            print(f"Invalid coordinates")

[print(*matrix[i]) for i in range(len(matrix))]

