# 06. Symbol in Matrix:
rows = int(input())
columns = rows

matrix = []
symbol_has_been_found = False
symbol_location = None

for i in range(rows):
    line = [x for x in input()]
    matrix.append(line)

symbol = input()

for row in range(rows):
    for column in range(columns):
        current_cell = matrix[row][column]
        if current_cell == symbol:
            symbol_has_been_found = True
            symbol_location = [row, column]
        if symbol_has_been_found:
            break

if symbol_has_been_found:
    print(f"({symbol_location[0]}, {symbol_location[1]})")
else:
    print(f"{symbol} does not occur in the matrix")



