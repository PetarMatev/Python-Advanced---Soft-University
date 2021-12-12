# 04. File Delete:
# Create a program that deletes the file you created in the previous task.
# If you try to delete the file multiple times, print the message: 'File already deleted!'.

import os

file_path = "D:\\03. Python\\03. Python Advanced\\13. File Handling\\my_first_file.txt"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print(f"File already deleted!")
