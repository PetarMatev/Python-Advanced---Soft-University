# Diagonals:
num = int(input())
matrix = [[int(i) for i in input().split(", ")] for i in range(num)]

diagonal_one = []
diagonal_two = []

for i in range(num):
    diagonal_one.append(matrix[i][i])
    diagonal_two.append(matrix[i][num - i - 1])

print(f"Primary diagonal: {', '.join(map(str,diagonal_one))}. Sum: {sum(diagonal_one)}")
print(f"Secondary diagonal: {', '.join(map(str,diagonal_two))}. Sum: {sum(diagonal_two)}")
