# 03. Knight Game:
# 03. Knight Game:
N = int(input())
chess = [[k for k in input()] for i in range(N)]

knights = [[row, col] for row in range(N) for col in range(N) if chess[row][col] == "K"]
max_reach = 0
a, b = 0, 0
possible_moves = [[a - 1, b - 2], [a - 1, b + 2], [a + 1, b - 2], [a + 1, b + 2],
                  [a - 2, b - 1], [a - 2, b + 1], [a + 2, b + 1], [a + 2, b - 1]]

reachable_knights = {}

def get_reach_of_knights(knights, possible_moves, a, b, max_reach):
    global Chess
    global reachable_knights
    sorted_reachable_knights = {}
    for i in range(len(knights)):
        knight = knights[i]
        r, c = knight
        if chess[r][c] == "K":
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
                reachable_knights[r,c]=max_reach
                max_reach = 0
    sorted_reachable_knights = sorted(reachable_knights.items(), key=lambda item: -item[1])
    return sorted_reachable_knights


resultss = get_reach_of_knights(knights, possible_moves, a, b, max_reach)
if len(resultss) == 0:
    print(len(resultss))
else:
    eliminated = 0


    def residual(knights, possible_moves, a, b, max_reach):
        global Chess
        residual_sorting = {}
        for i in range(len(knights)):
            knight = knights[i]
            r, c = knight
            if chess[r][c] == "K":
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
                    residual_sorting[r, c] = max_reach
                    max_reach = 0
        residual_sorting = sorted(residual_sorting.items(), key=lambda item: -item[1])
        return residual_sorting


    for item in range(len(resultss)):
        knighty, reach = resultss[0]
        resultss = resultss[1:]
        r, c = knighty
        if chess[r][c] == "K":
            chess[r][c] = 0
            eliminated += 1
            remaining_knights = [[row, col] for row in range(N) for col in range(N) if chess[row][col] == "K"]
            new_result = residual(remaining_knights, possible_moves, a, b, max_reach)
            z = len(new_result)
            v = new_result
            if len(new_result) == 0:
                print(eliminated)
                break


