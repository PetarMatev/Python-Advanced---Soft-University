# 05. Matrix of Palindromes:
r, c = [int(i) for i in input().split()]
matrix = []
for row in range(r):
    for column in range(c):
        item = chr(row + 97), chr(column + row + 97), chr(row + 97)
        item = "".join(list(map(str, [i for i in item])))

        if item == item[::-1]:
            matrix.append(item)

matrix = [matrix[x:x+c] for x in range(0, len(matrix), c)]
[print(*i) for i in matrix]