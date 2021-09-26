# 01. Sum Matrix Elements:

rows, columns = [int(i) for i in input().split(", ")]
matrix = []
for row in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

print(sum(list(map(sum, matrix))))
print(matrix)