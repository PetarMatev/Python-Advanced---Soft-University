# 03. Knight Game:
N = int(input())
chess = [[k for k in input()] for i in range(N)]
knights = [[row, col] for row in range(N) for col in range(N) if chess[row][col] == "K"]
max_reach = 0
a, b = 0, 0
reachable_knights = {}
possible_moves = [[a - 1, b - 2], [a - 1, b + 2], [a + 1, b - 2], [a + 1, b + 2],
                  [a - 2, b - 1], [a - 2, b + 1], [a + 2, b + 1], [a + 2, b - 1]]


def get_reach_of_knights(knights, possible_moves, a, b, max_reach, reachable_knights):
    knights = [[row, col] for row in range(N) for col in range(N) if chess[row][col] == "K"]
    for i in range(len(knights)):
        r, c = knights[i]
        for move in range(8):
            x, y = possible_moves[move]
            row_, column = (r + x), (c + y)
            try:
                if 0 <= row_ and 0 <= column:
                    if chess[row_][column] == "K":
                        max_reach += 1
            except(IndexError):
                pass
        if max_reach > 0:
            reachable_knights[r, c] = max_reach
            max_reach = 0
    reachable_knights = sorted(reachable_knights.items(), key=lambda item: -item[1])
    return reachable_knights

reachable_knights = get_reach_of_knights(knights, possible_moves, a, b, max_reach, reachable_knights)

if len(reachable_knights) == 0:
    print(len(reachable_knights))
else:
    eliminated = 0
    for _ in range(len(reachable_knights)):
        knighty, reach = reachable_knights[0]
        reachable_knights = reachable_knights[1:]
        r, c = knighty
        chess[r][c] = 0
        eliminated += 1

        reachable_knights = {}
        reachable_knights = get_reach_of_knights(knights, possible_moves, a, b, max_reach, reachable_knights)
        if len(reachable_knights) == 0:
            print(eliminated)
            break
