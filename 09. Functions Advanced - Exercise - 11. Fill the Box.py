# 11. Fill the Box:

def fill_the_box(height, length, width, *args, dimension=None):
    if dimension is None:
        dimension = height * length * width

    if args[0] == "Finish" or not args or dimension <= 0:
        if dimension > 0:
            return f"There is free space in the box. You could put {dimension} more cubes."
        return f"No more free space! You have {sum([i for i in args if str(i).isdigit()]) - dimension} more cubes."

    return fill_the_box(height, length, width, *args[1:], dimension=dimension - args[0])


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
