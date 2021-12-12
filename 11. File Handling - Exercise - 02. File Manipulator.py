# 02. Line Numbers:
import string
from os import path

file_path = path.relpath("D:\\03. Python\\03. Python Advanced\\14. Exercise File Handling\\Even Lines.txt")
updated_text = []
with open(file_path, 'r') as file:
    counter = 1
    for line in file:
        line = line.replace("\n", "")
        letters = len([i for i in line if i.isalpha()])
        punctuations = len([i for i in line if not i.isalpha() and i != " "])
        updated_text.append(f"Line {counter}: {line} ({letters}) ({punctuations})")
        counter += 1

file_path_to_write = path.relpath("D:\\03. Python\\03. Python Advanced\\14. Exercise File Handling\\Line_Numbers.txt")
with open(file_path_to_write, 'w') as file:
    for line in updated_text:
        file.write(f"{line}\n")


