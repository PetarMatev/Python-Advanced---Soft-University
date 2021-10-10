# 06. Matrix Shuffling:
r, c = [int(i) for i in input().split()]
mtx = [[i for i in input().split()] for i in range(r)]

while True:
    command = input()
    if command == "END":
        break
    if "swap" not in command or len(command.split()) != 5:
        print(f"Invalid input!")
    else:
        n = [int(i) for i in command.split()[1:]]
        num_list = [item for item in n if item < 0 or item > len(mtx)]
        if len(num_list) > 0:
            print(f"Invalid input!")
        else:
            mtx[n[0]][n[1]], mtx[n[2]][n[3]] = mtx[n[2]][n[3]], mtx[n[0]][n[1]]
            [print(*i) for i in mtx]