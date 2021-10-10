# 03. Knight Game:
a = [1, 3, 5]
b = a
b[:] = [x + 3 for x in b]
print(b)
print(a)