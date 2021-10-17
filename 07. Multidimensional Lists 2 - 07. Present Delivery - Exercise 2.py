# 07. Present Delivery:
presents = int(input())
n = int(input())
matrix = [input().split() for i in range(n)]
Santa = [[r, c] for c in range(n) for r in range(n) if matrix[r][c] == "S"]
r = Santa[0][0]
c = Santa[0][1]
initial_nice_kids = len([[r, c] for c in range(n) for r in range(n) if matrix[r][c] == "V"])
nice_kids = len([[r, c] for c in range(n) for r in range(n) if matrix[r][c] == "V"])


def Santa_current_step(matrix, r, c, presents, nice_kids):
    matrix[r][c] = "S"
    nice_kids -= 1
    presents -= 1
    return nice_kids, presents


def action_for_cookie(matrix, r, c, presents, nice_kids, n):
    result = presents, nice_kids
    matrix[r][c] = "S"
    for direction in ["up", "down", "left", "right"]:
        if direction == "up" and 0 <= (r - 1):
            if matrix[r - 1][c] == "V":
                nice_kids -= 1
                presents -= 1
                if nice_kids == 0 or presents == 0:
                    matrix[r][c + 1] = "-"
                    result = presents, nice_kids
                    break
            elif matrix[r - 1][c] == "X":
                presents -= 1
                if presents == 0:
                    result = presents, nice_kids
                    matrix[r -1][c] = "-"
                    break
            matrix[r - 1][c] = "-"

        elif direction == "down" and (r + 1) < n:
            if matrix[r + 1][c] == "V":
                nice_kids -= 1
                presents -= 1
                if nice_kids == 0 or presents == 0:
                    matrix[r + 1][c] = "-"
                    result = presents, nice_kids
                    break
            elif matrix[r + 1][c] == "X":
                presents -= 1
                if presents == 0:
                    result = presents, nice_kids
                    matrix[r + 1][c] = "-"
                    break
            matrix[r + 1][c] = "-"

        elif direction == "left" and 0 <= (c - 1):
            if matrix[r][c - 1] == "V":
                nice_kids -= 1
                presents -= 1
                if nice_kids == 0 or presents == 0:
                    result = presents, nice_kids
                    matrix[r][c - 1] = "-"
                    break
            elif matrix[r][c - 1] == "X":
                presents -= 1
                if presents == 0:
                    result = presents, nice_kids
                    matrix[r][c - 1] = "-"
                    break
            matrix[r][c - 1] = "-"

        elif direction == "right" and (c + 1) < n:
            if matrix[r][c + 1] == "V":
                nice_kids -= 1
                presents -= 1
                if nice_kids == 0 or presents == 0:
                    result = presents, nice_kids
                    matrix[r][c + 1] = "-"
                    break
            elif matrix[r][c + 1] == "X":
                presents -= 1
                if presents == 0:
                    result = presents, nice_kids
                    matrix[r][c + 1] = "-"
                    break
            matrix[r][c + 1] = "-"
    return result


while True:
    try:
        command = input()
    except EOFError:
        break
    if command == "" or command == "Christmas morning":
        break

    direction = command

    if direction == "up" and 0 <= (r - 1):
        matrix[r][c] = "-"
        r -= 1
        if matrix[r][c] == "V":
            nice_kids, presents = Santa_current_step(matrix, r, c, presents, nice_kids)
        elif matrix[r][c] == "X":
            matrix[r][c] = "S"
        elif matrix[r][c] == "C":
            presents, nice_kids = action_for_cookie(matrix, r, c, presents, nice_kids, n)

    elif direction == "down" and (r + 1) < n:
        matrix[r][c] = "-"
        r += 1
        if matrix[r][c] == "V":
            nice_kids, presents = Santa_current_step(matrix, r, c, presents, nice_kids)
        elif matrix[r][c] == "X":
            matrix[r][c] = "S"
        elif matrix[r][c] == "C":
            presents, nice_kids = action_for_cookie(matrix, r, c, presents, nice_kids, n)

    elif direction == "left" and 0 <= (c - 1):
        matrix[r][c] = "-"
        c -= 1
        if matrix[r][c] == "V":
            nice_kids, presents = Santa_current_step(matrix, r, c, presents, nice_kids)
        elif matrix[r][c] == "X":
            matrix[r][c] = "S"
        elif matrix[r][c] == "C":
            presents, nice_kids = action_for_cookie(matrix, r, c, presents, nice_kids, n)

    elif direction == "right" and (c + 1) < n:
        matrix[r][c] = "-"
        c += 1
        if matrix[r][c] == "V":
            nice_kids, presents = Santa_current_step(matrix, r, c, presents, nice_kids)
        elif matrix[r][c] == "X":
            matrix[r][c] = "S"
        elif matrix[r][c] == "C":
            presents, nice_kids = action_for_cookie(matrix, r, c, presents, nice_kids, n)

    if presents == 0 or nice_kids == 0:
        break

if presents == 0:
    if nice_kids > 0:
        print("Santa ran out of presents!")
        [[print(*line)] for line in matrix]
        print(f"No presents for {nice_kids} nice kid/s.")
    else:
        [[print(*line)] for line in matrix]
        print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")

else:
    if nice_kids == 0:
        [[print(*line)] for line in matrix]
        print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")
    else:
        [[print(*line)] for line in matrix]
        print(f"No presents for {nice_kids} nice kid/s.")