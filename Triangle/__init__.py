def print_triangle(size):
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(size, 1, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()

