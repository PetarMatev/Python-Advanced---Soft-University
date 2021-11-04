# 03. Arguments Length:
def args_length(*args):
    if args:
        return args_length(*args[1:]) + 1
    return 0


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
