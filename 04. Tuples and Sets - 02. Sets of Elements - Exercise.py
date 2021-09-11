# 02. Sets of Elements:

num_set_one, num_set_two = [int(i) for i in input().split()]

set_one = set()
set_two = set()

for i in range(num_set_one):
    set_one.add(int(input()))

for j in range(num_set_two):
    set_two.add(int(input()))

[print(i) for i in set_one & set_two]
