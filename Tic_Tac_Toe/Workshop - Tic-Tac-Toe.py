# Workshop - Tic-Tac-Toe Game:
from Tic_Tac_Toe import *

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

