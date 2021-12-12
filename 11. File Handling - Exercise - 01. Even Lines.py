# 01. even Lines:
from os import path

file_path = path.relpath("D:\\03. Python\\03. Python Advanced\\14. Exercise File Handling\\Even Lines.txt")
with open(file_path, 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            symbols = ["-", ",", ".", "!", "?"]
            for sym in symbols:
                if sym in line:
                    line = line.replace(sym, '@')

            list_of_words = line.split()
            for i in reversed(list_of_words):
                print("".join(i), end=" ")
            print(" ")



