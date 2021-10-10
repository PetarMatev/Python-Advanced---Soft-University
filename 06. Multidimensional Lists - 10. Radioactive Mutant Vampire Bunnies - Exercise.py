# 10. Radioactive Mutate Vampire Bunnies:
n, m = input().split()
matrix = [[cell for cell in input()] for row in range(int(n))]
directions = [d for d in input()]
get_position = [[int(r), int(c)] for r in range(int(n)) for c in range(int(m)) if matrix[r][c] == "P"][0]
ps1 = get_position[0]
ps2 = get_position[1]
bunny_reached_person = False

def Function_to_print_when_person_is_dead(n, m):
    global matrix
    global ps1
    global ps2
    [print("".join([str(n) for n in matrix[m]])) for m in range((int(n)))]
    print(f"dead: {ps1} {ps2}")
    exit()

def Function_to_print_when_person_escapes_and_wins(n, m):
    global matrix
    global ps1
    global ps2
    matrix[ps1][ps2] = "."
    Function_to_add_bunnies_to_the_matrix(n, m)
    [print("".join([str(n) for n in matrix[m]])) for m in range((int(n)))]
    print(f"won: {ps1} {ps2}")
    exit()

def Function_to_add_bunnies_to_the_matrix(n, m):
    global matrix
    global ps1
    global ps2
    global bunny_reached_person
    bunnies = [[r, c] for r in range(int(n)) for c in range(int(m)) if matrix[r][c] == "B"]

    for bunny in bunnies:
        row, column = bunny
        for x in range(1, 2):

            if 0 <= row - x:
                if matrix[row - x][column] == "P":
                    bunny_reached_person = True
                matrix[row - x][column] = "B"

            if row + x < int(n):
                if matrix[row + x][column] == "P":
                    bunny_reached_person = True
                matrix[row + x][column] = "B"

            if 0 <= column - x:
                if matrix[row][column - x] == "P":
                    bunny_reached_person = True
                matrix[row][column - x] = "B"

            if column + x < int(m):
                if matrix[row][column + x] == "P":
                    bunny_reached_person = True
                matrix[row][column + x] = "B"

    if bunny_reached_person:
        Function_to_print_when_person_is_dead(n, m)

def Person_moves_to_the_left(n, m):
    global matrix
    global ps1
    global ps2
    if 0 <= (ps2 - 1):
        if matrix[ps1][ps2 - 1] == "B":
            ps2 -= 1
            Function_to_add_bunnies_to_the_matrix(n, m)
        else:
            matrix[ps1][ps2] = "."
            ps2 -= 1
            matrix[ps1][ps2] = "P"
            Function_to_add_bunnies_to_the_matrix(n, m)
    else:
        Function_to_print_when_person_escapes_and_wins(n, m)

def Person_moves_to_the_Right(n, m):
    global matrix
    global ps1
    global ps2
    if (ps2 + 1) < int(m):
        if matrix[ps1][ps2 + 1] == "B":
            ps2 += 1
            Function_to_add_bunnies_to_the_matrix(n, m)
        else:
            matrix[ps1][ps2] = "."
            ps2 += 1
            matrix[ps1][ps2] = "P"
            Function_to_add_bunnies_to_the_matrix(n, m)
    else:
        Function_to_print_when_person_escapes_and_wins(n, m)

def Person_moves_UP(n, m):
    global matrix
    global ps1
    global ps2
    if 0 <= (ps1 - 1):
        if matrix[ps1 - 1][ps2] == "B":
            ps1 -= 1
            Function_to_add_bunnies_to_the_matrix(n, m)
        else:
            matrix[ps1][ps2] = "."
            ps1 -= 1
            matrix[ps1][ps2] = "P"
            Function_to_add_bunnies_to_the_matrix(n, m)
    else:
        Function_to_print_when_person_escapes_and_wins(n, m)

def Person_moves_Down(n, m):
    global matrix
    global ps1
    global ps2
    if (ps1 + 1) < int(n):
        if matrix[ps1 + 1][ps2] == "B":
            ps1 += 1
            Function_to_add_bunnies_to_the_matrix(n, m)
        else:
            matrix[ps1][ps2] = "."
            ps1 += 1
            matrix[ps1][ps2] = "P"
            Function_to_add_bunnies_to_the_matrix(n, m)
    else:
        Function_to_print_when_person_escapes_and_wins(n, m)

for direction in directions:
    if direction == "L":
        Person_moves_to_the_left(n, m)
    elif direction == "R":
        Person_moves_to_the_Right(n, m)
    elif direction == "U":
        Person_moves_UP(n, m)
    elif direction == "D":
        Person_moves_Down(n, m)
