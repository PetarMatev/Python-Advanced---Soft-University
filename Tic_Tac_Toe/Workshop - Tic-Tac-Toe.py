# Workshop - Tic-Tac-Toe Game:
from math import ceil


def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    correct_game_symbol_selected = False
    while not correct_game_symbol_selected:
        try:
            player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'?")
            if player_one_sign == "X" or player_one_name == "O":
                correct_game_symbol_selected = True
            else:
                print(f"Please choose correct symbol")
        except:
            print(f"Please choose correct symbol")

    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
    print(f"{player_one_name} start first!")


basket_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def play(current_player, board):
    free_position_between_1_and_9 = False
    while not free_position_between_1_and_9:
        try:
            choice = (int(input(f"{current_player[0]} choose a free position [1-9]: ")))
            if 1 <= choice and choice <= 9:
                if choice in basket_of_nums:
                    basket_of_nums.remove(choice)
                    free_position_between_1_and_9 = True
                else:
                    print(f"Selected number has been taken! Please try again!")
            else:
                print(f"Please select a number between 1 and 9!")
        except:
            print(f"Please select a free position")
    row = ceil(choice / 3) - 1
    col = choice % 3 - 1
    board[row][col] = current_player[1]
    draw_board(board)
    check_if_won(current_player, board)


def draw_board(board):
    for row in board:
        print(f"| ", end='')
        print(f" | ".join([str(x) for x in row]), end='')
        print(f" |")


def check_if_won(current_player, board):
    global loop
    first_row = all([X == current_player[1] for X in board[0]])
    second_row = all([X == current_player[1] for X in board[1]])
    third_row = all([X == current_player[1] for X in board[2]])
    first_col = all(X == current_player[1] for X in [board[0][0], board[1][0], board[2][0]])
    second_col = all(X == current_player[1] for X in [board[0][1], board[1][1], board[2][1]])
    third_col = all(X == current_player[1] for X in [board[0][2], board[1][2], board[2][2]])
    first_diag = all(X == current_player[1] for X in [board[0][0], board[1][1], board[2][2]])
    second_diag = all(X == current_player[1] for X in [board[2][0], board[1][1], board[0][2]])

    if any([first_row, second_row, third_row, first_col, second_col, third_col, first_diag, second_diag]):
        print(f"{current_player[0]} won!")
        loop = False


player_one = None
player_two = None
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
setup()

current_turn = player_one
next_turn = player_two
loop = True

while loop:
    play(current_turn, board)
    current_turn, next_turn = next_turn, current_turn
