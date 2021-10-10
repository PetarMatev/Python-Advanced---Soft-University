# 01. Flatten Lists:
row_data = input().split("|")
matrix = [row_data[i].strip().split() for i in range(len(row_data))][::-1]
[[print(item, end=" ") for item in given_list] for given_list in matrix]
