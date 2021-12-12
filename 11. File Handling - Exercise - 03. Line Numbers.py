# 03. File Manipulator:
from os import path
import os
import fileinput
import sys

file_path = path.relpath("D:\\03. Python\\03. Python Advanced\\14. Exercise File Handling")

while True:
    command = input()
    if command == "End":
        break
    instruction = command.split("-")
    if instruction[0] == "Create":
        Create_Fine_Name = instruction[1]
        directory = f"{file_path}\\{Create_Fine_Name}"
        with open(directory, 'w') as file:
            file.write("")

    elif instruction[0] == "Add":
        Add_Fine_Name = instruction[1]
        content = instruction[2]
        directory = f"{file_path}\\{Add_Fine_Name}"
        with open(directory, 'a') as file:
            content_to_append = f"{content}\n"
            file.write(content_to_append)

    elif instruction[0] == "Replace":
        Replace_Fine_Name = instruction[1]
        old_string = instruction[2]
        new_string = instruction[3]
        directory = f"{file_path}\\{Replace_Fine_Name}"
        if os.path.exists(directory):
            with open(directory, 'r') as file:
                list_of_lines = file.readlines()

                for index, line in enumerate(list_of_lines):
                    if old_string in line:
                        line = line.replace(old_string, new_string)
                        list_of_lines[index] = line

                with open(directory, 'w') as file:
                    file.writelines(list_of_lines)
        else:
            print(f"An error occurred")

    elif instruction[0] == "Delete":
        Delete_Fine_Name = instruction[1]
        directory = f"{file_path}\\{Delete_Fine_Name}"
        if os.path.exists(directory):
            os.remove(directory)
        else:
            print(f"An error occurred")
