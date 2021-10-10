# 09. Miner:
rows = int(input())  # the size of a square field in which the miner should move
possible_moves = [i for i in input().split()]  # the commands for the miner's movement
matrix = [[j for j in input().split()] for _ in range(rows)]
columns = len(matrix[0])

column = len(matrix[0])
miner = []
total_coal = len([matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] == "c"])
collected_coal = 0
Game_Over = False


def miner_location(rows, columns):
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == "s":
                miner.append(r)
                miner.append(c)
                break
        else:
            continue
        break


def move_up(matrix, miner):
    ps1, ps2 = miner[0], miner[1]
    try:
        if 0 <= ps1 - 1 < len(matrix):
            return True
    except (IndexError):
        return False


def move_down(matrix, miner):
    ps1, ps2 = miner[0], miner[1]
    try:
        if 0 <= ps1 + 1 < len(matrix):
            return True
    except (IndexError):
        return False


def move_left(matrix, miner):
    ps1, ps2 = miner[0], miner[1]
    try:
        if 0 <= ps2 - 1 < len(matrix[ps1]):
            return True
    except (IndexError):
        return False


def move_right(matrix, miner):
    ps1, ps2 = miner[0], miner[1]
    try:
        z = len(matrix[ps1])
        if 0 <= ps2 + 1 < len(matrix[ps1]):
            return True
    except (IndexError):
        return False


miner_location(rows, columns)

for move in possible_moves:

    if move == "up":
        if move_up(matrix, miner):
            miner = [int(miner[0] - 1), int(miner[1])]
            ps1, ps2 = miner[0], miner[1]
            if matrix[ps1][ps2] == "c":
                collected_coal += 1
                matrix[ps1][ps2] = "*"
                if collected_coal == total_coal:
                    print(f"You collected all coal! ({ps1}, {ps2})")
                    break
            elif matrix[ps1][ps2] == "e":
                Game_Over = True
                break

    elif move == "down":
        if move_down(matrix, miner):
            miner = [int(miner[0] + 1), int(miner[1])]
            ps1, ps2 = miner[0], miner[1]
            if matrix[ps1][ps2] == "c":
                collected_coal += 1
                matrix[ps1][ps2] = "*"
                if collected_coal == total_coal:
                    print(f"You collected all coal! ({ps1}, {ps2})")
                    break
            elif matrix[ps1][ps2] == "e":
                Game_Over = True
                break

    elif move == "left":
        if move_left(matrix, miner):
            miner = [int(miner[0]), int(miner[1] - 1)]
            ps1, ps2 = miner[0], miner[1]
            if matrix[ps1][ps2] == "c":
                collected_coal += 1
                matrix[ps1][ps2] = "*"
                if collected_coal == total_coal:
                    print(f"You collected all coal! ({ps1}, {ps2})")
                    break
            elif matrix[ps1][ps2] == "e":
                Game_Over = True
                break

    elif move == "right":
        if move_right(matrix, miner):
            miner = [int(miner[0]), int(miner[1] + 1)]
            ps1, ps2 = miner[0], miner[1]
            if matrix[ps1][ps2] == "c":
                collected_coal += 1
                matrix[ps1][ps2] = "*"
                if collected_coal == total_coal:
                    print(f"You collected all coal! ({ps1}, {ps2})")
                    break
            elif matrix[ps1][ps2] == "e":
                Game_Over = True
                break



coals_left = total_coal - collected_coal
if coals_left > 0 and not Game_Over:
    print(f"{coals_left} pieces of coal left. ({miner[0]}, {miner[1]})")

if Game_Over:
    print(f"Game over! ({ps1}, {ps2})")