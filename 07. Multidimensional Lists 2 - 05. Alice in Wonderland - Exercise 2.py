# 05. Alice in Wonderland:
n = int(input())
territory = [[i for i in input().split(" ")] for x in range(n)]
position_of_Alice = [[r, c] for c in range(n) for r in range(n) if territory[r][c] == "A"]

r = position_of_Alice[0][0]
c = position_of_Alice[0][1]
territory[r][c] = "*"

tea_bags_total = 0

Alice_did_not_make_it_to_the_tea_party = False
Alice_made_it_to_the_tea_party = False

while True:
    command = input()
    if command == "":
        Alice_did_not_make_it_to_the_tea_party = True
        break
    direction = command
    if direction == "up":

        if 0 <= r - 1:
            r -= 1
            if territory[r][c] == "R":
                Alice_did_not_make_it_to_the_tea_party = True
                territory[r][c] = "*"
                break
            elif territory[r][c].isnumeric():
                tea_bags_total += int(territory[r][c])
                territory[r][c] = "*"
                if tea_bags_total >= 10:
                    Alice_made_it_to_the_tea_party = True
                    break
            territory[r][c] = "*"
        else:
            Alice_did_not_make_it_to_the_tea_party = True
            break
        territory[r][c] = "*"

    elif direction == "down":

        if r + 1 < n:
            r += 1
            if territory[r][c] == "R":
                Alice_did_not_make_it_to_the_tea_party = True
                territory[r][c] = "*"
                break
            elif territory[r][c].isnumeric():
                tea_bags_total += int(territory[r][c])
                territory[r][c] = "*"
                if tea_bags_total >= 10:
                    Alice_made_it_to_the_tea_party = True
                    break
            territory[r][c] = "*"
        else:
            Alice_did_not_make_it_to_the_tea_party = True
            break
        territory[r][c] = "*"

    elif direction == "left":

        if 0 <= c - 1:
            c -= 1
            if territory[r][c] == "R":
                Alice_did_not_make_it_to_the_tea_party = True
                territory[r][c] = "*"
                break
            elif territory[r][c].isnumeric():
                tea_bags_total += int(territory[r][c])
                territory[r][c] = "*"
                if tea_bags_total >= 10:
                    Alice_made_it_to_the_tea_party = True
                    break
            territory[r][c] = "*"
        else:
            Alice_did_not_make_it_to_the_tea_party = True
            break

    elif direction == "right":
        if c + 1 < n:
            c += 1
            if territory[r][c] == "R":
                Alice_did_not_make_it_to_the_tea_party = True
                territory[r][c] = "*"
                break
            elif territory[r][c].isnumeric():
                tea_bags_total += int(territory[r][c])
                territory[r][c] = "*"
                if tea_bags_total >= 10:
                    Alice_made_it_to_the_tea_party = True
                    break
            territory[r][c] = "*"
        else:
            Alice_did_not_make_it_to_the_tea_party = True
            break

if Alice_did_not_make_it_to_the_tea_party:
    print("Alice didn't make it to the tea party.")
    [print(*line) for line in territory]
elif Alice_made_it_to_the_tea_party:
    print("She did it! She went to the party.")
    [print(*line) for line in territory]
