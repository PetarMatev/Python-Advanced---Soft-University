# 02. ASCII Art:
from pyfiglet import figlet_format


def print_art_message(msg):
    ascii_art = figlet_format(msg)
    print(ascii_art)


print_art_message(input())

