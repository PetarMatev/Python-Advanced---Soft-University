# 5. Fibonacci_Sequence:
from Fibonacci_Sequence import Fibonacci

while True:
    command = input()
    if command == "Stop":
        break
    define = command.split()
    if len(define) == 3:
        Current_Sequence = Fibonacci(int(define[2]))
        print(*Current_Sequence)
    else:
        Locate_num = int(define[1])
        if Locate_num in Current_Sequence:
            index = Current_Sequence.index(Locate_num)
            print(f"The number - {Locate_num} is at index {index}")
        else:
            print(f"The number {Locate_num} is not in the sequence")


# setup function for Tic-Tac-Toe

def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'?")
    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player_one_name} start first!")
