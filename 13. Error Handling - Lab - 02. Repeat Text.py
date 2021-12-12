# 02. Repeat Text:
try:
    text = input()
    times = int(input())
    repeat_text = text * times
    print(repeat_text)
except ValueError:
    print("Variable times must be an integer")
