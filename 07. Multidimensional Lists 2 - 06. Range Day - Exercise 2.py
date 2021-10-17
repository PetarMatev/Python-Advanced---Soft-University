# 06. Range Day:
matrix = [[i for i in input().split(" ")] for x in range(5)]
position = [[row, col] for col in range(5) for row in range(5) if matrix[row][col] == "A"]
targets = len([[row, col] for col in range(5) for row in range(5) if matrix[row][col] == "x"])

r = position[0][0]
c = position[0][1]

all_the_targets_were_shot = False
count_targets = []

for i in range(int(input())):
    command = input().split()
    if "move" == command[0]:
        direction, steps = command[1], command[2]
        steps = int(steps)

        if direction == "right":
            if c + steps < 5 and matrix[r][c + steps] == ".":
                matrix[r][c + steps] = "A"
                matrix[r][c] = "."
                c += steps

        elif direction == "left":
            if 0 <= c - steps and matrix[r][c - steps] == ".":
                matrix[r][c - steps] = "A"
                matrix[r][c] = "."
                c -= steps

        elif direction == "up":
            if 0 <= r - steps and matrix[r - steps][c] == ".":
                matrix[r - steps][c] = "A"
                matrix[r][c] = "."
                r -= steps

        elif direction == "down":
            if r + steps < 5 and matrix[r + steps][c] == ".":
                matrix[r + steps][c] = "A"
                matrix[r][c] = "."
                r += steps

    elif "shoot" == command[0]:
        direction_ = command[1]

        if direction_ == "right":
            for x in range(1, 5):
                if c + x < 5 and matrix[r][c + x] == "x":
                    count_targets.append([r, c + x])
                    matrix[r][c + x] = "."
                    break

        elif direction_ == "left":
            for x in range(1, 5):
                if 0 <= c - x and matrix[r][c - x] == "x":
                    count_targets.append([r, c - x])
                    matrix[r][c - x] = "."
                    break

        elif direction_ == "up":
            for x in range(1, 5):
                if 0 <= r - x and matrix[r - x][c] == "x":
                    count_targets.append([r - x, c])
                    matrix[r - x][c] = "."
                    break

        elif direction_ == "down":
            for x in range(1, 5):
                if r + x < 5 and matrix[r + x][c] == "x":
                    count_targets.append([r + x, c])
                    matrix[r + x][c] = "."
                    break

    if targets == len(count_targets):
        all_the_targets_were_shot = True
        break

if all_the_targets_were_shot:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets - len(count_targets)} targets left.")

[print(target) for target in count_targets]
